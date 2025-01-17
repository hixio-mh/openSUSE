#
# spec file for package python
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_without python2
Name:           python-pytest4%{psuffix}
Version:        4.6.9
Release:        0
Summary:        Python testing tool with autodiscovery and detailed asserts
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pytest-dev/pytest
Source:         https://files.pythonhosted.org/packages/source/p/pytest/pytest-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 40.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-atomicwrites >= 1.0
Requires:       python-attrs >= 17.4.0
Requires:       python-importlib-metadata >= 0.12
Requires:       python-more-itertools >= 4.0.0
Requires:       python-packaging
Requires:       python-pluggy >= 0.12
Requires:       python-py >= 1.5.0
Requires:       python-setuptools
Requires:       python-six >= 1.10.0
Requires:       python-wcwidth
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      python-pytest
Provides:       python-pytest = %{version}-%{release}
Obsoletes:      python-pytest4-doc
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module importlib-metadata >= 0.12}
BuildRequires:  %{python_module pygments-pytest}
BuildRequires:  %{python_module pytest4 >= %{version}}
BuildRequires:  %{python_module setuptools_scm}
%if %{with python2}
BuildRequires:  python-funcsigs
BuildRequires:  python-mock
%endif
%endif
%ifpython2
Requires:       python-funcsigs
%endif
%if "%{python_flavor}" == "python2" || %{python3_version_nodots} < 36
Requires:       python-pathlib2 >= 2.2.0
%endif
%python_subpackages

%description
pytest is a cross-project Python testing tool. It provides:

* auto-discovery of test modules and functions,
* detailed info on failing assert statements (no need to remember
  self.assert* names),
* modular fixtures for managing small or parametrized long-lived test resources.
* multi-paradigm support: you can use py.test to run test suites based on
  unittest (or trial), nose,
* single-source compatibility to Python2.4 all the way up to Python3.3,
  PyPy-1.9 and Jython-2.5.1, and
* many external plugins.

%prep
%setup -q -n pytest-%{version}

%build
%python_build

%install
%if ! %{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/py.test
%python_clone -a %{buildroot}%{_bindir}/pytest

if [ -x %{buildroot}%{_bindir}/py.test-%{python2_bin_suffix} ]; then
    ln -s py.test-%{python2_bin_suffix} %{buildroot}%{_bindir}/py.test2
fi
if [ -x %{buildroot}%{_bindir}/py.test-%{python3_bin_suffix} ]; then
    ln -s py.test-%{python3_bin_suffix} %{buildroot}%{_bindir}/py.test3
fi

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if ! %{with test}
%post
%{python_install_alternative py.test} \
   --slave %{_bindir}/pytest pytest %{_bindir}/pytest-%{python_version}

%postun
%python_uninstall_alternative py.test

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/py.test
%python_alternative %{_bindir}/pytest
%python2_only %{_bindir}/py.test2
%python3_only %{_bindir}/py.test3
%{python_sitelib}/*
%endif

%changelog
