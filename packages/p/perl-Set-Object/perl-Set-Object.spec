#
# spec file for package perl-Set-Object
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Set-Object
Version:        1.40
Release:        0
%define cpan_name Set-Object
Summary:        Set of objects and strings
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
Recommends:     perl(Moose)
Recommends:     perl(Test::LeakTrace)
%{perl_requires}

%description
This modules implements a set of objects, that is, an unordered collection
of objects without duplication.

The term _objects_ is applied loosely - for the sake of Set::Object,
anything that is a reference is considered an object.

Set::Object 1.09 and later includes support for inserting scalars
(including the empty string, but excluding 'undef') as well as objects.
This can be thought of as (and is currently implemented as) a degenerate
hash that only has keys and no values. Unlike objects placed into a
Set::Object, scalars that are inserted will be flattened into strings, so
will lose any magic (eg, tie) or other special bits that they went in with;
only strings come out.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc README
%license LICENSE

%changelog
