#
# spec file for package dmidecode
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


Name:           dmidecode
Version:        3.2
Release:        0
Summary:        DMI table decoder
License:        GPL-2.0-or-later
Group:          System/Console
URL:            http://www.nongnu.org/dmidecode/
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz
Source1:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz.sig
# https://savannah.nongnu.org/project/memberlist-gpgkeys.php?group=dmidecode
Source2:        %{name}.keyring
Patch1:         dmidecode-fix-redfish-hostname-print-length.patch
Patch2:         dmidecode-add-logical-non-volatile-device.patch
Patch3:         dmidecode-only-scan-dev-mem-for-entry-point-on-x86.patch
Patch4:         dmidecode-fix-formatting-of-tpm-table-output.patch
Patch5:         dmidecode-fix-system-slot-information-for-pcie-ssd.patch
Patch6:         dmidecode-add-enumerated-values-from-smbios-3.3.0.patch
Patch7:         dmidecode-print-type-33-name-unconditionally.patch
Patch8:         dmidecode-dont-choke-on-invalid-processor-voltage.patch
Patch9:         dmidecode-fix-the-alignment-of-type-25-name.patch
Patch10:        dmidecode-allow-overriding-build-settings-from-env.patch
Provides:       pmtools:%{_sbindir}/dmidecode
Obsoletes:      pmtools < 20071117
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
ExclusiveArch:  %ix86 ia64 x86_64 %arm aarch64

%description
Dmidecode reports information about your system's hardware as described
in your system BIOS according to the SMBIOS/DMI standard. This
information typically includes system manufacturer, model name, serial
number, BIOS version, asset tag as well as a lot of other details of
varying level of interest and reliability depending on the
manufacturer. This will often include usage status for the CPU sockets,
expansion slots (e.g. AGP, PCI, ISA) and memory module slots, and the
list of I/O ports (e.g. serial, parallel, USB).

Beware that DMI data have proven to be too unreliable to be blindly
trusted. Dmidecode does not scan your hardware, it only reports what
the BIOS told it to.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
install -dm 755 %{buildroot}%{_sbindir}
install -dm 755 %{buildroot}%{_mandir}/man8
install -dm 755 %{buildroot}%{_docdir}/%{name}
%ifarch ia64 %arm aarch64
for i in dmidecode ; do
%else
for i in dmidecode vpddecode ownership biosdecode ; do
%endif
install -m 755 $i %{buildroot}%{_sbindir}/
install -m 644 man/$i.8 %{buildroot}%{_mandir}/man8/
done

%files
%defattr(-,root,root)
%{_sbindir}/*
%dir %{_docdir}/%{name}
%doc AUTHORS NEWS README
%{_mandir}/man8/*
%license LICENSE

%changelog
