#
# spec file for package octave-forge-octclip
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


%define octpkg  octclip
Name:           octave-forge-%{octpkg}
Version:        1.0.8
Release:        0
Summary:        Octave clipping polygons tool
License:        GPL-3.0-or-later AND BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM octclip-openmp.patch -- Fix build with OpenMP
Patch0:         octclip-openmp.patch
# PATCH-FIX-UPSTREAM compile-with-gcc-9.patch
Patch1:         compile-with-gcc-9.patch
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  octave-devel
Requires:       octave-cli >= 2.9.7

%description
This package allows to do boolean operations with polygons using
the Greiner-Hormann algorithm.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
pushd %{octpkg}-%{version}
%patch0 -p1
%patch1 -p1
popd
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
