#
# spec file for package snapper
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# optionally build with test coverage reporting
%bcond_with coverage

Name:           snapper
Version:        0.8.11
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         snapper-%{version}.tar.bz2
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
%if 0%{?suse_version} > 1230
BuildRequires:  libbtrfs-devel
%endif
%if 0%{?suse_version} > 1310
BuildRequires:  libmount-devel >= 2.24
%endif
%if 0%{?fedora_version} >= 23
BuildRequires:  pkgconfig
BuildRequires:  systemd
%else
BuildRequires:  pkg-config
%endif
%if 0%{?fedora_version} >= 24
BuildRequires:  glibc-langpack-de
BuildRequires:  glibc-langpack-en
%endif
%if ! 0%{?mandriva_version}
%if 0%{?fedora_version} >= 23
BuildRequires:  dbus-devel
BuildRequires:  docbook-style-xsl
%else
BuildRequires:  dbus-1-devel
BuildRequires:  docbook-xsl-stylesheets
%endif
BuildRequires:  libxslt
%else
BuildRequires:  docbook-dtd45-xml
BuildRequires:  docbook-xsl
BuildRequires:  libdbus-1-devel
BuildRequires:  xsltproc
%endif
%if (0%{?suse_version} && 0%{?suse_version} >= 1210)
BuildRequires:  libzypp(plugin:commit)
%endif
BuildRequires:  pam-devel
%if 0%{?fedora_version}
BuildRequires:  json-c-devel
%else
BuildRequires:  libjson-c-devel
%endif
%if %{with coverage}
BuildRequires:  lcov
%endif
Requires:       diffutils
Requires:       libsnapper5 = %version
%if 0%{?suse_version}
Recommends:     logrotate snapper-zypp-plugin
Supplements:    btrfsprogs
%endif
Summary:        Tool for filesystem snapshot management
License:        GPL-2.0-only
Group:          System/Packages
Url:            http://snapper.io/

%description
This package contains snapper, a tool for filesystem snapshot management.

%prep
%setup

%build
%if %{with coverage}
# optimized code may confuse the coverage measurement, turn it off
# -fPIC is mysteriously needed on Fedora.
export CFLAGS="-g3 -fPIC"
export CXXFLAGS="-g3 -fPIC"
%else
export CFLAGS="%{optflags} -DNDEBUG"
export CXXFLAGS="%{optflags} -DNDEBUG"
%endif

autoreconf -fi
%configure \
	--docdir="%{_defaultdocdir}/snapper"				\
%if %{with coverage}
	--enable-coverage \
%endif
%if 0%{?suse_version} <= 1310
	--disable-rollback							\
%endif
%if 0%{?suse_version} <= 1310
	--disable-btrfs-quota							\
%endif
	--disable-silent-rules --disable-ext4
make %{?_smp_mflags}

%install
%make_install
rm -f "%{buildroot}/%{_libdir}"/*.la "%{buildroot}/%{_lib}/security/pam_snapper.la"
rm -f %{buildroot}/etc/cron.hourly/suse.de-snapper
rm -f %{buildroot}/etc/cron.daily/suse.de-snapper

%if 0%{?suse_version}
install -D -m 644 data/sysconfig.snapper "%{buildroot}%{_fillupdir}/sysconfig.snapper"
%else
install -D -m 644 data/sysconfig.snapper "%{buildroot}/etc/sysconfig/snapper"
%endif

%{find_lang} snapper

%check
make check VERBOSE=1

%pre
%if 0%{?suse_version}
%service_add_pre snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer
%endif

%post
%if 0%{?suse_version}
# special hack, since the macros were added much later than
# the systemd timer
if [ -f /etc/cron.hourly/suse.de-snapper ]; then
 systemctl preset snapper-timeline.timer || :
 systemctl is-enabled -q snapper-timeline.timer && systemctl start snapper-timeline.timer || :
fi
if [ -f /etc/cron.daily/suse.de-snapper ]; then
 systemctl preset snapper-cleanup.timer || :
 systemctl is-enabled -q snapper-cleanup.timer && systemctl start snapper-cleanup.timer || :
fi
%service_add_post snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer
%endif

%preun
%if 0%{?suse_version}
%service_del_preun snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer
%endif

%postun
%if 0%{?suse_version}
%service_del_postun snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer
%endif

%files -f snapper.lang
%defattr(-,root,root)
%{_bindir}/snapper
%{_sbindir}/snapperd
%if 0%{?suse_version} > 1310
%{_sbindir}/mksubvolume
%endif
%dir %{_prefix}/lib/snapper
%{_prefix}/lib/snapper/*-helper
%doc %{_mandir}/*/snapper.8*
%doc %{_mandir}/*/snapperd.8*
%doc %{_mandir}/*/snapper-configs.5*
%if 0%{?suse_version} > 1310
%doc %{_mandir}/*/mksubvolume.8*
%endif
%config(noreplace) %{_sysconfdir}/logrotate.d/snapper
%{_unitdir}/snapper-*.*
%config /etc/dbus-1/system.d/org.opensuse.Snapper.conf
%{_datadir}/dbus-1/system-services/org.opensuse.Snapper.service

%package -n libsnapper5
Summary:        Library for filesystem snapshot management
Group:          System/Libraries
Requires:       util-linux
%if 0%{?suse_version}
PreReq:         %fillup_prereq
%endif
# expands to Obsoletes: libsnapper1 libsnapper2 libsnapper3...
Obsoletes:      %(echo `seq -s " " -f "libsnapper%.f" $((5 - 1))`)

%description -n libsnapper5
This package contains libsnapper, a library for filesystem snapshot management.

%files -n libsnapper5
%defattr(-,root,root)
%{_libdir}/libsnapper.so.*
%dir %{_sysconfdir}/snapper
%dir %{_sysconfdir}/snapper/configs
%dir %{_sysconfdir}/snapper/config-templates
%config(noreplace) %{_sysconfdir}/snapper/config-templates/default
%dir %{_sysconfdir}/snapper/filters
%config(noreplace) %{_sysconfdir}/snapper/filters/*.txt
%doc %dir %{_defaultdocdir}/snapper
%doc %{_defaultdocdir}/snapper/AUTHORS
%doc %{_defaultdocdir}/snapper/COPYING
%if 0%{?suse_version}
%{_fillupdir}/sysconfig.snapper
%else
%config(noreplace) %{_sysconfdir}/sysconfig/snapper
%endif

%post -n libsnapper5
/sbin/ldconfig
%if 0%{?suse_version}
%{fillup_only -n snapper}
%endif

%postun -n libsnapper5 -p /sbin/ldconfig

%package -n libsnapper-devel
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel
%endif
Requires:       gcc-c++
Requires:       libacl-devel
Requires:       libsnapper5 = %version
Requires:       libstdc++-devel
Requires:       libxml2-devel
%if 0%{?suse_version} > 1230
Requires:       libbtrfs-devel
%endif
%if 0%{?suse_version} > 1310
Requires:       libmount-devel >= 2.24
%endif
Summary:        Header files and documentation for libsnapper
Group:          Development/Languages/C and C++

%description -n libsnapper-devel
This package contains header files and documentation for developing with
libsnapper.

%files -n libsnapper-devel
%defattr(-,root,root)
%{_libdir}/libsnapper.so
%{_includedir}/snapper

%package -n snapper-zypp-plugin
Requires:       snapper = %version
Requires:       libzypp(plugin:commit) = 1
Summary:        A zypp commit plugin for calling snapper
Group:          System/Packages

%description -n snapper-zypp-plugin
This package contains a plugin for zypp that makes filesystem snapshots with
snapper during commits.

%files -n snapper-zypp-plugin
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/snapper/zypp-plugin.conf
%if 0%{?suse_version} < 1210
%dir /usr/lib/zypp
%dir /usr/lib/zypp/plugins
%dir /usr/lib/zypp/plugins/commit
%endif
/usr/lib/zypp/plugins/commit/snapper-zypp-plugin
%doc %{_mandir}/*/snapper-zypp-plugin.8*
%doc %{_mandir}/*/snapper-zypp-plugin.conf.5*

%package -n pam_snapper
Requires:       pam
Requires:       snapper = %version
Summary:        PAM module for calling snapper
Group:          System/Packages

%description -n pam_snapper
A PAM module for calling snapper during user login and logout.

%files -n pam_snapper
%defattr(-,root,root)
/%{_lib}/security/pam_snapper.so
%dir /usr/lib/pam_snapper
/usr/lib/pam_snapper/*.sh
%doc %{_mandir}/*/pam_snapper.8*

%package testsuite
Summary:        Integration tests for snapper
Group:          System/Packages

%description testsuite
Tests to be run in a scratch machine to test that snapper operates as expected.

%files testsuite
%defattr(-,root,root)
%dir %{_libdir}/snapper
%dir %{_libdir}/snapper/testsuite
%{_libdir}/snapper/testsuite/*

%changelog
