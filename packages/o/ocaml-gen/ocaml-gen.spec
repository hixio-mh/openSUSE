#
# spec file for package ocaml-gen
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


Name:           ocaml-gen
Version:        0.5.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Simple, efficient iterators for OCaml
License:        BSD-2-Clause
Group:          Development/Languages/OCaml
URL:            https://github.com/c-cube/gen
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20191101
BuildRequires:  ocamlfind(bytes)
BuildRequires:  ocamlfind(qcheck)
BuildRequires:  ocamlfind(qtest)
BuildRequires:  ocamlfind(oUnit)

%description
Iterators for OCaml, both restartable and consumable.
The implementation keeps a good balance between simplicity and performance.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -p1

%build
dune_release_pkgs='gen'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%doc README.md

%files devel -f %{name}.files.devel

%changelog
