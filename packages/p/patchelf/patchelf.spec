#
# spec file for package patchelf
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


Name:           patchelf
Version:        0.10
Release:        0
Summary:        A utility for patching ELF binaries
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://nixos.org/patchelf.html
Source:         https://nixos.org/releases/patchelf/patchelf-%{version}/patchelf-%{version}.tar.bz2
BuildRequires:  gcc-c++

%description
PatchELF is a simple utility for modifing existing ELF executables and
libraries.  It can change the dynamic loader ("ELF interpreter") of
executables and change the RPATH of executables and libraries.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
rm %{buildroot}%{_datadir}/doc/patchelf/README

%files
%doc README
%license COPYING
%{_bindir}/patchelf
%{_mandir}/man1/patchelf.1%{?ext_man}

%changelog
