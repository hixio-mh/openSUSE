#
# spec file for package python-fudge
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
Name:           python-fudge
Version:        1.1.1
Release:        0
Summary:        Module for replacing real objects with fakes (mocks, stubs, etc) while testing
License:        MIT
Group:          Development/Languages/Python
URL:            http://farmdev.com/projects/fudge/
Source:         https://files.pythonhosted.org/packages/source/f/fudge/fudge-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM remove_nose.patch gh#fudge-py/fudge#11 mcepl@suse.com
# Remove the need of using nose and port to py3k
Patch0:         remove_nose.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Complete documentation is available at http://farmdev.com/projects/fudge/

Fudge is a Python module for using fake objects (mocks and stubs) to test real ones.

In readable Python code, you declare what methods are available on your fake and
how they should be called. Then you inject that into your application and start
testing. This declarative approach means you don't have to record and playback
actions and you don't have to inspect your fakes after running code. If the fake
object was used incorrectly then you'll see an informative exception message
with a traceback that points to the culprit.

%prep
%setup -q -n fudge-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#fudge-py/fudge#11
# Still unported tests
%pytest -k 'not (test_decorator_on_def or test_expectations_are_always_cleared or test_expectations_are_always_cleared or test_global_clear_expectations)'

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
