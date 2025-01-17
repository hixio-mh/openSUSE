#
# spec file for package python-neovim
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


%define modname pynvim
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?rhel} >= 7
%define python_module() python34-%{**}
%endif
Name:           python-neovim
Version:        0.4.1
Release:        0
Summary:        Python client to Neovim
License:        Apache-2.0
Group:          Productivity/Text/Editors
URL:            https://github.com/neovim/pynvim
Source:         https://github.com/neovim/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM setup_version.patch gh#neovim/pynvim#431 mcepl@suse.com
# Upstream setup.py has incorrect version.
Patch0:         setup_version.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       neovim >= 0.1.6
Requires:       python-greenlet
Requires:       python-msgpack-python
Provides:       python-nvim
BuildArch:      noarch
%python_subpackages

%description
Library for scripting Nvim processes through its msgpack-rpc API.

%prep
%autosetup -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/neovim/
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-*.egg-info/

%changelog
