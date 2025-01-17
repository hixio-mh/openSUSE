#
# spec file for package perl-WebService-MusicBrainz
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


Name:           perl-WebService-MusicBrainz
Version:        1.0.4
Release:        0
%define cpan_name WebService-MusicBrainz
Summary:        Web service API to MusicBrainz database
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/%{cpan_name}/
Source0:        http://www.cpan.org/authors/id/B/BF/BFAIST/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
%{perl_requires}
Requires:       perl(Mojolicious)

%description
An API to search the musicbrainz.org database.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc README.md

%changelog
