#
# spec file for package python-pytest-virtualenv
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-virtualenv
Version:        1.7.0
Release:        0
Summary:        Virtualenv fixture for pytest
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/manahl/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-virtualenv/pytest-virtualenv-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module path.py}
BuildRequires:  %{python_module pytest-fixture-config}
BuildRequires:  %{python_module pytest-shutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-path.py
Requires:       python-pytest-fixture-config
Requires:       python-pytest-shutil
Requires:       python-setuptools
Requires:       python-virtualenv
BuildArch:      noarch
%python_subpackages

%description
Create a Python virtual environment in your test that cleans up on
teardown. The fixture has utility methods to install packages and list
what's installed.

%prep
%setup -q -n pytest-virtualenv-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
