#
# spec file for package gnome-nibbles
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


Name:           gnome-nibbles
Version:        3.36.1
Release:        0
Summary:        Worm Game for GNOME
License:        GPL-3.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://live.gnome.org/Lightsoff
Source0:        https://download.gnome.org/sources/gnome-nibbles/3.36/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  meson >= 0.43.1
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(clutter-1.0) >= 1.22.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.4.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gsound) >= 1.0.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18.0
BuildRequires:  pkgconfig(libgnome-games-support-1)

%description
Nibbles is a worm game for GNOME. The player controls a 2D worm while
trying to get food. Getting food gives points, but hitting anything
causes a loss of points. When all points are lost, the player loses.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}/%{_datadir}
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.gnome.Nibbles.appdata.xml
%{_datadir}/applications/org.gnome.Nibbles.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.nibbles.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Nibbles*.*
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}.lang

%changelog
