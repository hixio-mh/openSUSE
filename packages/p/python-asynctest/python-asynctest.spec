#
# spec file for package python-asynctest
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-asynctest
Version:        0.13.0
Release:        0
Summary:        Enhancement for the unittest with features from asyncio libraries
License:        Apache-2.0
URL:            https://github.com/Martiusweb/asynctest/
Source:         https://files.pythonhosted.org/packages/source/a/asynctest/asynctest-%{version}.tar.gz
Patch0:         asynctest-skip-permstest.patch
Patch1:         py38.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package enhances the standard unittest package with features for
testing asyncio libraries.

%prep
%setup -q -n asynctest-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests failing with py3.8 https://github.com/Martiusweb/asynctest/issues/132
# test_basic - it is not supposed to be launched by pytest
%pytest -k 'not (test_basic or test_create_autospec_on_coroutine_and_using_assert_methods or test_awaited_from_autospec_mock or test_patch_coroutine_with_multiple_scopes or test_multiple_patches_on_coroutine or test_patch_coroutine_only_when_running)'

%files %{python_files}
%license LICENSE.md
%doc README.rst
%{python_sitelib}/*

%changelog
