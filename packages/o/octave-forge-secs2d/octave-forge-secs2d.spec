#
# spec file for package octave-forge-secs2d
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define octpkg  secs2d
Name:           octave-forge-%{octpkg}
Version:        0.0.8
Release:        0
Summary:        SEmi Conductor Simulator in 2D for Octave
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM secs2d-octave-4.patch -- https://savannah.gnu.org/bugs/?44803
Patch1:         secs2d-octave-4.patch
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  octave-devel
Requires:       octave-cli >= 2.9.17

%description
A Drift-Diffusion simulator for 2D semiconductor devices.
This is part of the Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%patch1 -p0 -d %{octpkg}-%{version}
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
%defattr(-,root,root)
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
