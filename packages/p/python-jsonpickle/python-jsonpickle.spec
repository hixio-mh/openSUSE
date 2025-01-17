#
# spec file for package python-jsonpickle
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
%define modname jsonpickle
%bcond_without python2
Name:           python-jsonpickle
Version:        1.3
Release:        0
Summary:        Python library for serializing any arbitrary object graph into JSON
License:        BSD-3-Clause
URL:            https://github.com/jsonpickle/jsonpickle
Source:         https://files.pythonhosted.org/packages/source/j/jsonpickle/jsonpickle-%{version}.tar.gz
# PATCH-FIX-UPSTREAM PR292-Python38.patch gh#jsonpickle/jsonpickle#281 mcepl@suse.com
# Fix Python 3.8 incompatibilities
Patch01:        PR292-Python38.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-simplejson
Suggests:       python-demjson
Suggests:       python-ujson
Suggests:       python-yajl
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{pythons}
# /SECTION
%if %{with python2}
BuildRequires:  python-enum34
%endif
%ifpython2
Suggests:       python-feedparser
Suggests:       python-jsonlib
%endif
%python_subpackages

%description
Python library for serializing any arbitrary object graph into JSON.
It can take almost any Python object and turn the object into JSON.
Additionally, it can reconstitute the object back into Python.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst docs/source/changelog.rst
%license COPYING
%{python_sitelib}/*

%changelog
