#
# spec file for package apache2-mod_auth_openidc
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


%define apxs %{_sbindir}/apxs2
%define apache_libexecdir %(%{apxs} -q LIBEXECDIR)
Name:           apache2-mod_auth_openidc
Version:        2.4.2.1
Release:        0
Summary:        Apache2.x module for an OpenID Connect enabled Identity Provider
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://github.com/zmartzone/mod_auth_openidc/
Source:         https://github.com/zmartzone/mod_auth_openidc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  autoconf
BuildRequires:  automake
%if 0%{?is_opensuse} > 0
BuildRequires:  hiredis-devel
%endif
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cjose) >= 0.4.1
BuildRequires:  pkgconfig(jansson) >= 2.0
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(openssl) >= 1.0.1
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}

%description
This module enables an Apache 2.x web server to operate as an OpenID Connect Relying Party and/or OAuth 2.0 Resource Server.

%prep
%setup -q -n mod_auth_openidc-%{version}

%build
./autogen.sh
%configure \
%if 0%{?is_opensuse} > 0
  %{?_with_hiredis}    \
%else
  %{?_without_hiredis} \
%endif

make %{?_smp_mflags}

%install
install -D -m0755 src/.libs/mod_auth_openidc.so %{buildroot}%{apache_libexecdir}/mod_auth_openidc.so

%files
%dir %{apache_libexecdir}
%{apache_libexecdir}/mod_auth_openidc.so

%changelog
