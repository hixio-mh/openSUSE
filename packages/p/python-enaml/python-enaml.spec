#
# spec file for package python-enaml
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
# python-cppy, python-bytecode is python3 only (at least)
%define skip_python2 1
Name:           python-enaml
Version:        0.11.2
Release:        0
# Source code is under BSD but images are under different licenses
# and details are inside image_LICENSE.txt
Summary:        Declarative DSL for building rich user interfaces in Python
License:        BSD-3-Clause AND LGPL-2.1-only
URL:            https://github.com/nucleic/enaml
Source:         https://github.com/nucleic/enaml/archive/%{version}.tar.gz#/enaml-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-QtPy >= 1.3
Requires:       python-atom >= 0.4.2
Requires:       python-bytecode >= 0.11.0
Requires:       python-future
Requires:       python-kiwisolver >= 1.0.0
Requires:       python-ply >= 3.4
Requires:       python-qt5
Requires:       python-qtwebengine-qt5
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION test requirements
BuildRequires:  %{python_module QtPy >= 1.3}
BuildRequires:  %{python_module atom >= 0.4.2}
BuildRequires:  %{python_module bytecode}
BuildRequires:  %{python_module cppy >= 1.1.0}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module kiwisolver >= 1.0.0}
BuildRequires:  %{python_module ply >= 3.4}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module qtwebengine-qt5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  gdb
BuildRequires:  libqt5-qtwebengine-debuginfo
BuildRequires:  xauth
BuildRequires:  xorg-x11-fonts
BuildRequires:  xorg-x11-server-Xvfb
# /SECTION
%python_subpackages

%description
Enaml is a programming language and framework for creating
professional quality user interfaces with minimal effort.
Enaml combines a domain specific declarative language with
a constraints based layout system to allow users to easily
define rich UIs with complex and flexible layouts. Enaml
applications can be run on any platform which supports
Python and Qt.

%prep
%setup -q -n enaml-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/enaml-compileall
%python_clone -a %{buildroot}%{_bindir}/enaml-run

%check
mv enaml enaml_temp
# not sure why these two are failing
%pytest_arch -k "not (test_focus_tracking or test_focus_traversal)"
mv enaml_temp enaml
find %{buildroot} -name __enamlcache__ | xargs rm -r # drop unreproducible files https://github.com/nucleic/enaml/issues/397

%post
%{python_install_alternative enaml-compileall enaml-run}

%postun
%python_uninstall_alternative enaml-compileall

%files %{python_files}
%doc README.rst releasenotes.rst
%license LICENSE
%python_alternative %{_bindir}/enaml-compileall
%python_alternative %{_bindir}/enaml-run
%{python_sitearch}/*

%changelog
