#
# spec file for package python-python-crontab
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
Name:           python-python-crontab
Version:        2.4.0
Release:        0
Summary:        Python Crontab API
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://gitlab.com/doctormo/python-crontab/
# https://gitlab.com/doctormo/python-crontab/-/issues/69
Source:         https://gitlab.com/doctormo/python-crontab/-/archive/v%{version}/python-crontab-v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
Recommends:     cronie
Recommends:     python-cron-descriptor
Recommends:     python-croniter
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cron-descriptor}
BuildRequires:  %{python_module croniter}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  cronie
BuildRequires:  python2-devel
BuildRequires:  python3-testsuite
# /SECTION
%python_subpackages

%description
Crontab module for reading and writing crontab files and
accessing the system cron automatically using an API.

%prep
%setup -q -n python-crontab-v%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc README.rst
%license COPYING AUTHORS
%{python_sitelib}/*

%changelog
