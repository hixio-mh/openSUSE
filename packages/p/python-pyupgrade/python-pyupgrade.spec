#
# spec file for package python-pyupgrade
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pyupgrade
Version:        2.6.2
Release:        0
License:        MIT
Summary:        A tool to automatically upgrade syntax for newer versions
Url:            https://github.com/asottile/pyupgrade
Group:          Development/Languages/Python
# pypi tarball does not include tests, use github instead. PR for inclusion: https://github.com/asottile/pyupgrade/pull/326
Source:         https://github.com/asottile/pyupgrade/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source:         https://files.pythonhosted.org/packages/source/p/pyupgrade/pyupgrade-%%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module tokenize-rt >= 3.2.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-tokenize-rt >= 3.2.0
BuildArch:      noarch

%python_subpackages

%description
A tool to automatically upgrade syntax for newer versions.

%prep
%setup -q -n pyupgrade-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/pyupgrade
%{python_sitelib}/*

%changelog
