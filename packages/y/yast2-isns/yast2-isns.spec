#
# spec file for package yast2-isns
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-isns
Version:        4.2.0
Release:        0
Summary:        Configuration of isns
License:        GPL-2.0-only
Group:          System/YaST

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-testsuite
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
# Yast2::Systemd::Service
BuildRequires:  yast2 >= 4.1.3

# Yast2::Systemd::Service
Requires:       yast2 >= 4.1.3
Requires:       yast2-ruby-bindings >= 1.0.0

BuildArch:      noarch

%description
-

%prep
%setup -q

%check
%yast_check

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%doc %{yast_docdir}
%{yast_icondir}
%license COPYING

%changelog
