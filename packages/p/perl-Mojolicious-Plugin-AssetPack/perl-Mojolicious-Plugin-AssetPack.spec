#
# spec file for package perl-Mojolicious-Plugin-AssetPack
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


Name:           perl-Mojolicious-Plugin-AssetPack
Version:        2.08
Release:        0
%define cpan_name Mojolicious-Plugin-AssetPack
Summary:        Compress and convert css, less, sass, javascript and coffeescript files
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which) >= 1.21
BuildRequires:  perl(IPC::Run3) >= 0.048
BuildRequires:  perl(Mojolicious) >= 7.17
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(File::Which) >= 1.21
Requires:       perl(IPC::Run3) >= 0.048
Requires:       perl(Mojolicious) >= 7.17
%{perl_requires}

%description
Mojolicious::Plugin::AssetPack is Mojolicious plugin for processing static
assets. The idea is that JavaScript and CSS files should be served as one
minified file to save bandwidth and roundtrip time to the server.

Note that the main author have moved on to using
Mojolicious::Plugin::Webpack instead, which uses https://webpack.js.org/
under the hood, but is just as convenient to use as this plugin. It is very
easy to try out Mojolicious::Plugin::Webpack, since it will detect your
AssetPack based project automatically, and migrate them over to webpack
once the plugin is loaded.

There are many external tools for doing this, but integrating them with
Mojolicious can be a struggle: You want to serve the source files directly
while developing, but a minified version in production. This assetpack
plugin will handle all of that automatically for you.

Your application creates and refers to an asset by its topic (virtual asset
name). The process of building actual assets from their components is
delegated to "pipe objects". Please see
Mojolicious::Plugin::AssetPack::Guides::Tutorial/Pipes for a complete list.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes examples README.md

%changelog
