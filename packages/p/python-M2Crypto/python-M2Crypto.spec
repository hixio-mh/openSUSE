#
# spec file for package python-M2Crypto
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-M2Crypto
Version:        0.36.0
Release:        0
Summary:        Crypto and SSL toolkit for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://gitlab.com/m2crypto/m2crypto
Source:         https://files.pythonhosted.org/packages/source/M/M2Crypto/M2Crypto-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  python-rpm-macros
Requires:       python-typing
Requires:       python-xml
# hpj: SLES 12 and Leap 42.1 need swig3 to build this package
%if 0%{?sle_version} == 120100
BuildRequires:  swig3
%else
BuildRequires:  swig
%endif
%ifpython2
Provides:       %{oldpython}-m2crypto = %{version}
Obsoletes:      %{oldpython}-m2crypto < %{version}
%endif
%python_subpackages

%description
M2Crypto is a crypto and SSL toolkit for Python featuring the following:

RSA, DSA, DH, HMACs, message digests, symmetric ciphers (including
AES). SSL functionality to implement clients and servers. HTTPS
extensions to Python's httplib, urllib, and xmlrpclib. Unforgeable
HMAC'ing AuthCookies for web session management. FTP/TLS client and
server. S/MIME. ZServerSSL: A HTTPS server for Zope. ZSmime: An S/MIME
messenger for Zope.

%package -n %{name}-doc
Summary:        Documentation for the Crypto and SSL toolkit for Python
Group:          Development/Libraries/Python
BuildArch:      noarch

%description -n %{name}-doc
M2Crypto is a crypto and SSL toolkit for Python featuring the following:

RSA, DSA, DH, HMACs, message digests, symmetric ciphers (including
AES). SSL functionality to implement clients and servers. HTTPS
extensions to Python's httplib, urllib, and xmlrpclib. Unforgeable
HMAC'ing AuthCookies for web session management. FTP/TLS client and
server. S/MIME. ZServerSSL: A HTTPS server for Zope. ZSmime: An S/MIME
messenger for Zope.

Documentation for the Crypto and SSL toolkit for Python

%prep
%setup -q -n M2Crypto-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES LICENCE README.rst
%{python_sitearch}/*

%files -n %{name}-doc
%doc doc/*.rst

%changelog
