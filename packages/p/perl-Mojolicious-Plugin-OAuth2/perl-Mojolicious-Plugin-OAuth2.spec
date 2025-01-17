#
# spec file for package perl-Mojolicious-Plugin-OAuth2
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


Name:           perl-Mojolicious-Plugin-OAuth2
Version:        1.58
Release:        0
%define cpan_name Mojolicious-Plugin-OAuth2
Summary:        Auth against OAuth2 APIs
License:        Artistic-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Socket::SSL) >= 1.94
BuildRequires:  perl(Mojolicious) >= 7.53
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(IO::Socket::SSL) >= 1.94
Requires:       perl(Mojolicious) >= 7.53
%{perl_requires}

%description
This Mojolicious plugin allows you to easily authenticate against a at
http://oauth.net provider. It includes configurations for a few popular
providers, but you can add your own easily as well.

Note that OAuth2 requires https, so you need to have the optional
Mojolicious dependency required to support it. Run the command below to
check if IO::Socket::SSL is installed.

   $ mojo version

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README README.md

%changelog
