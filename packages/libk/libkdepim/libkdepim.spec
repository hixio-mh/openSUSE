#
# spec file for package libkdepim
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
Name:           libkdepim
Version:        20.04.3
Release:        0
Summary:        Base package of kdepim
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5AkonadiSearch)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Ldap)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package contains the libkdepim library.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%package -n libKF5Libkdepim5
Summary:        libkdepim library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKF5Libkdepim5
The libkdepim library

%package -n libKF5LibkdepimAkonadi5
Summary:        libkdepim Akonadi library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKF5LibkdepimAkonadi5
The libkdepim library for Akonadi related functions

%post -n libKF5Libkdepim5  -p /sbin/ldconfig
%postun -n libKF5Libkdepim5 -p /sbin/ldconfig
%post -n libKF5LibkdepimAkonadi5  -p /sbin/ldconfig
%postun -n libKF5LibkdepimAkonadi5 -p /sbin/ldconfig

%package devel
Summary:        Development package for libkdepim
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       libKF5Libkdepim5 = %{version}
Requires:       libKF5LibkdepimAkonadi5 = %{version}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5AkonadiContact)

%description devel
The development package for the libkdepim libraries

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5Libkdepim/
%{_kf5_cmakedir}/KF5LibkdepimAkonadi/
%{_kf5_cmakedir}/MailTransportDBusService/
%{_kf5_includedir}/Libkdepim/
%{_kf5_includedir}/LibkdepimAkonadi/
%{_kf5_includedir}/libkdepim/
%{_kf5_includedir}/libkdepim_version.h
%{_kf5_includedir}/libkdepimakonadi/
%{_kf5_includedir}/libkdepimakonadi_version.h
%{_kf5_libdir}/libKF5Libkdepim.so
%{_kf5_libdir}/libKF5LibkdepimAkonadi.so
%{_kf5_mkspecsdir}/qt_Libkdepim.pri
%{_kf5_mkspecsdir}/qt_LibkdepimAkonadi.pri

%files
%license COPYING*
%{_kf5_debugdir}/libkdepim.categories
%{_kf5_debugdir}/libkdepim.renamecategories
%{_kf5_dbusinterfacesdir}/org.kde.addressbook.service.xml
%{_kf5_dbusinterfacesdir}/org.kde.mailtransport.service.xml
%{_kf5_plugindir}/designer/
%{_kf5_plugindir}/kcm_ldap.so
%{_kf5_servicesdir}/kcmldap.desktop
%{_kf5_sharedir}/kdepimwidgets/

%files -n libKF5Libkdepim5
%license COPYING*
%{_kf5_libdir}/libKF5Libkdepim.so.*

%files -n libKF5LibkdepimAkonadi5
%license COPYING*
%{_kf5_libdir}/libKF5LibkdepimAkonadi.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
