#
# spec file for package libevdev
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


%define sonum	2
Name:           libevdev
Version:        1.9.0
Release:        0
Summary:        A wrapper library for evdev devices
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://xorg.freedesktop.org/
#Git-Web:	http://cgit.freedesktop.org/libevdev
#Git-Clone:	git://anongit.freedesktop.org/libevdev
Source0:        http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz
Source1:        http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
Patch0:         n_buildfix_for_opensuse_12_2.patch
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python

%description
Library for handling evdev kernel devices. It abstracts the ioctls
through type-safe interfaces and provides functions to change
the appearance of the device.

%package devel
Summary:        Development files for libevdev library
Group:          Development/Libraries/C and C++
Requires:       libevdev%{sonum} = %{version}

%description devel
Library for handling evdev kernel devices. It abstracts the ioctls
through type-safe interfaces and provides functions to change
the appearance of the device.

Development files for libevdev library

%package -n libevdev%{sonum}
Summary:        Library for handling evdev kernel devices
Group:          System/Libraries
Suggests:       %{name}-tools

%description -n libevdev%{sonum}
Library for handling evdev kernel devices. It abstracts the ioctls
through type-safe interfaces and provides functions to change
the appearance of the device.

%package tools
Summary:        Library for handling evdev kernel devices
Group:          System/Base

%description tools
Library for handling evdev kernel devices. It abstracts the ioctls
through type-safe interfaces and provides functions to change
the appearance of the device.

Aditional utilities for libevdev library

%prep
%setup -q
%if 0%{?suse_version} < 1230
%patch0 -p1
%endif

%build
%configure \
  --disable-static \
  --disable-gcov
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libevdev%{sonum} -p /sbin/ldconfig
%postun -n libevdev%{sonum} -p /sbin/ldconfig

%files -n libevdev%{sonum}
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%license COPYING
%{_libdir}/%{name}.so
%{_includedir}/%{name}-1.0/
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/libevdev.*

%files tools
%license COPYING
%{_bindir}/mouse-dpi-tool
%{_bindir}/libevdev-tweak-device
%{_bindir}/touchpad-edge-detector

%changelog
