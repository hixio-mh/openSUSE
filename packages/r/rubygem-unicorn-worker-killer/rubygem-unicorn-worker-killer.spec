#
# spec file for package rubygem-unicorn-worker-killer
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-unicorn-worker-killer
Version:        0.4.4
Release:        0
%define mod_name unicorn-worker-killer
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/kzk/unicorn-worker-killer
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Kill unicorn workers by memory and request counts
License:        Ruby OR (GPL-2.0 OR GPL-3.0)
Group:          Development/Languages/Ruby

%description
Kill unicorn workers by memory and request counts.

%prep

%build

%install
%gem_install \
  --doc-files="ChangeLog LICENSE README.md" \
  -f

%gem_packages

%changelog
