#
# spec file for package python-csvkit
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
%define binaries csvclean csvcut csvformat csvgrep csvjoin csvjson csvlook csvpy csvsort csvsql csvstack csvstat in2csv sql2csv
%define         skip_python2 1
Name:           python-csvkit
Version:        1.0.5
Release:        0
Summary:        A library of utilities for working with CSV
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wireservice/csvkit
Source:         https://files.pythonhosted.org/packages/source/c/csvkit/csvkit-%{version}.tar.gz
BuildRequires:  %{python_module SQLAlchemy >= 0.9.3}
BuildRequires:  %{python_module Sphinx >= 1.0.7}
BuildRequires:  %{python_module aenum}
BuildRequires:  %{python_module agate >= 1.6.1}
BuildRequires:  %{python_module agate-dbf >= 0.2.0}
BuildRequires:  %{python_module agate-excel >= 0.2.2}
BuildRequires:  %{python_module agate-sql >= 0.5.3}
BuildRequires:  %{python_module dbf >= 0.9.3}
BuildRequires:  %{python_module et_xmlfile}
BuildRequires:  %{python_module jdcal}
BuildRequires:  %{python_module openpyxl >= 2.2.0.b1}
BuildRequires:  %{python_module python-dateutil >= 2.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.6.1}
BuildRequires:  %{python_module xlrd >= 0.9.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
CSVkit is a library of utilities for working with CSV. It is inspired
by pdftk, gdal and the original csvcut utility by Joe Germuska and
Aaron Bycoffe.

%prep
%setup -q -n csvkit-%{version}
# find and remove unneeded shebangs
find csvkit -name "*.py" | xargs sed -i '1 {/^#!/ d}'

%build
%python_build

%install
%python_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec -m unittest discover -s tests/ -v

%post
for b in %{binaries}; do
  %python_install_alternative $b
done

%postun
for b in %{binaries}; do
  %python_uninstall_alternative $b
done

%files %{python_files}
%license COPYING
%doc AUTHORS.rst CHANGELOG.rst README.rst
%python_alternative %{_bindir}/csvclean
%python_alternative %{_bindir}/csvcut
%python_alternative %{_bindir}/csvformat
%python_alternative %{_bindir}/csvgrep
%python_alternative %{_bindir}/csvjoin
%python_alternative %{_bindir}/csvjson
%python_alternative %{_bindir}/csvlook
%python_alternative %{_bindir}/csvpy
%python_alternative %{_bindir}/csvsort
%python_alternative %{_bindir}/csvsql
%python_alternative %{_bindir}/csvstack
%python_alternative %{_bindir}/csvstat
%python_alternative %{_bindir}/in2csv
%python_alternative %{_bindir}/sql2csv
%{python_sitelib}/csvkit-%{version}-py*.egg-info
%{python_sitelib}/csvkit/

%changelog
