#
# spec file for package kdiff3
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
Name:           kdiff3
Version:        1.8.3
Release:        0
Summary:        Code Comparison Utility
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            http://kdiff3.sourceforge.net/
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core) >= 5.7.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang = %{version}

%description
KDiff3 is a program that:

* Compares or merges two or three text input files or directories

* Shows the differences line-by-line and character-by-character

* Provides an automatic merge facility and an integrated editor for
  solving merge conflicts

* Supports KDE's KIO framework (allows accessing ftp, sftp, fish, smb, etc.)

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %suse_update_desktop_file -r org.kde.kdiff3 Qt KDE Utility TextEditor X-KDE-Utilities-File
%if %{with lang}
  %find_lang %{name} %{name}.lang --with-man
  %find_lang diff_ext %{name}.lang
  %find_lang kdiff3fileitemactionplugin %{name}.lang
  %kf5_find_htmldocs
%endif
  %fdupes %{buildroot}

%files
%license COPYING
%{_kf5_applicationsdir}/org.kde.kdiff3.desktop
%{_kf5_appstreamdir}/org.kde.kdiff3.appdata.xml
%{_kf5_bindir}/kdiff3
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%{_kf5_iconsdir}/hicolor/*/apps/kdiff3.png
%{_kf5_iconsdir}/hicolor/scalable/apps/kdiff3.svgz
%{_kf5_kxmlguidir}/kdiff3/
%{_kf5_kxmlguidir}/kdiff3part/
%{_kf5_plugindir}/kf5/parts/
%{_kf5_plugindir}/kf5/kfileitemaction/
%{_kf5_servicesdir}/kdiff3part.desktop
%doc %lang(en) %{_kf5_mandir}/man1/kdiff3.1%{?ext_man}
%doc %lang(en) %{_kf5_htmldir}/en/kdiff3

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
