#
# spec file for package release-compare
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


Name:           release-compare
Summary:        Release Compare Script
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/release-compare
Version:        0.1
Release:        0
Source1:        COPYING
Source2:        obsgendiff
BuildArch:      noarch

%description
This package contains scripts to create changelog files relative
to last released result.

Note: you need to use a releasetarget definition in your OBS repository
      to get this working. And the release target needs to have published binaries.


%prep
%setup -q -c -T

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/build/ $RPM_BUILD_ROOT/%_defaultdocdir/%name
install -m 0755 %SOURCE2 $RPM_BUILD_ROOT/usr/lib/build/

%files
/usr/lib/build

%changelog
