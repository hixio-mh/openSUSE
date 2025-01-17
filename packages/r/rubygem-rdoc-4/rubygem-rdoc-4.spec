#
# spec file for package rubygem-rdoc-4
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

Name:           rubygem-rdoc-4
Version:        4.3.0
Release:        0
%define mod_name rdoc
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 1.9.3}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  update-alternatives
Url:            http://docs.seattlerb.org/rdoc
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        RDoc produces HTML and command-line documentation for Ruby projects
License:        Ruby
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
RDoc produces HTML and command-line documentation for Ruby projects.  RDoc
includes the +rdoc+ and +ri+ tools for generating and displaying documentation
from the command-line.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="History.rdoc LEGAL.rdoc LICENSE.rdoc README.rdoc" \
  -f

%gem_packages

%changelog
