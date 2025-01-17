#
# spec file for package fnotifystat
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


Name:           fnotifystat
Version:        0.02.05
Release:        0
Summary:        File activity monitoring tool
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://kernel.ubuntu.com/~cking/fnotifystat/
Source:         https://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.gz

%description
Fnotifystat periodically dumps out the activity on files in the system. It can
be used to identify rogue file activity and discover which processes are
performing open/close/read/write operations on the files.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Benchmark
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (fnotifystat and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%make_build

%install
%make_install

%files
%license COPYING
%{_sbindir}/fnotifystat
%{_mandir}/man8/fnotifystat.8%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
