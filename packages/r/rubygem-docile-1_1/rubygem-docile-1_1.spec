#
# spec file for package rubygem-docile-1_1
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-docile-1_1
Version:        1.1.5
Release:        0
%define mod_name docile
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -1_1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 1.8.7}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://ms-ati.github.io/docile/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Ruby gem to treat Ruby objects as a domain-specific language
License:        MIT
Group:          Development/Languages/Ruby

%description
Docile turns any Ruby object into a DSL. Especially useful with the Builder
pattern.

%prep

%build

%install
%gem_install \
  --doc-files="HISTORY.md LICENSE README.md" \
  -f

%gem_packages

%changelog
