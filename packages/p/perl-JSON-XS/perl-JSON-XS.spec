#
# spec file for package perl-JSON-XS
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-JSON-XS
Version:        4.02
Release:        0
%define cpan_name JSON-XS
Summary:        JSON serialising/deserialising, done correctly and fast
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
#Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{cpan_name}-4.01.tar.gz
Source0:        JSON-XS-4.02.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(common::sense)
Requires:       perl(Types::Serialiser)
Requires:       perl(common::sense)
%{perl_requires}

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be _correct_ and its secondary goal is to be _fast_. To
reach the latter goal it was written in C.

See MAPPING, below, on how JSON::XS maps perl values to JSON values and
vice versa.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license COPYING

%changelog
