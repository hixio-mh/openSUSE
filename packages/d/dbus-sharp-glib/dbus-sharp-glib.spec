#
# spec file for package dbus-sharp-glib
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


# Define _libexecdir for <= 1110
%if 0%{?suse_version} <= 1110
%define _libexecdir %{_prefix}/lib
%endif

Name:           dbus-sharp-glib
Version:        0.5.0
Release:        1
License:        MIT
Summary:        Glib integration for DBus
Url:            http://mono.github.com/dbus-sharp/
Group:          Development/Libraries/Other
Source:         dbus-sharp-glib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  pkgconfig
%if 0%{?suse_version} >= 1130
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(dbus-sharp-1.0)
%else
BuildRequires:  mono-devel
BuildRequires:  dbus-sharp-devel
%endif
Requires:       dbus-sharp

%description
This package provides glib integration for Mono.DBus.

%package devel
License:        MIT
Summary:        Glib integration for DBus - development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This package provides glib integration for Mono.DBus - Development
files.

%prep
%setup -q

%build
# '--target' required on <= 1110 else build fails using configure macro
%configure \
%if 0%{?suse_version} <= 1110
   --target=%{_arch} \
%endif
   --libdir=%{_libexecdir}
make %{?_smp_mflags}

%install
# For backward compatability with <= 1110
make DESTDIR=%{buildroot} install
# Move .pc file to /usr/share/pkgconfig (for no arch) and remove from libdir
install -Dm 0644 %{name}-1.0.pc %{buildroot}%{_datadir}/pkgconfig/%{name}-1.0.pc
find %{buildroot}%{_libexecdir} -name %{name}-1.0.pc -type f -print -delete

%files
%defattr(-,root,root)
%doc COPYING README
%{_prefix}/lib/mono/gac/%{name}/
%{_prefix}/lib/mono/%{name}-1.0/

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/%{name}-1.0.pc

%changelog
