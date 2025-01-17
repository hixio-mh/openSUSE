#
# spec file for package wgetpaste
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wgetpaste
Version:        2.28
Release:        0
Summary:        Command-line interface to various pastebins
License:        SUSE-Public-Domain
Group:          Productivity/Other
Url:            http://wgetpaste.zlin.dk/
Source0:        http://wgetpaste.zlin.dk/%{name}-%{version}.tar.bz2
Source1:        services.conf
Requires:       bash
Requires:       coreutils
Requires:       wget
Recommends:     xclip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Command-line interface to communicate with various pastebin services.

%prep
%setup -q

%build
# do nothing

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}.d/services.conf
install -D -m 0644 _%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/%{name}.d/
%dir %{_datadir}/zsh/site-functions/
%dir %{_datadir}/zsh/
%{_datadir}/zsh/site-functions/_%{name}
%config %{_sysconfdir}/%{name}.d/services.conf
%{_bindir}/%{name}

%changelog
