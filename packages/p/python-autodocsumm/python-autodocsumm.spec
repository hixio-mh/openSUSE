#
# spec file for package python-autodocsumm
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-autodocsumm
Version:        0.1.13
Release:        0
Summary:        Extended sphinx autodoc including automatic autosummaries
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/Chilipp/autodocsumm
Source:         https://github.com/Chilipp/autodocsumm/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sphinx-testing}
# /SECTION
%python_subpackages

%description
Extended sphinx autodoc including automatic autosummaries

%prep
%setup -q -n autodocsumm-%{version}

%build
%python_build

%check
%pytest

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
