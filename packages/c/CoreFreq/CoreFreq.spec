#
# spec file for package CoreFreq
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


# from coretypes.h
%define corefreq_major  1
%define corefreq_minor  75
%define corefreq_rev    2
%define gitdate 20200418
Name:           CoreFreq
Version:        %{corefreq_major}.%{corefreq_minor}.%{corefreq_rev}+git%{gitdate}
Release:        0
Summary:        CPU monitoring software designed for 64-bits processors
License:        GPL-2.0-or-later
URL:            https://github.com/cyring/CoreFreq
Source:         %{name}-%{version}.tar.gz
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
Requires:       CoreFreq-kmp
ExclusiveArch:  x86_64
%systemd_ordering
%kernel_module_package

%description
A CPU monitoring software with BIOS like functionalities, is designed for the 64-bits
Processors of architecture Intel Atom, Core2, Nehalem, SandyBridge and superiors;
AMD Families 0Fh ... 17h (Zen), 18h (Hygon Dhyana)

%prep
%setup -q -n CoreFreq

%build
%make_build

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
PREFIX=%{buildroot}%{_prefix} make install

# replace invocation in corefreqd.service of /bin/corefreqd  by /usr/bin/corefreqd
sed -i -e 's/\/bin\/corefreqd/\/usr\/bin\/corefreqd/g' %{buildroot}%{_unitdir}/corefreqd.service

# load module on boot. Necessary for corefreqd to be able to run
mkdir -p %{buildroot}%{_libexecdir}/modules-load.d
echo corefreqk > %{buildroot}%{_libexecdir}/modules-load.d/corefreq.conf

mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rccorefreqd

%files
%license LICENSE
%doc README.md
%{_bindir}/corefreq-cli
%{_bindir}/corefreqd
%{_unitdir}/corefreqd.service
%{_sbindir}/rccorefreqd
%dir %{_libexecdir}/modules-load.d
%{_libexecdir}/modules-load.d/corefreq.conf

%pre
%service_add_pre corefreqd.service

%post
%service_add_post corefreqd.service

%preun
%service_del_preun corefreqd.service

%postun
%service_del_postun corefreqd.service

%changelog
