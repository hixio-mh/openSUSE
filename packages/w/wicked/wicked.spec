#
# spec file for package wicked
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define		release_prefix  %{?snapshot:%{snapshot}}%{!?snapshot:0}
Name:           wicked
Version:        0.6.63
Release:        %{release_prefix}.0.0
Summary:        Network configuration infrastructure
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/openSUSE/wicked
Source0:        %{name}-%{version}.tar.bz2
Source1:        wicked-rpmlintrc
#
# Upstream First - openSUSE Build Service Policy:
#
# Never add any patches to this package without the upstream commit id in
# the patch. Any patches added here without a very good reason to make an
# exception will be silently removed with the next version update.
# Please use pull requests at https://github.com/openSUSE/wicked/ instead.
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
%if %{with wicked_devel}
# libwicked-%{version}.so shlib package compatible match for wicked-devel
Provides:       libwicked-0_6_63 = %{version}-%{release}
%endif
# uninstall obsolete libwicked-0-6 (libwicked-0.so.6, wicked < 0.6.60)
Provides:       libwicked-0-6 = %{version}
Obsoletes:      libwicked-0-6 < %{version}

%if 0%{?suse_version} >= 1500
%bcond_without  rfc4361_cid
%else
%bcond_with     rfc4361_cid
%endif
%if 0%{?suse_version} >= 1230
%bcond_without  systemd
%bcond_with     dbusstart
%else
%bcond_with     systemd
%bcond_with     dbusstart
%endif

%bcond_with     wicked_devel

# Note: nanny use is enabled by default
%bcond_without  use_nanny
%bcond_without  use_teamd

# Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
%define _fillupdir /var/adm/fillup-templates
%endif

BuildRequires:  libnl3-devel
%if 0%{?suse_version} > 1110
BuildRequires:  libiw-devel
%else
BuildRequires:  wireless-tools
%endif
BuildRequires:  dbus-1-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  pkg-config

# Prerequire the logger package
%if 0%{?suse_version} > 1310
Requires(pre):       util-linux-systemd
%else
Requires(pre):       util-linux
%endif

%if %{with systemd}
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libsystemd)
%{?systemd_requires}
%if 0%{?suse_version:1}
Requires(pre):  %fillup_prereq
Requires:       sysconfig-netconfig
%endif
Requires:       %{name}-service = %{version}
%else
%if 0%{?suse_version:1}
PreReq:         %fillup_prereq %insserv_prereq
%endif
%endif
%if %{defined _rundir}
%define         wicked_piddir   %_rundir/%{name}
%define         wicked_statedir %_rundir/%{name}
%else
%define         wicked_piddir   %_localstatedir/run/%{name}
%define         wicked_statedir %_localstatedir/run/%{name}
%endif
%define         wicked_storedir %_localstatedir/lib/%{name}

%description
Wicked is a network configuration infrastructure incorporating a number
of existing frameworks into a unified architecture, providing a DBUS
interface to network configuration.

%if %{with systemd}

%package service
Summary:        Network configuration infrastructure - systemd service
Group:          System/Management
Requires(pre):  %name = %{version}
Requires:       sysconfig >= 0.81.0
Provides:       /sbin/ifup
Provides:       sysvinit(network)
Conflicts:      otherproviders(/sbin/ifup)
Obsoletes:      sysconfig-network

%description service
Wicked is a network configuration infrastructure incorporating a number
of existing frameworks into a unified architecture, providing a DBUS
interface to network configuration.

This package provides the wicked systemd service files.

%else

%package service
Summary:        Network configuration infrastructure - SysVinit service
Group:          System/Management
Requires(pre):  %name = %{version}
Provides:       /sbin/ifup
Provides:       sysvinit(network)
# sysvinit test package only, unsupported -> no more deps

%description service
Wicked is a network configuration infrastructure incorporating a number
of existing frameworks into a unified architecture, providing a DBUS
interface to network configuration.

This package provides the wicked system V init scripts.

%endif

%if %{with wicked_devel}
%package devel
Summary:        Network configuration infrastructure - Development files
Group:          Development/Libraries/C and C++
Requires:       dbus-1-devel
Requires:       libnl3-devel
Requires:       libwicked-0_6_63 = %{version}-%{release}

%description devel
Wicked is a network configuration infrastructure incorporating a number
of existing frameworks into a unified architecture, providing a DBUS
interface to network configuration.

This package provides the wicked development files.
%endif

%prep
%setup

%build
test -x ./configure || autoreconf --force --install
export CFLAGS="-std=gnu89 $RPM_OPT_FLAGS"
%configure \
	--with-piddir=%{wicked_piddir}	\
	--with-statedir=%{wicked_statedir}\
	--with-storedir=%{wicked_storedir}\
	--with-compat=suse		\
	--with-fillup-templatesdir=%{_fillupdir}\
%if %{without rfc4361_cid}
	--disable-dhcp4-rfc4361-cid	\
%endif
%if %{without use_nanny}
	--disable-nanny-use		\
%endif
%if %{without use_teamd}
	--disable-teamd			\
%endif
%if %{with systemd}
	--enable-systemd		\
	--with-systemd-unitdir=%{_unitdir} \
%else
	--enable-systemv		\
%endif
%if ! %{with dbusstart}
	--without-dbus-servicedir	\
%endif
	--disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=${RPM_BUILD_ROOT}
# install /sbin/{ifup,ifown,ifstatus,ifprobe} links
%if "%_sbindir" != "/sbin"
%__mkdir_p -m 0755 ${RPM_BUILD_ROOT}/sbin
%__ln_s %_sbindir/ifup	${RPM_BUILD_ROOT}/sbin/ifup
%endif
%__ln_s %_sbindir/ifup	${RPM_BUILD_ROOT}/sbin/ifdown
%__ln_s %_sbindir/ifup	${RPM_BUILD_ROOT}/sbin/ifstatus
%__ln_s %_sbindir/ifup  ${RPM_BUILD_ROOT}/sbin/ifprobe
# remove libwicked.a and la
%__rm -f ${RPM_BUILD_ROOT}%_libdir/libwicked*.*a
# create reboot-persistent (leases) store directory
%__mkdir_p -m 0750 ${RPM_BUILD_ROOT}%{wicked_storedir}
%if %{with systemd}
ln -sf %_sbindir/service ${RPM_BUILD_ROOT}%_sbindir/rcwicked
ln -sf %_sbindir/service ${RPM_BUILD_ROOT}%_sbindir/rcwickedd
ln -sf %_sbindir/service ${RPM_BUILD_ROOT}%_sbindir/rcwickedd-nanny
ln -sf %_sbindir/service ${RPM_BUILD_ROOT}%_sbindir/rcwickedd-dhcp6
ln -sf %_sbindir/service ${RPM_BUILD_ROOT}%_sbindir/rcwickedd-dhcp4
ln -sf %_sbindir/service ${RPM_BUILD_ROOT}%_sbindir/rcwickedd-auto4
%else
ln -sf %_sysconfdir/init.d/wickedd ${RPM_BUILD_ROOT}%_sbindir/rcwickedd
ln -sf %_sysconfdir/init.d/network ${RPM_BUILD_ROOT}%_sbindir/rcnetwork
%endif

%if %{without wicked_devel}
pushd $RPM_BUILD_ROOT
rm -rfv \
	.%_libdir/libwicked.so \
	.%_datadir/pkgconfig/wicked.pc \
	.%_mandir/man7/wicked.7* \
	.%_includedir/wicked
popd
%endif

%if %{with systemd}

%pre service
# upgrade from sysconfig[-network] scripts
_id=`readlink /etc/systemd/system/network.service 2>/dev/null` || :
if test "x${_id##*/}" = "xnetwork.service" -a -x /etc/init.d/network ; then
	/etc/init.d/network stop-all-dhcp-clients || :
fi
%{service_add_pre wicked.service}

%post service
%{service_add_post wicked.service}
# See bnc#843526: presets do not apply for upgrade / are not sufficient
#                 to handle sysconfig-network|wicked -> wicked migration
_id=`readlink /etc/systemd/system/network.service 2>/dev/null` || :
case "${_id##*/}" in
""|wicked.service|network.service)
	/usr/bin/systemctl --system daemon-reload || :
	/usr/bin/systemctl --force enable wicked.service || :
;;
esac

%preun service
# stop the daemons on removal
# - stopping wickedd should be sufficient ... other just to be sure.
# - stopping of the wicked.service does not stop network, but removes
#   the wicked.service --> network.service link and resets its status.
%{service_del_preun wickedd.service wickedd-auto4.service wickedd-dhcp4.service wickedd-dhcp6.service wickedd-nanny.service wicked.service}

%postun service
# restart wickedd after upgrade
%{service_del_postun wickedd.service}

%else

%post service
%{fillup_and_insserv wickedd}

%preun service
if test -x /etc/init.d/wicked ; then
	%stop_on_removal wickedd
fi

%postun service
if test -x /etc/init.d/wicked ; then
	%restart_on_update wickedd
fi
%insserv_cleanup

%endif

%post
/sbin/ldconfig
%{fillup_only -dns config wicked network}
%{fillup_only -dns dhcp wicked network}
# reload dbus after install or upgrade to apply new policies
/usr/bin/systemctl reload dbus.service 2>/dev/null || :

%postun
/sbin/ldconfig
# reload dbus after uninstall, our policies are gone again
if [ ${FIRST_ARG:-$1} -eq 0 ]; then
	/usr/bin/systemctl reload dbus.service 2>/dev/null || :
fi

%files
%defattr (-,root,root)
%doc ChangeLog ANNOUNCE COPYING README TODO samples
%_sbindir/wicked
%_sbindir/wickedd
%_sbindir/wickedd-nanny
%_libdir/libwicked-*.so*
%dir %_libexecdir/%{name}
%dir %_libexecdir/%{name}/bin
%_libexecdir/%{name}/bin/wickedd-auto4
%_libexecdir/%{name}/bin/wickedd-dhcp4
%_libexecdir/%{name}/bin/wickedd-dhcp6
%dir %_sysconfdir/wicked
%config(noreplace) %_sysconfdir/wicked/common.xml
%config(noreplace) %_sysconfdir/wicked/client.xml
%config(noreplace) %_sysconfdir/wicked/server.xml
%config(noreplace) %_sysconfdir/wicked/nanny.xml
%dir %_sysconfdir/wicked/extensions
%config(noreplace) %_sysconfdir/wicked/extensions/*
%dir %_sysconfdir/wicked/ifconfig
%dir %_sysconfdir/dbus-1
%dir %_sysconfdir/dbus-1/system.d
# mark the policies as config to keep backup, but replace on upgrade
%config %_sysconfdir/dbus-1/system.d/org.opensuse.Network.conf
%config %_sysconfdir/dbus-1/system.d/org.opensuse.Network.AUTO4.conf
%config %_sysconfdir/dbus-1/system.d/org.opensuse.Network.DHCP4.conf
%config %_sysconfdir/dbus-1/system.d/org.opensuse.Network.DHCP6.conf
%config %_sysconfdir/dbus-1/system.d/org.opensuse.Network.Nanny.conf
%if %{with dbusstart}
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/system-services
%_datadir/dbus-1/system-services/org.opensuse.Network.*.service
%endif
%dir %_datadir/wicked
%dir %_datadir/wicked/schema
%_datadir/wicked/schema/*.xml
%_mandir/man5/wicked-config.5*
%_mandir/man5/ifcfg-bonding.5*
%_mandir/man5/ifcfg-bridge.5*
%_mandir/man5/ifcfg-dummy.5*
%_mandir/man5/ifcfg-macvlan.5*
%_mandir/man5/ifcfg-macvtap.5*
%_mandir/man5/ifcfg-ppp.5*
%_mandir/man5/ifcfg-ovs-bridge.5*
%_mandir/man5/ifcfg-team.5*
%_mandir/man5/ifcfg-tunnel.5*
%_mandir/man5/ifcfg-vlan.5*
%_mandir/man5/ifcfg-vxlan.5*
%_mandir/man5/ifcfg-wireless.5*
%_mandir/man5/ifcfg-dhcp.5*
%_mandir/man5/ifcfg-lo.5*
%_mandir/man5/ifcfg.5*
%_mandir/man5/ifroute.5*
%_mandir/man5/ifrule.5*
%_mandir/man5/ifsysctl.5*
%_mandir/man5/routes.5*
%_mandir/man8/wicked.8*
%_mandir/man8/wickedd.8*
%_mandir/man8/wicked-ethtool.8*
%_mandir/man8/ifdown.8*
%_mandir/man8/ifstatus.8*
%_mandir/man8/ifup.8*
%_fillupdir/sysconfig.config-wicked
%_fillupdir/sysconfig.dhcp-wicked
%attr(0750,root,root) %dir        %wicked_storedir

%if %{with systemd}

%files service
%defattr (-,root,root)
%_unitdir/wickedd-auto4.service
%_unitdir/wickedd-dhcp4.service
%_unitdir/wickedd-dhcp6.service
%_unitdir/wickedd-nanny.service
%_unitdir/wickedd.service
%_unitdir/wicked.service
%_unitdir/wickedd-pppd@.service
%attr(0600,root,root) %config /etc/sysconfig/network/ifcfg-lo
%_sbindir/ifup
%if "%_sbindir" != "/sbin"
/sbin/ifup
%endif
/sbin/ifdown
/sbin/ifstatus
/sbin/ifprobe
%_sbindir/rcwickedd-nanny
%_sbindir/rcwickedd-dhcp6
%_sbindir/rcwickedd-dhcp4
%_sbindir/rcwickedd-auto4
%_sbindir/rcwickedd
%_sbindir/rcwicked

%else

%files service
%defattr (-,root,root)
%_sysconfdir/init.d/wickedd
%_sysconfdir/init.d/network
%_sbindir/rcwickedd
%_sbindir/rcnetwork
%attr(0600,root,root) %config /etc/sysconfig/network/ifcfg-lo
%_sbindir/ifup
%if "%_sbindir" != "/sbin"
/sbin/ifup
%endif
/sbin/ifdown
/sbin/ifstatus
/sbin/ifprobe

%endif

%if %{with wicked_devel}
%files devel
%defattr (-,root,root)
%dir %_includedir/wicked
%_includedir/wicked/*
%_libdir/libwicked.so
%_datadir/pkgconfig/wicked.pc
%_mandir/man7/wicked.7*
%endif

%changelog
