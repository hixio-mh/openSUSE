#
# spec file for package ffms2
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Packman Team <packman@links2linux.de>
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


%define aversion 2.23
%define libname lib%{name}
%define soname 4
Name:           ffms2
Version:        2.23.1
Release:        0
Summary:        Wrapper library around FFmpeg libraries
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/FFMS/ffms2
Source:         https://github.com/FFMS/ffms2/archive/%{aversion}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         ffms2-pkgconfig.patch
BuildRequires:  gcc-c++ >= 4.8
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FFmpegSource (usually known as FFMS or FFMS2) is a wrapper
library around FFmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

%package -n ffmsindex
Summary:        Wrapper library around libffmpeg
Group:          Productivity/Multimedia/Other

%description -n ffmsindex
FFmpegSource (usually known as FFMS or FFMS2) is a wrapper
library around FFmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

%package -n %{libname}-%{soname}
Summary:        Wrapper library around libffmpeg
Group:          System/Libraries

%description -n %{libname}-%{soname}
FFmpegSource (usually known as FFMS or FFMS2) is a wrapper
library around FFmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

%package -n %{libname}-devel
Summary:        Wrapper library around libffmpeg
Group:          Development/Libraries/C and C++
Requires:       %{libname}-%{soname} = %{version}

%description -n %{libname}-devel
FFmpegSource (usually known as FFMS or FFMS2) is a wrapper
library around FFmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

%prep
%setup -q -n %{name}-%{aversion}
%patch0 -p1
sed -i 's/\r$//' COPYING

%build
%configure --docdir=%{_docdir}/%{libname}-devel \
           --disable-static --enable-shared

make %{?_smp_mflags} V=1

%install
%make_install V=1
rm %{buildroot}%{_libdir}/%{libname}.la

%post -n %{libname}-%{soname} -p /sbin/ldconfig
%postun -n %{libname}-%{soname} -p /sbin/ldconfig

%files -n ffmsindex
%defattr(0644, root, root, 0755)
%attr(0755,root,root) %{_bindir}/ffmsindex

%files -n %{libname}-%{soname}
%defattr(0644, root, root, 0755)
%doc COPYING
%{_libdir}/%{libname}.so.%{soname}*

%files -n %{libname}-devel
%defattr(0644, root, root, 0755)
%{_libdir}/%{libname}.so
%{_includedir}/ffms*
%{_libdir}/pkgconfig/%{name}.pc
%{_docdir}/%{libname}-devel

%changelog
