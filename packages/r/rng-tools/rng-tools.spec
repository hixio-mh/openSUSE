#
# spec file for package rng-tools
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rng-tools
Version:        5
Release:        0
Summary:        Support daemon for hardware random device
License:        GPL-3.0+
Group:          System/Kernel
Url:            http://sourceforge.net/projects/gkernel/
Source:         http://sourceforge.net/projects/gkernel/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source2:        %{name}.service
Source3:        90-hwrng.rules
Patch0:         rng-tools-check_signals.patch
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Supplements:    modalias(pci:v00001022d00007443sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00001022d0000746Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002410sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002420sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002440sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000244Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002450sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002480sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000248Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000024C0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000024CCsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000024D0sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000025A1sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002640sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002641sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002670sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002671sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002672sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002673sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002674sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002675sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002676sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002677sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002678sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d00002679sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000267Asv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000267Bsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000267Csv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000267Dsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000267Esv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000267Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000027B8sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000027B9sv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d000027BDsv*sd*bc*sc*i*)
Supplements:    modalias(virtio:d00000004v*)
ExclusiveArch:  aarch64 %ix86 ia64 x86_64 %{arm} ppc64 ppc64le
%{?systemd_requires}
%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d }

%description
This  daemon  feeds data from a random number generator to the kernel's
random  number  entropy  pool,  after	first checking the data to
ensure that it is properly random.

%prep
%setup -q
%patch0

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_udevrulesdir}/90-hwrng.rules
ln -sf /sbin/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service

%post
%{?udev_rules_update:%{udev_rules_update}}
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%doc NEWS
%{_bindir}/rngtest
%{_sbindir}/rngd
%{_mandir}/man?/*.*.gz
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_udevrulesdir}/90-hwrng.rules

%changelog
