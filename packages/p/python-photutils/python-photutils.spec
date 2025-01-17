#
# spec file for package python-photutils
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-photutils
Version:        0.7.2
Release:        0
Summary:        An Astropy package for photometry
License:        BSD-3-Clause
Group:          Productivity/Scientific/Astronomy
URL:            https://github.com/astropy/photutils
Source:         https://files.pythonhosted.org/packages/source/p/photutils/photutils-%{version}.tar.gz
Patch0:         https://github.com/astropy/photutils/pull/1014.patch#/0001-aperture-mask-test-assert-almost-equal.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.13}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astropy >= 2.0
Requires:       python-numpy >= 1.13
Requires:       python-scipy >= 0.19
Recommends:     python-matplotlib >= 2.2
Recommends:     python-scikit-image >= 0.14.2
Recommends:     python-scikit-learn >= 0.19
Recommends:     python-gwcs >= 0.11
# SECTION test requirements
BuildRequires:  %{python_module astropy >= 2.0}
BuildRequires:  %{python_module astropy-helpers >= 2.0}
BuildRequires:  %{python_module pytest-astropy >= 0.7}
BuildRequires:  %{python_module scikit-image >= 0.14.2}
BuildRequires:  %{python_module scikit-learn >= 0.19}
BuildRequires:  python3-dbm
# /SECTION
%python_subpackages

%description
Photutils is an affiliated package of Astropy to provide tools for detecting
and performing photometry of astronomical sources.

%prep
%setup -q -n photutils-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
rm -rf  %{buildroot}%{python_sitearch}/photutils/*.c
rm -rf  %{buildroot}%{python_sitearch}/photutils/geometry/*.c
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# do not import source dir without extensions
cd .. 
# Use astropy test suite logic. Calling pytest directly would require
# duplicate in-place building of extensions.
%{python_expand export PYTHONPATH="%{buildroot}%{$python_sitearch}"
$python -B -c "import photutils, sys; sys.exit(photutils.test(args=\"-v\"))"
}

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst licenses
%{python_sitearch}/photutils
%{python_sitearch}/photutils-%{version}-py*.egg-info

%changelog
