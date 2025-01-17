#
# spec file for package python-whatthepatch
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-whatthepatch
Version:        0.0.6
Release:        0
License:        MIT
Summary:        A patch parsing and application library
Url:            https://github.com/cscorley/whatthepatch
Group:          Development/Languages/Python
Source:         https://github.com/cscorley/whatthepatch/archive/%{version}.tar.gz#/whatthepatch-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module nose}
BuildRequires:  ed
BuildRequires:  fdupes
BuildRequires:  patch
Requires:       ed
Requires:       patch
BuildArch:      noarch

%python_subpackages

%description
A patch parsing and application library.

%prep
%setup -q -n whatthepatch-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m nose --with-doctest --doctest-extension=rst

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
