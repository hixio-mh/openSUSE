#
# spec file for package kexi
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soVersion 3.2
%bcond_without lang
Name:           kexi
Version:        3.2.0
Release:        0
Summary:        Database Application
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GFDL-1.2-only
Group:          Productivity/Office/Suite
URL:            http://www.kexi-project.org/
Source0:        https://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         Fix-build-with-Qt-5_13.patch
BuildRequires:  breeze5-icons
BuildRequires:  extra-cmake-modules
BuildRequires:  glib2-devel
BuildRequires:  karchive-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdb-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kproperty-devel
BuildRequires:  kreport-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libmysqld-devel
BuildRequires:  marble-devel
BuildRequires:  mysql-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5WebKit)
BuildRequires:  cmake(Qt5WebKitWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Recommends:     %{name}-lang = %{version}
Obsoletes:      calligra-kexi < %{version}
Provides:       calligra-kexi = %{version}
# not ported yet
Obsoletes:      calligra-kexi-spreadsheet-import < %{version}
%if 0%{?suse_version} > 1500
BuildRequires:  postgresql-server-devel
%else
BuildRequires:  postgresql-devel
%endif

%description
Kexi is a visual database applications creator, competing with
programs like MS Access or Filemaker.

%package spreadsheet-import
Summary:        Spreadsheet-to-Kexi-table import plugin
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Suite
Obsoletes:      calligra-kexi-spreadsheet-import < %{version}
Provides:       calligra-kexi-spreadsheet-import = %{version}

%description spreadsheet-import
Kexi is a visual database applications creator, competing with
programs like MS Access or Filemaker.

This package contains a Spreadsheet-to-Kexi-table import plugin.

%lang_package

%prep
%autosetup -p1

%build
# install translations to %{_kf5_localedir} so they don't clash with the kexi translations in calligra-l10n (KDE4 based)
# can probably be changed back to the standard location when we have calligra 3 in all supported distributions...
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%make_jobs

%install
%kf5_makeinstall -C build

%if %{with lang}
%{kf5_find_lang}
%endif

%suse_update_desktop_file -r org.kde.kexi-%{soVersion}       Qt KDE Office Database

#Remove unwanted development files
for i in dataviewcommon formutils extendedwidgets relationsview main migrate utils guiutils datatable core undo
do
    rm %{buildroot}%{_kf5_libdir}/libkexi${i}%{soVersion}.so
done
rm %{buildroot}%{_kf5_libdir}/libkformdesigner%{soVersion}.so

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.*
%doc AUTHORS README.md
%dir %{_kf5_appstreamdir}
%dir %{_kf5_iconsdir}/hicolor/1024x1024
%dir %{_kf5_iconsdir}/hicolor/1024x1024/apps
%{_kf5_applicationsdir}/org.kde.kexi-%{soVersion}.desktop
%{_kf5_appstreamdir}/org.kde.kexi-%{soVersion}.appdata.xml
%{_kf5_bindir}/kexi-%{soVersion}
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_libdir}/libkexi*.so*
%{_kf5_libdir}/libkformdesigner%{soVersion}.so*
%{_kf5_plugindir}/kexi/
%{_kf5_sharedir}/kexi/

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
