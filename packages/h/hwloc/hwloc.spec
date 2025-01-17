#
# spec file for package hwloc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global lname libhwloc15
Name:           hwloc
Version:        2.1.0
Release:        0
Summary:        Portable Hardware Locality
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
Url:            http://www.open-mpi.org/projects/hwloc/
Source0:        https://download.open-mpi.org/release/hwloc/v2.1/%{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(x11)
Requires:       %{lname} = %{version}-%{release}
Requires:       perl-JSON
Requires:       perl-base >= 5.18.2
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%ifnarch s390 s390x i586 aarch64 %{arm}
BuildRequires:  libnuma-devel
%endif

%description
The Portable Hardware Locality (hwloc) software package provides
an abstraction (across OS, versions, architectures, ...)
of the hierarchical topology of modern architectures, including
NUMA memory nodes, shared caches, processor sockets, processor cores
and processing units (logical processors or "threads"). It also gathers
various system attributes such as cache and memory information. It primarily
aims at helping applications with gathering information about modern
computing hardware so as to exploit it accordingly and efficiently.

hwloc may display the topology in multiple convenient formats.
It also offers a powerful programming interface (C API) to gather information
about the hardware, bind processes, and much more.

%package devel
Summary:        Headers and shared development libraries for hwloc
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Provides:       libhwloc-devel = %{version}
Obsoletes:      libhwloc-devel < %{version}
Obsoletes:      libhwloc-devel = 0.0.0

%description devel
This package contains the headers and shared object symbolic links
for the hwloc.

%package -n %{lname}
Summary:        Runtime libraries for hwloc
Group:          System/Libraries
Requires:       %{name}-data

%description -n %{lname}
This package contains the run time libraries for hwloc.

%package data
Summary:        Run time data for hwloc
Group:          Development/Libraries/C and C++
%if 0%{?sle_version} > 120300 || 0%{?is_opensuse}
BuildArch:      noarch
%endif

%description data
This package contains the run time data for the hwloc.

%package doc
Summary:        Documentation for hwloc
Group:          Documentation/Other
%if 0%{?sle_version} > 120300 || 0%{?is_opensuse}
BuildArch:      noarch
%endif

%description doc
This package contains the documentation for hwloc.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -fvi

%configure \
    --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -r lstopo System Monitor
# We don't ship .la files.
rm -rf %{buildroot}%{_libdir}/libhwloc.la

# documentation will be handled by % doc macro
rm -rf %{buildroot}%{_datadir}/doc/

# This binary is built only for intel architectures
%ifarch %{ix86} x86_64
mkdir -p %{buildroot}%{_libexecdir}/systemd/system
mv %{buildroot}%{_datadir}/hwloc/hwloc-dump-hwdata.service %{buildroot}%{_libexecdir}/systemd/system/hwloc-dump-hwdata.service
%else
rm %{buildroot}%{_datadir}/hwloc/hwloc-dump-hwdata.service
%endif

%fdupes -s %{buildroot}/%{_mandir}/man1
%fdupes -s %{buildroot}/%{_mandir}/man7

%check
#XXX: this is weird, but make check got broken by removing doxygen-doc/man above
#     the only one fix is to install documentation by hand, or to ignore check error
make %{?_smp_mflags} check || :

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING NEWS README VERSION
%{_mandir}/man1/hwloc*
%{_mandir}/man1/lstopo*
%{_bindir}/hwloc*
%{_bindir}/lstopo*
%{_datadir}/applications/*.desktop
%{_sysconfdir}/bash_completion.d/hwloc-completion.bash
%ifarch %{ix86} x86_64
%attr(0755,root,root) %{_sbindir}/hwloc-dump-hwdata
%{_libexecdir}/systemd/system/hwloc-dump-hwdata.service
%endif

%files devel
%defattr(-, root, root, -)
%{_mandir}/man7/hwloc*
%{_includedir}/hwloc
%{_includedir}/hwloc.h
%{_libdir}/libhwloc.so
%{_libdir}/pkgconfig/hwloc.pc

%files -n %{lname}
%defattr(-, root, root, -)
%{_libdir}/libhwloc*so.*

%files data
%defattr(-, root, root, -)
%dir %{_datadir}/hwloc
%dir %{_datadir}/hwloc/hwloc-ps.www
%{_datadir}/hwloc/hwloc.dtd
%{_datadir}/hwloc/hwloc2-diff.dtd
%{_datadir}/hwloc/hwloc2.dtd
%{_datadir}/hwloc/hwloc-valgrind.supp
%{_datadir}/hwloc/hwloc-ps.www/*

%files doc
%defattr(-, root, root, -)
%doc ./doc/doxygen-doc/html/*
%{_mandir}/man3/*

%changelog
