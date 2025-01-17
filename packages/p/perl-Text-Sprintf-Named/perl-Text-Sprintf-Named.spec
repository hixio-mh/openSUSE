#
# spec file for package perl-Text-Sprintf-Named
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


Name:           perl-Text-Sprintf-Named
Version:        0.0403
Release:        0
%define cpan_name Text-Sprintf-Named
Summary:        Sprintf-Like Function with Named Conversions
License:        MIT
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Sprintf-Named/
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.280000
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(parent)
Requires:       perl(parent)
%{perl_requires}

%description
Text::Sprintf::Named provides a sprintf equivalent with named conversions.
Named conversions are sprintf field specifiers (like '"%s"' or '"%4d'")
only they are associated with the key of an associative array of
parameters. So for example '"%(name)s"' will emit the ''name'' parameter as
a string, and '"%(num)4d"' will emit the ''num'' parameter as a variable
with a width of 4.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README TODO
%license LICENSE

%changelog
