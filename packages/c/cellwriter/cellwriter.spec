#
# spec file for package cellwriter
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


Name:           cellwriter
Version:        1.3.6
Release:        0
Summary:        Character-based handwriting input panel
License:        GPL-2.0+
Group:          System/GUI/GNOME
Url:            http://risujin.org/cellwriter/
Source0:        https://github.com/risujin/cellwriter/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)

%description
CellWriter is a grid-entry natural handwriting input panel. As you
write characters into the cells, your writing is instantly recognized
at the character level. When you press Enter on the panel, the input
you entered is sent to the currently focused application as if typed on
the keyboard.

%prep
%setup -q

%build
autoreconf -fi
%configure \
	 --without-gnome
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -i -G "Handwriting Input Panel" cellwriter Utility Accessibility

%files
%doc README NEWS COPYING AUTHORS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/scalable/apps/cellwriter.svg
%{_datadir}/applications/*

%changelog
