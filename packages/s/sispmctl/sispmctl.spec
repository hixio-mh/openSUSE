#
# spec file for package sispmctl
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


%define libname libsispmctl0
Name:           sispmctl
Version:        4.6
Release:        0
Summary:        SIS-PM Control for Linux
License:        GPL-2.0-only
URL:            https://sourceforge.net/projects/sispmctl/
Source0:        sispmctl-%{version}.tar.gz
Patch0:         sispmctl-fix-udev-group.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(udev)

%description
This projects adds support control for the GEMBIRD Silver Shield PM device to linux.

%package -n %{libname}
Summary:        Libraries for sispmctl

%description -n %{libname}
Libraries for the GEMBIRD Silver Shield PM device.

%package devel
Summary:        Development files for sispmctl
Requires:       %{libname} = %{version}

%description devel
Development files for the GEMBIRD Silver Shield PM device.

%prep
%setup -q
%autopatch -p1

%build
./autogen.sh
%configure \
  --disable-static \
  --enable-webless
%make_build

%install
%make_install
# Remove static libs
find %{buildroot} -type f -name "*.la" -delete -print

install -Dm 0644 examples/60-sispmctl.rules %{buildroot}%{_udevrulesdir}/60-sispmctl.rules

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_mandir}/man1/sispmctl.1%{?ext_man}
%license COPYING
%{_bindir}/sispmctl
%dir %{_udevrulesdir}
%{_udevrulesdir}/60-sispmctl.rules

%files -n %{libname}
%{_libdir}/libsispmctl.so.*

%files devel
%{_libdir}/libsispmctl.so

%changelog
