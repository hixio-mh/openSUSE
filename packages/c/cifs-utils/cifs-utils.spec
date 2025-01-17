#
# spec file for package cifs-utils
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           cifs-utils
Version:        6.9
Release:        0
Summary:        Utilities for doing and managing mounts of the Linux CIFS filesystem
License:        GPL-3.0-or-later
Group:          System/Filesystems
URL:            http://www.samba.org/linux-cifs/cifs-utils/
# origin   git://git.samba.org/cifs-utils.git
# for-next https://github.com/piastry/cifs-utils.git
Source:         https://ftp.samba.org/pub/linux-cifs/%{name}/%{name}-%{version}.tar.bz2
Source5:        https://ftp.samba.org/pub/linux-cifs/%{name}/%{name}-%{version}.tar.bz2.asc
# http://ftp.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-pubkey_70F3B981.asc
Source6:        cifs-utils.keyring
Source100:      README.cifstab.migration
Source1:        cifs.init

Patch0:         0001-smbinfo-Improve-help-usage-and-add-h-option.patch
Patch1:         0002-smbinfo-Add-bash-completion-support-for-smbinfo.patch
Patch2:         0003-getcifsacl-Add-support-to-accept-more-paths.patch
Patch3:         0004-getcifsacl-Fix-usage-message-to-include-multiple-fil.patch
Patch4:         0005-smbinfo-add-GETCOMPRESSION-support.patch
Patch5:         0006-getcifsacl-Add-support-for-R-recursive-option.patch
Patch6:         0007-smbinfo-add-bash-completion-support-for-getcompressi.patch
Patch7:         0008-mount.cifs.c-fix-memory-leaks-in-main-func.patch
Patch8:         0009-Zero-fill-the-allocated-memory-for-new-struct-cifs_n.patch
Patch9:         0010-Zero-fill-the-allocated-memory-for-a-new-ACE.patch
Patch10:        0011-fix-doublefree.patch
Patch11:        0012-mount.cifs-Fix-invalid-free.patch

# cifs-utils 6.8 switched to python for man page generation
# we need to require either py2 or py3 package
# some products do not have a py2/py3 versions
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 120000
BuildRequires:  python3-docutils
%else
BuildRequires:  python-docutils
%endif

%if 0%{?suse_version} >= 1221
%define systemd 1
%else
%define systemd 0
%endif

%if 0%{?suse_version} < 1221
PreReq:         insserv %{?fillup_prereq}
%endif
%define         initdir %{_sysconfdir}/init.d
Provides:       cifs-mount = %{version}
Obsoletes:      cifs-mount < %{version}
%if 0%{?suse_version} > 1140
BuildRequires:  autoconf
%endif
BuildRequires:  automake
BuildRequires:  keyutils-devel
BuildRequires:  krb5-devel
%if 0%{?suse_version} > 1120
BuildRequires:  libcap-ng-devel
%else
BuildRequires:  libcap-devel
%endif
#!BuildIgnore:  samba-client
BuildRequires:  libtalloc-devel
%if 0%{?suse_version} > 1110
BuildRequires:  fdupes
%endif
BuildRequires:  libwbclient-devel
BuildRequires:  pam-devel
BuildRequires:  pkg-config
Requires:       keyutils
%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif

%description
The cifs-utils package consist of utilities for doing and managing mounts of
the Linux CIFS filesystem.

%package devel
Summary:        Files needed for building plugins for cifs-utils
Group:          Development/Libraries/C and C++

%description devel
The SMB/CIFS protocol is a standard file sharing protocol widely deployed
on Microsoft Windows machines. This package contains the header file
necessary for building ID mapping plugins for cifs-utils.

%package -n pam_cifscreds
Summary:        PAM module to manage NTLM credentials in kernel keyring
Group:          System/Libraries

%description -n pam_cifscreds
The pam_cifscreds PAM module is a tool for automatically adding
credentials (username and password) for the purpose of establishing
sessions in multiuser mounts.

When a cifs filesystem is mounted with the "multiuser" option, and does
not use krb5 authentication, it needs to be able to get the credentials
for each user from somewhere. The pam_cifscreds module can be used to
provide these credentials to the kernel automatically at login.

%prep
%setup -q
cp -a ${RPM_SOURCE_DIR}/README.cifstab.migration .
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE -fpie"
export LDFLAGS="-pie"
autoreconf -i
%configure \
	--with-pamdir=/%{_lib}/security
make %{?_smp_mflags}

%install
%if ! %{systemd}
mkdir -p %{buildroot}/%{_sysconfdir}/init.d
%endif

%make_install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
ln -s %{_libdir}/%{name}/idmapwb.so %{buildroot}%{_sysconfdir}/%{name}/idmap-plugin
mkdir -p %{buildroot}%{_sysconfdir}/request-key.d
install -m 644 -p contrib/request-key.d/cifs.idmap.conf %{buildroot}%{_sysconfdir}/request-key.d
install -m 644 -p contrib/request-key.d/cifs.spnego.conf %{buildroot}%{_sysconfdir}/request-key.d
%if 0%{?suse_version} > 1221
mkdir -p \
	%{buildroot}/%{_sysconfdir}/sysconfig/network/if-{down,up}.d \
	%{buildroot}/%{_sysconfdir}/samba \
	%{buildroot}/%{_sbindir} \
	%{buildroot}/%{_rundir}

%if ! %{systemd}
install -m 0755 -p ${RPM_SOURCE_DIR}/cifs.init %{buildroot}/%{_sysconfdir}/init.d/cifs
ln -s service %{buildroot}/%{_sbindir}/rccifs
%endif

touch %{buildroot}/%{_sysconfdir}/sysconfig/network/if-{down,up}.d/${script} \
	%{buildroot}%{_rundir}/cifs
%endif
# Hardlink duplicate files
%if 0%{?suse_version} > 1110
%fdupes %{buildroot}
%endif

%files
/sbin/mount.cifs
%{_bindir}/getcifsacl
%{_bindir}/setcifsacl
%{_sbindir}/cifs.idmap
%{_mandir}/man1/getcifsacl.1%{ext_man}
%{_mandir}/man1/setcifsacl.1%{ext_man}
%{_mandir}/man8/cifs.idmap.8%{ext_man}
%{_bindir}/cifscreds
%{_sbindir}/cifs.upcall
%{_bindir}/smbinfo
%{_mandir}/man1/cifscreds.1%{ext_man}
%{_mandir}/man1/smbinfo.1%{ext_man}
%{_mandir}/man8/cifs.upcall.8%{ext_man}
%{_mandir}/man8/mount.cifs.8%{ext_man}
%dir %{_sysconfdir}/request-key.d
%config(noreplace) %{_sysconfdir}/request-key.d/cifs.idmap.conf
%config(noreplace) %{_sysconfdir}/request-key.d/cifs.spnego.conf
%dir %{_libdir}/cifs-utils
%dir %{_sysconfdir}/cifs-utils
%config(noreplace) %{_sysconfdir}/cifs-utils/idmap-plugin
%{_libdir}/%{name}/idmapwb.so
%{_mandir}/man8/idmapwb.8%{ext_man}
%if 0%{?suse_version} > 1221
%if ! %{systemd}
%attr(0754,root,root) %config %{_sysconfdir}/init.d/cifs
%{_sbindir}/rccifs
%endif
%dir %{_sysconfdir}/samba
%ghost %{_rundir}/cifs
%endif
%doc README.cifstab.migration

%files devel
%{_includedir}/cifsidmap.h

%files -n pam_cifscreds
/%{_lib}/security/pam_cifscreds.so
%{_mandir}/man8/pam_cifscreds.8%{ext_man}

%changelog
