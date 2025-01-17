#
# spec file for package i3lock
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2014 B1 Systems GmbH, Vohburg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
Name:           i3lock
Version:        2.12
Release:        0
Summary:        Screen Locker for the i3 Window Manager
License:        BSD-3-Clause
URL:            https://i3wm.org/i3lock/
Source:         https://i3wm.org/i3lock/%{name}-%{version}.tar.bz2
# borrowed from gnome-icon-theme
Source2:        i3lock-icon.png
Source3:        xlock.sh
# PATCH-FIX-UPSTREAM 0001-unlock_indicator.c-fix-build-failure-against-gcc-10.patch gh#i3/i3lock#259
Patch0:         0001-unlock_indicator.c-fix-build-failure-against-gcc-10.patch
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(xkbcommon-x11)

%description
i3lock is a simple screen locker like slock. After starting it, you will see a
white screen (you can configure the color/an image). You can return to your
screen by entering your password.

%package xlock-compat
Summary:        Xlock-compatibility script which calls i3lock
Requires:       ImageMagick
Requires:       xdpyinfo
Conflicts:      xlockmore

%description xlock-compat
This package provides a script %{_bindir}/xlock which calls i3lock to lock your screen.
This is handy for hard-coded screen-saver invocations e.g. in XFCE4, so you can use
i3lock instead of xlock with them.

%prep
%autosetup -p 1

%build
%configure
export CFLAGS="%{optflags}"
%make_build

%install
%make_install

install -D -m0644 %{name}.1 "%{buildroot}%{_mandir}/man1/%{name}.1"
install -D -m0644 %{SOURCE2} %{buildroot}%{_datadir}/i3lock-xlock-compat/i3lock-icon.png
install -m0755 %{SOURCE3} %{buildroot}/%{_bindir}/xlock

%files xlock-compat
%{_bindir}/xlock
%{_datadir}/%{name}-xlock-compat

%files
%license LICENSE
%doc CHANGELOG README.md
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
