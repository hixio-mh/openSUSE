#
# spec file for package i3blocks
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


Name:           i3blocks
Version:        1.4
Release:        0
Summary:        Alternative status bar for i3
License:        GPL-3.0-or-later
Group:          System/Monitoring
URL:            https://github.com/vivien/i3blocks
Source:         https://github.com/vivien/i3blocks/releases/download/%{version}/i3blocks-%{version}.tar.gz
BuildRequires:  pandoc
Requires:       acpi
Requires:       alsa-utils
Requires:       i3
Requires:       iproute2
Requires:       sysstat
Requires:       xclip

%description
i3blocks is a flexible status line for the i3 window manager. It handles
clicks, signals and language-agnostic user scripts.

The content of each block (e.g. time, battery status, network state, ...) is
the output of a command provided by the user. Blocks are updated on click, at a
given interval of time or on a given signal, also specified by the user.

It follows the i3bar protocol, providing customization such as text
alignment, urgency and color.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir}

%files
%doc CHANGELOG.md README.md
%license COPYING
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_mandir}/man?/%{name}.?%{ext_man}

%changelog
