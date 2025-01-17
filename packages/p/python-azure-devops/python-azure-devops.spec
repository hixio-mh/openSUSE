#
# spec file for package python-azure-devops
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
Name:           python-azure-devops
Version:        6.0.0b2
Release:        0
License:        MIT
Summary:        Python wrapper around the Azure DevOps 5x APIs
Url:            https://github.com/Microsoft/vsts-python-api
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/azure-devops/azure-devops-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module msrest >= 0.6.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest >= 0.6.0
Provides:       python-vsts = %{version}
Obsoletes:      python-vsts < %{version}

BuildArch:      noarch

%python_subpackages

%description
Python wrapper around the Azure DevOps 5.x APIs

%prep
%setup -q -n azure-devops-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/azure/devops
%{python_sitelib}/azure_devops-*.egg-info

%changelog
