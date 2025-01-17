#
# spec file for package xdg-desktop-portal
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


Name:           xdg-desktop-portal
Version:        1.6.0
Release:        0
Summary:        A portal frontend service for Flatpak
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://github.com/flatpak/xdg-desktop-portal
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
# PATCH-FEATURE-UPSTREAM xdg-dp-port-pipewire-3-api.patch -- Port to use new pipewire-3.0 api
Patch0:         xdg-dp-port-pipewire-3-api.patch
Patch1:         0001-Fix-use-after-free-in-xdg_get_app_info_from_pid.patch
Patch2:         0002-add-AssumedAppArmorLabel-key-to-D-Bus-service-files.patch
Patch3:         0003-Fix-criticals-if-no-default-handler-for-desired-type.patch

BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.5.2
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.2.90
BuildRequires:  pkgconfig(libportal)
# Break cycle: we buildrequire flatpak, and flatpak has a requires on xdg-desktop-portal
#!BuildIgnore:  xdg-desktop-portal

%description
A portal frontend service for Flatpak and possibly other desktop containment frameworks.

xdg-desktop-portal works by exposing a series of D-Bus interfaces known as portals under
a well-known name (org.freedesktop.portal.Desktop) and object path (/org/freedesktop/portal/desktop).

The portal interfaces include APIs for file access, opening URIs, printing and others.

%package devel
Summary:        A portal frontend service for Flatpak -- Development files
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
A portal frontend service for Flatpak and possibly other desktop containment frameworks.

xdg-desktop-portal works by exposing a series of D-Bus interfaces known as portals under
a well-known name (org.freedesktop.portal.Desktop) and object path (/org/freedesktop/portal/desktop).

This package contains convenience files for developers.

%lang_package

%prep
%autosetup -p1

%build
export LANG=C.UTF-8
autoreconf -fiv
%configure \
	--enable-geoclue \
	--enable-pipewire \
	%{nil}
%make_build

%install
export LANG=C.UTF-8
%make_install
%find_lang %{name}

%files
%license COPYING
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/interfaces
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Desktop.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Documents.service
%{_datadir}/doc/xdg-desktop-portal/
%{_libexecdir}/xdg-desktop-portal
%{_prefix}/lib/systemd/user/xdg-document-portal.service
%{_prefix}/lib/systemd/user/xdg-permission-store.service
%{_libexecdir}/xdg-document-portal
%{_libexecdir}/xdg-permission-store
%{_userunitdir}/xdg-desktop-portal.service

%files devel
%{_datadir}/pkgconfig/xdg-desktop-portal.pc

%files lang -f %{name}.lang

%changelog
