#
# spec file for package rubygem-rubyforge
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-rubyforge
Version:        2.0.4
Release:        0
%define mod_name rubyforge
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
Url:            http://codeforpeople.rubyforge.org/rubyforge/
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
# MANUAL
Patch0:         raise-on-auth-fail.patch
# /MANUAL
Summary:        A script which automates a limited set of rubyforge operations
License:        GPL-2.0+ or Ruby
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
A script which automates a limited set of rubyforge operations.
* Run 'rubyforge help' for complete usage.
* Setup: For first time users AND upgrades to 0.4.0:
* rubyforge setup (deletes your username and password, so run sparingly!)
* edit ~/.rubyforge/user-config.yml
* rubyforge config
* For all rubyforge upgrades, run 'rubyforge config' to ensure you have
latest.

%prep
%gem_unpack
%patch0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="History.txt README.txt" \
  -f

%gem_packages

%changelog
