#
# spec file for package heaptrack
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


%define kf5_version 5.26.0
%bcond_without lang
Name:           heaptrack
Version:        1.1.0
Release:        0
Summary:        Heap Memory Allocation Profiler
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other
Url:            https://userbase.kde.org/Heaptrack
Source0:        https://download.kde.org/stable/heaptrack/%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         Fix-compile-on-32bit.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libdwarf-devel
BuildRequires:  libunwind-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  cmake(KChart) >= 2.6.0
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(Qt5Core) >= 5.2.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(libzstd) 
Recommends:     %{name}-lang
Suggests:       heaptrack-gui
%if 0%{?suse_version} >= 1330
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
%else
BuildRequires:  boost-devel
%endif

%description
A memory profiler for Linux, tracking heap allocations.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q
%autopatch -p1

# Disable building tests, they're not used and post-build-checks trips over it
sed -i"" '/add_subdirectory(tests)/d' CMakeLists.txt

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %make_install -C build
  %if %{with lang}
    %find_lang %{name} --all-name
  %endif
  # Fixup desktop file
  %suse_update_desktop_file org.kde.heaptrack Development Profiling

%package devel
Summary:        Development files for the Heaptrack API
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description devel
This package contains files needed to develop for the Heaptrack
API.

%package gui
Summary:        GUI Frontend for Heaptrack
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description gui
A Qt5/KF5 based GUI for Heaptrack.

%files
%license COPYING*
%doc README.md
%{_kf5_bindir}/heaptrack
%{_kf5_bindir}/heaptrack_print
%{_libexecdir}/heaptrack

%files devel
%license COPYING*
%{_includedir}/heaptrack_api.h

%files gui
%license COPYING*
%{_kf5_bindir}/heaptrack_gui
%{_datadir}/applications/org.kde.heaptrack.desktop
%{_kf5_appstreamdir}/org.kde.heaptrack.appdata.xml
%dir %{_kf5_iconsdir}/hicolor/*
%dir %{_kf5_iconsdir}/hicolor/*/*
%{_kf5_iconsdir}/*/*/*/*.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
