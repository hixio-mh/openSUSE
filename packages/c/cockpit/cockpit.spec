#
# Copyright (C) 2014-2020 Red Hat, Inc.
#
# Cockpit is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2.1 of the License, or
# (at your option) any later version.
#
# Cockpit is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Cockpit; If not, see <http://www.gnu.org/licenses/>.
#

#
# This file is maintained at the following location:
# https://github.com/cockpit-project/cockpit/blob/master/tools/cockpit.spec
#
# If you are editing this file in another location, changes will likely
# be clobbered the next time an automated release is done.
#
# Check first cockpit-devel@lists.fedorahosted.org
#
# Globals that may be defined elsewhere
#  * Version 122
#  * wip 1
#

# earliest base that the subpackages work on; the instances of this get computed/updated
# by tools/gen-spec-dependencies during "make dist", but keep a hardcoded fallback
%define required_base 122

# we generally want CentOS packages to be like RHEL; special cases need to check %{centos} explicitly
%if 0%{?centos}
%define rhel %{centos}
%endif

%if "%{!?__python3:1}"
%define __python3 /usr/bin/python3
%endif

# for testing this already gets set in fedora.install, as we want the target
# VERSION_ID, not the mock chroot's one
%if "%{!?os_version_id:1}"
%define os_version_id %(. /etc/os-release; echo $VERSION_ID)
%endif

%define _hardened_build 1

# define to build the dashboard
%define build_dashboard 1

# build basic packages like cockpit-bridge
%define build_basic 1
# build optional extensions like cockpit-docker
%define build_optional 1

%define __lib lib

%if 0%{?rhel}
%define vdo_on_demand 1
%endif

%if 0%{?suse_version}
%define pamdir /%{_lib}/security
%else
%define pamdir %{_libdir}/security
%endif

Name:           cockpit
Summary:        Web Console for Linux servers

License:        LGPL-2.1-or-later
URL:            https://cockpit-project.org/

Version:        222
%if %{defined wip}
Release:        1.%{wip}%{?dist}
Source0:        cockpit-%{version}.tar.xz
%else
Release:        0
Source0:        https://github.com/cockpit-project/cockpit/releases/download/%{version}/cockpit-%{version}.tar.xz
%endif
Source1:       cockpit.pam
Source2:       cockpit-rpmlintrc

BuildRequires: gcc
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(polkit-agent-1) >= 0.105
BuildRequires: pam-devel

BuildRequires: autoconf automake
BuildRequires: /usr/bin/python3
BuildRequires: gettext >= 0.19.7
%if %{defined build_dashboard}
BuildRequires: libssh-devel >= 0.8.5
%endif
BuildRequires: openssl-devel
BuildRequires: gnutls-devel >= 3.4.3
BuildRequires: zlib-devel
BuildRequires: pkgconfig(krb5) >= 1.11
BuildRequires: libxslt-devel
BuildRequires: glib-networking
BuildRequires: sed

BuildRequires: glib2-devel >= 2.37.4
# this is for runtimedir in the tls proxy ace21c8879
BuildRequires: pkgconfig(libsystemd) >= 235
%if 0%{?suse_version}
BuildRequires: distribution-release
BuildRequires: libpcp-devel
BuildRequires: pcp-devel
BuildRequires: libpcp3
BuildRequires: libpcp_import1
BuildRequires: openssh
BuildRequires: distribution-logos
BuildRequires: wallpaper-branding
%else
BuildRequires: pcp-libs-devel
BuildRequires: openssh-clients
BuildRequires: docbook-style-xsl
%endif
BuildRequires: krb5-server
BuildRequires: gdb

# For documentation
BuildRequires: xmlto

# This is the "cockpit" metapackage. It should only
# Require, Suggest or Recommend other cockpit-xxx subpackages

Requires: cockpit-bridge
Requires: cockpit-ws
Requires: cockpit-system

# Optional components
Recommends: (cockpit-storaged if udisks2)
Recommends: cockpit-packagekit
Suggests: cockpit-pcp

%ifarch x86_64 %{arm} aarch64 ppc64le i686 s390x
%if (0%{?fedora} == 31 || 0%{?suse_version}) && 0%{?build_optional}
%define build_docker 1
Recommends: (cockpit-docker if /usr/bin/docker)
%endif
%endif

%if 0%{?rhel} == 0
Recommends: (cockpit-networkmanager if NetworkManager)
Suggests: cockpit-selinux
%endif
%if 0%{?rhel} && 0%{?centos} == 0
Recommends: subscription-manager-cockpit
%endif

%prep
%setup -q -n cockpit-%{version}
%autopatch -p1
cp %SOURCE1 tools/cockpit.pam

%build
exec 2>&1
%configure \
    --disable-silent-rules \
    --with-cockpit-user=cockpit-ws \
    --with-cockpit-ws-instance-user=cockpit-wsinstance \
    --with-selinux-config-type=etc_t \
    --with-appstream-data-packages='[ "appstream-data" ]' \
    --with-nfs-client-package='"nfs-utils"' \
%if 0%{?suse_version}
    --docdir=%_defaultdocdir/%{name} \
%endif
    --with-pamdir='%{pamdir}' \
    %{?vdo_on_demand:--with-vdo-package='"vdo"'}
make -j4 %{?extra_flags} all

%check
exec 2>&1
# HACK: Fedora koji builders are very slow, unreliable, and inaccessible for debugging; https://github.com/cockpit-project/cockpit/issues/13909
%if 0%{?fedora} >= 0
%ifarch s390x
%define testsuite_fail || true
%endif
%endif
# HACK: RHEL i686 builders hang after running all tests; not a supported architecture, so don't bother
%if 0%{?rhel} >= 8
%ifarch i686
%define testsuite_skip #
%endif
%endif
%{?testsuite_skip} make -j4 check %{?testsuite_fail}

%install
make install DESTDIR=%{buildroot}
make install-tests DESTDIR=%{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -p -m 644 tools/cockpit.pam $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/cockpit
rm -f %{buildroot}/%{_libdir}/cockpit/*.so
# shipped in firewalld since 0.6, everywhere in Fedora/RHEL 8
rm -f %{buildroot}/%{_prefix}/%{__lib}/firewalld/services/cockpit.xml
install -D -p -m 644 AUTHORS COPYING README.md %{buildroot}%{_docdir}/cockpit/

# Build the package lists for resource packages
echo '%dir %{_datadir}/cockpit/base1' > base.list
echo '%dir %{_datadir}/cockpit/base1/fonts' >> base.list
find %{buildroot}%{_datadir}/cockpit/base1 -type f >> base.list
echo '%{_sysconfdir}/cockpit/machines.d' >> base.list
echo %{buildroot}%{_datadir}/polkit-1/actions/org.cockpit-project.cockpit-bridge.policy >> base.list
echo '%dir %{_datadir}/cockpit/ssh' >> base.list
find %{buildroot}%{_datadir}/cockpit/ssh -type f >> base.list
echo '%{_libexecdir}/cockpit-ssh' >> base.list

%if %{defined build_dashboard}
echo '%dir %{_datadir}/cockpit/dashboard' >> dashboard.list
find %{buildroot}%{_datadir}/cockpit/dashboard -type f >> dashboard.list
%else
rm -rf %{buildroot}/%{_datadir}/cockpit/dashboard
touch dashboard.list
%endif

echo '%dir %{_datadir}/cockpit/pcp' >> pcp.list
find %{buildroot}%{_datadir}/cockpit/pcp -type f >> pcp.list

echo '%dir %{_datadir}/cockpit/tuned' >> system.list
find %{buildroot}%{_datadir}/cockpit/tuned -type f >> system.list

echo '%dir %{_datadir}/cockpit/shell' >> system.list
find %{buildroot}%{_datadir}/cockpit/shell -type f >> system.list

echo '%dir %{_datadir}/cockpit/systemd' >> system.list
find %{buildroot}%{_datadir}/cockpit/systemd -type f >> system.list

echo '%dir %{_datadir}/cockpit/users' >> system.list
find %{buildroot}%{_datadir}/cockpit/users -type f >> system.list

echo '%dir %{_datadir}/cockpit/kdump' >> kdump.list
find %{buildroot}%{_datadir}/cockpit/kdump -type f >> kdump.list

echo '%dir %{_datadir}/cockpit/sosreport' > sosreport.list
find %{buildroot}%{_datadir}/cockpit/sosreport -type f >> sosreport.list

echo '%dir %{_datadir}/cockpit/storaged' > storaged.list
find %{buildroot}%{_datadir}/cockpit/storaged -type f >> storaged.list

echo '%dir %{_datadir}/cockpit/networkmanager' > networkmanager.list
find %{buildroot}%{_datadir}/cockpit/networkmanager -type f >> networkmanager.list

echo '%dir %{_datadir}/cockpit/packagekit' >> packagekit.list
find %{buildroot}%{_datadir}/cockpit/packagekit -type f >> packagekit.list

echo '%dir %{_datadir}/cockpit/apps' >> packagekit.list
find %{buildroot}%{_datadir}/cockpit/apps -type f >> packagekit.list

echo '%dir %{_datadir}/cockpit/machines' > machines.list
find %{buildroot}%{_datadir}/cockpit/machines -type f >> machines.list

echo '%dir %{_datadir}/cockpit/selinux' > selinux.list
find %{buildroot}%{_datadir}/cockpit/selinux -type f >> selinux.list

echo '%dir %{_datadir}/cockpit/playground' > tests.list
find %{buildroot}%{_datadir}/cockpit/playground -type f >> tests.list

%if 0%{?build_docker}
echo '%dir %{_datadir}/cockpit/docker' > docker.list
find %{buildroot}%{_datadir}/cockpit/docker -type f >> docker.list
%else
rm -rf %{buildroot}/%{_datadir}/cockpit/docker
rm -f %{buildroot}/%{_prefix}/share/metainfo/org.cockpit-project.cockpit-docker.metainfo.xml
touch docker.list
%endif

# when not building basic packages, remove their files
%if 0%{?build_basic} == 0
for pkg in base1 branding motd kdump networkmanager selinux shell sosreport ssh static systemd tuned users; do
    rm -r %{buildroot}/%{_datadir}/cockpit/$pkg
    rm -f %{buildroot}/%{_datadir}/metainfo/org.cockpit-project.cockpit-${pkg}.metainfo.xml
done
for data in doc locale man pixmaps polkit-1; do
    rm -r %{buildroot}/%{_datadir}/$data
done
for lib in systemd tmpfiles.d firewalld; do
    rm -r %{buildroot}/%{_prefix}/%{__lib}/$lib
done
for libexec in cockpit-askpass cockpit-session cockpit-ws cockpit-tls cockpit-wsinstance-factory cockpit-desktop; do
    rm %{buildroot}/%{_libexecdir}/$libexec
done
rm -r %{buildroot}/%{_libdir}/security %{buildroot}/%{_sysconfdir}/pam.d %{buildroot}/%{_sysconfdir}/motd.d %{buildroot}/%{_sysconfdir}/issue.d
rm %{buildroot}/usr/bin/cockpit-bridge %{buildroot}/usr/sbin/remotectl
rm -f %{buildroot}%{_libexecdir}/cockpit-ssh
rm -f %{buildroot}%{_datadir}/metainfo/cockpit.appdata.xml
%endif

# when not building optional packages, remove their files
%if 0%{?build_optional} == 0
for pkg in apps dashboard docker machines packagekit pcp playground storaged; do
    rm -rf %{buildroot}/%{_datadir}/cockpit/$pkg
done
# files from -tests
rm -r %{buildroot}/%{_prefix}/%{__lib}/cockpit-test-assets
# files from -pcp
rm -r %{buildroot}/%{_libexecdir}/cockpit-pcp %{buildroot}/%{_localstatedir}/lib/pcp/
# files from -machines
rm -f %{buildroot}/%{_prefix}/share/metainfo/org.cockpit-project.cockpit-machines.metainfo.xml
# files from -storaged
rm -f %{buildroot}/%{_prefix}/share/metainfo/org.cockpit-project.cockpit-storaged.metainfo.xml
# files from -docker
rm -f %{buildroot}/%{_prefix}/share/metainfo/org.cockpit-project.cockpit-docker.metainfo.xml
%endif

sed -i "s|%{buildroot}||" *.list

%if 0%{?suse_version}
# remove brandings with stale symlinks. Means they don't match
# the distro.
pushd %{buildroot}/%{_datadir}/cockpit/branding
find -L * -type l -printf "%H\n" | sort -u | xargs rm -rv
ln -s opensuse-tumbleweed opensuse-microos
popd
# need this in SUSE as post build checks dislike stale symlinks
install -m 644 -D /dev/null %{buildroot}/run/cockpit/motd
# remove files of not installable packages
rm -r %{buildroot}%{_datadir}/cockpit/{machines,sosreport,selinux}
rm -f %{buildroot}/%{_prefix}/share/metainfo/org.cockpit-project.cockpit-{machines,selinux,sosreport}.metainfo.xml
rm -f %{buildroot}%{_datadir}/pixmaps/cockpit-sosreport.png
%else
%global _debugsource_packages 1
%global _debuginfo_subpackages 0

%define find_debug_info %{_rpmconfigdir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_include_minidebuginfo:-m} %{?_find_debuginfo_dwz_opts} %{?_find_debuginfo_opts} %{?_debugsource_packages:-S debugsourcefiles.list} "%{_builddir}/%{?buildsubdir}"

# Redefine how debug info is built to slip in our extra debug files
%define __debug_install_post   \
   %{find_debug_info} \
   cat debug.partial >> %{_builddir}/%{?buildsubdir}/debugfiles.list \
%{nil}

# Build the package lists for debug package, and move debug files to installed locations
find %{buildroot}/usr/src/debug%{_datadir}/cockpit -type f -o -type l > debug.partial
sed -i "s|%{buildroot}/usr/src/debug||" debug.partial
sed -n 's/\.map\(\.gz\)\?$/\0/p' *.list >> debug.partial
sed -i '/\.map\(\.gz\)\?$/d' *.list
tar -C %{buildroot}/usr/src/debug -cf - . | tar -C %{buildroot} -xf -
%endif
# /suse_version
rm -rf %{buildroot}/usr/src/debug

# On RHEL kdump, networkmanager, selinux, and sosreport are part of the system package
%if 0%{?rhel}
cat kdump.list sosreport.list networkmanager.list selinux.list >> system.list
rm -f %{buildroot}%{_datadir}/metainfo/org.cockpit-project.cockpit-sosreport.metainfo.xml
rm -f %{buildroot}%{_datadir}/metainfo/org.cockpit-project.cockpit-kdump.metainfo.xml
rm -f %{buildroot}%{_datadir}/metainfo/org.cockpit-project.cockpit-selinux.metainfo.xml
rm -f %{buildroot}%{_datadir}/pixmaps/cockpit-sosreport.png
%endif

%if 0%{?build_basic}
%find_lang cockpit
%endif

# -------------------------------------------------------------------------------
# Basic Sub-packages

%if 0%{?build_basic}

%description
The Cockpit Web Console enables users to administer GNU/Linux servers using a
web browser.

It offers network configuration, log inspection, diagnostic reports, SELinux
troubleshooting, interactive command-line sessions, and more.

%files
%{_docdir}/cockpit/AUTHORS
%{_docdir}/cockpit/COPYING
%{_docdir}/cockpit/README.md
%dir %{_datadir}/cockpit
%{_datadir}/metainfo/cockpit.appdata.xml
%{_datadir}/pixmaps/cockpit.png
%doc %{_mandir}/man1/cockpit.1.gz


%package bridge
Summary: Cockpit bridge server-side component
Requires: glib-networking
Provides: cockpit-ssh = %{version}-%{release}
# cockpit-ssh moved from dashboard to bridge in 171
Conflicts: cockpit-dashboard < 170.x
# PR #10430 dropped workaround for ws' inability to understand x-host-key challenge
Conflicts: cockpit-ws < 181.x

%description bridge
The Cockpit bridge component installed server side and runs commands on the
system on behalf of the web based user interface.

%files bridge -f base.list
%doc %{_mandir}/man1/cockpit-bridge.1.gz
%{_bindir}/cockpit-bridge
%{_libexecdir}/cockpit-askpass

%package doc
Summary: Cockpit deployment and developer guide
BuildArch: noarch

%description doc
The Cockpit Deployment and Developer Guide shows sysadmins how to
deploy Cockpit on their machines as well as helps developers who want to
embed or extend Cockpit.

%files doc
%exclude %{_docdir}/cockpit/AUTHORS
%exclude %{_docdir}/cockpit/COPYING
%exclude %{_docdir}/cockpit/README.md
%{_docdir}/cockpit

%package system
Summary: Cockpit admin interface package for configuring and troubleshooting a system
BuildArch: noarch
Requires: cockpit-bridge >= %{version}-%{release}
%if !0%{?suse_version}
Requires: shadow-utils
%endif
Requires: grep
Requires: /usr/bin/pwscore
Requires: /usr/bin/date
Provides: cockpit-shell = %{version}-%{release}
Provides: cockpit-systemd = %{version}-%{release}
Provides: cockpit-tuned = %{version}-%{release}
Provides: cockpit-users = %{version}-%{release}
%if 0%{?rhel}
Provides: cockpit-networkmanager = %{version}-%{release}
Obsoletes: cockpit-networkmanager
Requires: NetworkManager >= 1.6
Provides: cockpit-kdump = %{version}-%{release}
Requires: kexec-tools
Recommends: polkit
Recommends: PackageKit
Recommends: NetworkManager-team
Recommends: setroubleshoot-server >= 3.3.3
Provides: cockpit-selinux = %{version}-%{release}
Provides: cockpit-sosreport = %{version}-%{release}
Requires: sos
%endif
%if 0%{?fedora} >= 29
# 0.7.0 (actually) supports task cancellation.
# 0.7.1 fixes tasks never announcing completion.
Recommends: (reportd >= 0.7.1 if abrt)
%endif
# NPM modules which are also available as packages
Provides: bundled(js-jquery) = 3.5.1
Provides: bundled(js-moment) = 2.25.3
Provides: bundled(nodejs-flot) = 0.8.3
Provides: bundled(xstatic-bootstrap-datepicker-common) = 1.9.0
Provides: bundled(xstatic-patternfly-common) = 3.59.4

%description system
This package contains the Cockpit shell and system configuration interfaces.

%files system -f system.list
%dir %{_datadir}/cockpit/shell/images

%package ws
Summary: Cockpit Web Service
Requires: glib-networking
Requires: openssl
Requires: glib2 >= 2.37.4
Conflicts: firewalld < 0.6.0-1
Recommends: sscg >= 2.3
Recommends: system-logos
Requires: systemd >= 235
Suggests: sssd-dbus
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description ws
The Cockpit Web Service listens on the network, and authenticates users.

If sssd-dbus is installed, you can enable client certificate/smart card
authentication via sssd/FreeIPA.

%files ws -f cockpit.lang
%doc %{_mandir}/man1/cockpit-desktop.1.gz
%doc %{_mandir}/man5/cockpit.conf.5.gz
%doc %{_mandir}/man8/cockpit-ws.8.gz
%doc %{_mandir}/man8/cockpit-tls.8.gz
%doc %{_mandir}/man8/remotectl.8.gz
%doc %{_mandir}/man8/pam_cockpit_cert.8.gz
%doc %{_mandir}/man8/pam_ssh_add.8.gz
%dir %{_sysconfdir}/cockpit
%config(noreplace) %{_sysconfdir}/cockpit/ws-certs.d
%config(noreplace) %{_sysconfdir}/pam.d/cockpit
%config %{_sysconfdir}/issue.d/cockpit.issue
# dir is not owned by pam in openSUSE
%dir %{_sysconfdir}/motd.d
%config %{_sysconfdir}/motd.d/cockpit
%ghost /run/cockpit/motd
%ghost %dir /run/cockpit
%dir %{_datadir}/cockpit/motd
%{_datadir}/cockpit/motd/update-motd
%{_datadir}/cockpit/motd/inactive.motd
%{_unitdir}/cockpit.service
%{_unitdir}/cockpit-motd.service
%{_unitdir}/cockpit.socket
%{_unitdir}/cockpit-wsinstance-http.socket
%{_unitdir}/cockpit-wsinstance-http.service
%{_unitdir}/cockpit-wsinstance-http-redirect.socket
%{_unitdir}/cockpit-wsinstance-http-redirect.service
%{_unitdir}/cockpit-wsinstance-https-factory.socket
%{_unitdir}/cockpit-wsinstance-https-factory@.service
%{_unitdir}/cockpit-wsinstance-https@.socket
%{_unitdir}/cockpit-wsinstance-https@.service
%{_unitdir}/system-cockpithttps.slice
%{_prefix}/%{__lib}/tmpfiles.d/cockpit-tempfiles.conf
%{_sbindir}/remotectl
%{pamdir}/pam_ssh_add.so
%{pamdir}/pam_cockpit_cert.so
%{_libexecdir}/cockpit-ws
%{_libexecdir}/cockpit-wsinstance-factory
%{_libexecdir}/cockpit-tls
%{_libexecdir}/cockpit-desktop
%attr(4750, root, cockpit-wsinstance) %{_libexecdir}/cockpit-session
%attr(775, -, wheel) %{_localstatedir}/lib/cockpit
%{_datadir}/cockpit/static
%{_datadir}/cockpit/branding

%pre ws
getent group cockpit-ws >/dev/null || groupadd -r cockpit-ws
getent passwd cockpit-ws >/dev/null || useradd -r -g cockpit-ws -d /nonexisting -s /sbin/nologin -c "User for cockpit web service" cockpit-ws
getent group cockpit-wsinstance >/dev/null || groupadd -r cockpit-wsinstance
getent passwd cockpit-wsinstance >/dev/null || useradd -r -g cockpit-wsinstance -d /nonexisting -s /sbin/nologin -c "User for cockpit-ws instances" cockpit-wsinstance

%post ws
%systemd_post cockpit.socket
# firewalld only partially picks up changes to its services files without this
test -f %{_bindir}/firewall-cmd && firewall-cmd --reload --quiet || true

%preun ws
%systemd_preun cockpit.socket

%postun ws
%systemd_postun_with_restart cockpit.socket
%systemd_postun_with_restart cockpit.service

# -------------------------------------------------------------------------------
# Sub-packages that are part of cockpit-system in RHEL/CentOS, but separate in Fedora

%if 0%{?rhel} == 0

%package kdump
Summary: Cockpit user interface for kernel crash dumping
Requires: cockpit-bridge >= 122
Requires: cockpit-shell >= 122
Requires: kexec-tools
BuildArch: noarch

%description kdump
The Cockpit component for configuring kernel crash dumping.

%files kdump -f kdump.list
%{_datadir}/metainfo/org.cockpit-project.cockpit-kdump.metainfo.xml

%if !0%{?suse_version}
%package sosreport
Summary: Cockpit user interface for diagnostic reports
Requires: cockpit-bridge >= 122
Requires: cockpit-shell >= 122
Requires: sos
BuildArch: noarch

%description sosreport
The Cockpit component for creating diagnostic reports with the
sosreport tool.

%files sosreport -f sosreport.list
%{_datadir}/metainfo/org.cockpit-project.cockpit-sosreport.metainfo.xml
%{_datadir}/pixmaps/cockpit-sosreport.png
%endif

%package networkmanager
Summary: Cockpit user interface for networking, using NetworkManager
Requires: cockpit-bridge >= 186
Requires: cockpit-shell >= 186
Requires: NetworkManager >= 1.6
# Optional components
Recommends: NetworkManager-team
BuildArch: noarch

%description networkmanager
The Cockpit component for managing networking.  This package uses NetworkManager.

%files networkmanager -f networkmanager.list

%endif

%if 0%{?rhel} == 0 && !0%{?suse_version}

%package selinux
Summary: Cockpit SELinux package
Requires: cockpit-bridge >= 122
Requires: cockpit-shell >= 122
Requires: setroubleshoot-server >= 3.3.3
BuildArch: noarch

%description selinux
This package contains the Cockpit user interface integration with the
utility setroubleshoot to diagnose and resolve SELinux issues.

%files selinux -f selinux.list
%{_datadir}/metainfo/org.cockpit-project.cockpit-selinux.metainfo.xml

%endif

#/ build basic packages
%else

# RPM requires this
%description
Dummy package from building optional packages only; never install or publish me.

#/ build basic packages
%endif

# -------------------------------------------------------------------------------
# Sub-packages that are optional extensions

%if 0%{?build_optional}

%package -n cockpit-storaged
Summary: Cockpit user interface for storage, using udisks
Requires: cockpit-shell >= 186
Requires: udisks2 >= 2.6
Recommends: udisks2-lvm2 >= 2.6
Recommends: udisks2-iscsi >= 2.6
Recommends: device-mapper-multipath
Recommends: clevis-luks
Requires: %{__python3}
%if 0%{?suse_version}
Requires: python3-dbus-python
%else
Requires: python3-dbus
%endif
BuildArch: noarch

%description -n cockpit-storaged
The Cockpit component for managing storage.  This package uses udisks.

%files -n cockpit-storaged -f storaged.list
%dir %{_datadir}/cockpit/storaged/images
%{_datadir}/metainfo/org.cockpit-project.cockpit-storaged.metainfo.xml

%package -n cockpit-tests
Summary: Tests for Cockpit
Requires: cockpit-bridge >= 138
Requires: cockpit-system >= 138
Requires: /usr/bin/ssh-agent /usr/bin/ssh-add
Provides: cockpit-test-assets = %{version}-%{release}

%description -n cockpit-tests
This package contains tests and files used while testing Cockpit.
These files are not required for running Cockpit.

%files -n cockpit-tests -f tests.list
%{_prefix}/%{__lib}/cockpit-test-assets

%if !0%{?suse_version}
%package -n cockpit-machines
BuildArch: noarch
Summary: Cockpit user interface for virtual machines
Requires: cockpit-bridge >= 186
Requires: cockpit-system >= 186
%if 0%{?suse_version}
Requires: libvirt-daemon-qemu
%else
Requires: libvirt-daemon-kvm
%endif
Requires: libvirt-client
Requires: libvirt-dbus >= 1.2.0
# Optional components
Recommends: virt-install
Recommends: libosinfo
Recommends: python3-gobject-base

%description -n cockpit-machines
The Cockpit components for managing virtual machines.

If "virt-install" is installed, you can also create new virtual machines.

%files -n cockpit-machines -f machines.list
%{_datadir}/metainfo/org.cockpit-project.cockpit-machines.metainfo.xml
%endif

%package -n cockpit-pcp
Summary: Cockpit PCP integration
Requires: cockpit-bridge >= 134.x
Requires(post): pcp

%description -n cockpit-pcp
Cockpit support for reading PCP metrics and loading PCP archives.

%files -n cockpit-pcp -f pcp.list
%{_libexecdir}/cockpit-pcp
%{_localstatedir}/lib/pcp/config/pmlogconf/tools/cockpit

%post -n cockpit-pcp
# HACK - https://bugzilla.redhat.com/show_bug.cgi?id=1185764
# We can't use "systemctl reload-or-try-restart" since systemctl might
# be out of sync with reality.
/usr/share/pcp/lib/pmlogger condrestart

%if %{defined build_dashboard}
%package -n cockpit-dashboard
Summary: Cockpit remote server dashboard
BuildArch: noarch
Requires: cockpit-ssh >= 135
Conflicts: cockpit-ws < 135

%description -n cockpit-dashboard
Cockpit page for showing performance graphs for up to 20 remote servers.

%files -n cockpit-dashboard -f dashboard.list

%endif

%if 0%{?build_docker}
%package -n cockpit-docker
Summary: Cockpit user interface for Docker containers
Requires: cockpit-bridge >= 122
Requires: cockpit-shell >= 122
Requires: (docker or moby-engine or docker-ce)
Requires: %{__python3}

%description -n cockpit-docker
The Cockpit components for interacting with Docker and user interface.
This package is not yet complete.

%files -n cockpit-docker -f docker.list
%dir %{_datadir}/cockpit/docker/images
%{_datadir}/metainfo/org.cockpit-project.cockpit-docker.metainfo.xml
%endif

%package -n cockpit-packagekit
Summary: Cockpit user interface for packages
BuildArch: noarch
Requires: cockpit-bridge >= 186
Requires: PackageKit

%description -n cockpit-packagekit
The Cockpit components for installing OS updates and Cockpit add-ons,
via PackageKit.

%files -n cockpit-packagekit -f packagekit.list

#/ build optional extension packages
%endif

# The changelog is automatically generated and merged
%changelog
