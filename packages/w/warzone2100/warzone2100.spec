#
# spec file for package warzone2100
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


Name:           warzone2100
Version:        3.2.3
Release:        0
Summary:        Innovative 3D real-time strategy
License:        GPL-2.0+ and CC-BY-SA-3.0 and CC0-1.0 and BSD-3-Clause and LGPL-2.1
Group:          Amusements/Games/Strategy/Real Time
Url:            http://wz2100.net/
Source:         http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source99:       %{name}.changes
# PATCH-FIX-UPSTREAM https://github.com/Warzone2100/warzone2100/pull/89
Patch2:         system-miniupnpc.patch
# PATCH-FIX-UPSTREAM https://github.com/Warzone2100/warzone2100/pull/98
Patch3:         reproducible.patch
BuildRequires:  asciidoc
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  libpng-devel
BuildRequires:  physfs-devel
BuildRequires:  pkg-config
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  zip
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew) >= 1.5.2
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(quesoglc)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(xrandr)
Requires:       %{name}-data = %{version}
Recommends:     %{name}-movies
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} <= 1220
BuildRequires:  libopenal1
%endif

%description
You command the forces of "The Project" in a battle to rebuild 
the world after mankind has almost been destroyed by nuclear 
missiles. 

The game offers campaign, multi-player and single-player skirmish 
modes. An extensive tech tree with over 400 different 
technologies, combined with the unit design system, allows for 
a wide variety of possible units and tactics.

Warzone 2100 was originally developed as a commercial game by 
Pumpkin Studios and published in 1999, and was released as 
open source by them in 2004, for the community to continue 
working on it.

This package provides the binaries for Warzone 2100.

%package data
Summary:        Data files for Warzone 2100
Group:          Amusements/Games/Strategy/Real Time
Requires:       %{name} = %{version}
BuildArch:      noarch 

%description data
You command the forces of "The Project" in a battle to rebuild 
the world after mankind has almost been destroyed by nuclear 
missiles. 

The game offers campaign, multi-player and single-player skirmish 
modes. An extensive tech tree with over 400 different 
technologies, combined with the unit design system, allows for 
a wide variety of possible units and tactics.

Warzone 2100 was originally developed as a commercial game by 
Pumpkin Studios and published in 1999, and was released as 
open source by them in 2004, for the community to continue 
working on it.

This package provides the binaries for Warzone 2100.

%prep
%setup -q
%patch2 -p1
%patch3 -p1

# constant timestamp for reproducible builds
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE99}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%T")\""
find .  -name '*.cpp' | xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"

%build
./autogen.sh
%configure \
  --docdir=%{_docdir}/%{name} \
  --with-distributor="openSUSE Build Service" \
  --with-icondir=%{_datadir}/pixmaps
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang %{name}
%suse_update_desktop_file -i %{name}

mkdir -p %{buildroot}%{_datadir}/appdata/
mv %{buildroot}%{_datadir}/metainfo/warzone2100.appdata.xml %{buildroot}%{_datadir}/appdata/warzone2100.appdata.xml

%post
%desktop_database_post

%postun
%desktop_database_postun

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/appdata/warzone2100.appdata.xml
%{_datadir}/pixmaps/*
%doc AUTHORS ChangeLog COPYING COPYING.NONGPL COPYING.README
%doc %{_docdir}/%{name}
%{_mandir}/man6/%{name}.6.*
%if 0%{?suse_version} == 1110
%dir %{_datadir}/locale/la
%dir %{_datadir}/locale/la/LC_MESSAGES
%endif

%files data
%defattr(-,root,root,-)
%{_datadir}/warzone2100/

%changelog
