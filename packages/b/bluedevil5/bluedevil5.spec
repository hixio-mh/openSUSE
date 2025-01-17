#
# spec file for package bluedevil5
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2010 Raymond Wooninck <tittiatcoke@gmail.com>
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


%bcond_without lang
Name:           bluedevil5
Version:        5.19.3
Release:        0
Summary:        Bluetooth Manager for KDE Plasma
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/bluedevil-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/bluedevil-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-UPSTREAM
Patch1:         0001-Port-applet-to-use-PlasmaExtras.PlaceholderMessage.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KDED) >= 5.25.0
BuildRequires:  cmake(KF5BluezQt) >= 5.25.0
BuildRequires:  cmake(KF5CoreAddons) >= 5.25.0
BuildRequires:  cmake(KF5DBusAddons) >= 5.25.0
BuildRequires:  cmake(KF5I18n) >= 5.25.0
BuildRequires:  cmake(KF5IconThemes) >= 5.25.0
BuildRequires:  cmake(KF5KIO) >= 5.25.0
BuildRequires:  cmake(KF5Notifications) >= 5.25.0
BuildRequires:  cmake(KF5Plasma) >= 5.25.0
BuildRequires:  cmake(KF5WidgetsAddons) >= 5.25.0
BuildRequires:  cmake(KF5WindowSystem) >= 5.25.0
BuildRequires:  cmake(Qt5Core) >= 5.4.0
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Qml) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
Requires:       bluez-qt-imports >= %{version}
Requires:       bluez-qt-udev >= %{version}
# atop of the bluez itself, we also need bluez-obexd for kio_obexftp and both send/receive
Requires:       bluez
# for connecting A2DP profile
Recommends:     pulseaudio-module-bluetooth
Recommends:     %{name}-lang
Supplements:    packageand(bluez:plasma5-workspace)
Conflicts:      bluedevil
Requires(post): shared-mime-info
Requires(postun): shared-mime-info

%description
Bluetooth daemon for KDE Plasma, handling connections.

%lang_package

%prep
%autosetup -p1 -n bluedevil-%{version}

%build
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
%kf5_find_lang
%endif

%post
%mime_database_post

%postun
%mime_database_postun

%files
%license COPYING*
%doc README
%dir %{_kf5_appstreamdir}/
%{_kf5_sharedir}/mime/packages/bluedevil-mime.xml
%{_kf5_applicationsdir}/org.kde.bluedevil*.desktop
%{_kf5_sharedir}/bluedevilwizard/
%{_kf5_bindir}/bluedevil-*
%{_kf5_sharedir}/remoteview/
%{_kf5_notifydir}/
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_qmldir}/
%{_kf5_plasmadir}/
%{_kf5_appstreamdir}/*.xml

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
