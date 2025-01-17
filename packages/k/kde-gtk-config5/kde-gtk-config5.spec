#
# spec file for package kde-gtk-config5
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


%bcond_without lang
Name:           kde-gtk-config5
Version:        5.19.3
Release:        0
Summary:        Daemon for GTK2 and GTK3 Applications Appearance Under KDE
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            http://projects.kde.org/kde-gtk-config
Source:         https://download.kde.org/stable/plasma/%{version}/kde-gtk-config-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/kde-gtk-config-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 0.0.9
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(x11)
# Needed for syncing GTK+ settings
Requires:       xsettingsd
Suggests:       gtk2-metatheme-breeze
Suggests:       gtk3-metatheme-breeze
Supplements:    packageand(plasma5-workspace:libgtk-2_0-0)
Supplements:    packageand(plasma5-workspace:libgtk-3-0)
Provides:       kde-gtk-config = %{version}
Obsoletes:      kde-gtk-config < %{version}
# Existed only up to 5.17
Obsoletes:      %{name}-lang < %{version}

%description
kde-gtk-config is a KDED module which configures GTK2 and GTK3 applications
appearance under KDE.

%package gtk2
Summary:        GTK2 Preview Helper for the GTK Configuration
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:libgtk-2_0-0)

%description gtk2
This package contains a helper application that allows previewing
the GTK2 application style from within the application style KCM

%package gtk3
Summary:        GTK3 Preview Helper for the GTK Configuration
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:libgtk-3-0)

%description gtk3
This package contains a helper application that allows previewing
the GTK3 application style from within the application style KCM

%prep
%autosetup -p1 -n kde-gtk-config-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%files
%license COPYING*
%dir %{_kf5_libdir}/gtk-3.0/
%dir %{_kf5_libdir}/gtk-3.0/modules/
%{_kf5_libdir}/gtk-3.0/modules/libcolorreload-gtk-module.so
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kded
%{_kf5_plugindir}/kf5/kded/gtkconfig.so
%dir %{_kf5_sharedir}/kcm-gtk-module/
%{_kf5_sharedir}/kcm-gtk-module/preview.ui

%dir %{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kconf_update/gtkconfig.upd
%dir %{_kf5_libdir}/kconf_update_bin/
%{_kf5_libdir}/kconf_update_bin/gtk_theme

%files gtk2
%license COPYING*
%{_kf5_libdir}/libexec/gtk_preview
%{_kf5_libdir}/libexec/reload_gtk_apps

%files gtk3
%license COPYING*
%{_kf5_libdir}/libexec/gtk3_preview

%changelog
