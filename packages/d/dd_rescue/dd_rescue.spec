#
# spec file for package dd_rescue
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


Name:           dd_rescue
Version:        1.99.8
Release:        0
Summary:        Data copying in the presence of I/O Errors
License:        GPL-2.0-only OR GPL-3.0-only
Group:          System/Base
URL:            http://www.garloff.de/kurt/linux/ddrescue/
Source0:        http://garloff.de/kurt/linux/ddrescue/%{name}-%{version}.tar.bz2
Source1:        http://garloff.de/kurt/linux/ddrescue/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source99:       %{name}.changes
Patch1:         ddr_1998-alg-caseindep.diff
Patch2:         ddr_1998-check-nofail-noxattr.diff
Patch3:         ddr_1998-sysrandom.diff
Patch4:         ddr_1998-testhole.diff
Patch5:         ddr_1998-ossl11-warn.diff
BuildRequires:  autoconf
BuildRequires:  libattr-devel
BuildRequires:  lzo-devel
%if 0%{?suse_version} >= 1200
BuildRequires:  lzop
%endif
BuildRequires:  pkgconfig
BuildRequires:  python
Requires:       bc
Recommends:     dd_rescue-crypt
Recommends:     dd_rescue-lzo
Recommends:     dd_rhelp
Recommends:     libfallocate0
# ddrescue was last used in openSUSE 11.4 (version 1.14_0.0.6)
Provides:       ddrescue = %{version}
Obsoletes:      ddrescue < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  libopenssl-devel

%description
dd_rescue helps when nothing else can: your disk has crashed and you
try to copy it over to another one. While standard Unix tools like cp,
cat, and dd will "abort" on every I/O error, dd_rescue does not.

dd_rescue has many other goodies; optimization by using large blocks
as long as no errors are in sight and falling back to small ones; reverse
direction copy; splice in-kernel zerocopy; O_DIRECT support; preallocation
with fallocate().

dd_rescue also provides data protection features by overwriting files
or disks with fast random numbers, optionally multiple times.

dd_rescue supports plugins; currently a hash, an lzo and a crypt plugin
exist, supporting on the fly hash/HMAC calculation/validation, lzo
de/compression and de/encryption. The lzo plugin is packaged in the
dd_rescue-lzo, the crypt plugin in the dd_rescue-crypt subpackage.

%package crypt
Summary:        Crypt plugin for dd_rescue
Group:          System/Base
Requires:       dd_rescue = %{version}

%description crypt
This plugin allows you do de/encrypt files during recovery copying
with dd_rescue using the AES family of algorithms. The plugin
supports various numbers of bits and rounds and uses the x86 AESNI
CPU support if available.

The plugin does offer a variety of options to handle the keys
and IVs including the generating keys from password and salt.

The plugin is new as of 1.98 and it despite diligent testing it
might be careful to expect some bugs and future changes.

%package lzo
Summary:        LZO plugin for dd_rescue
Group:          System/Base
Requires:       dd_rescue = %{version}

%description lzo
This plugin allows you do de/compress files during recovery copying
with dd_rescue using the lzo family of algorithms. lzo algorithms
are very fast to decompress and most algorithms are very fast to
compress as well -- at the expense of somewhat worse compression than
zlib's deflate.

The plugin does offer a variety of options to handle corrupted .lzo
files with some grace; it does skip over bad blocks (if the block
headers are still intact) by default, but does offer an option (nodiscard)
to allow to attempt decompression on faulty input, hoping to produce
some usable bytes. It can also search for valid block headers after
synchronization has been lost due to a corrupt one.

The plugin also handles sparse files (files with holes) and supports
appending to .lzo files, so it fits neatly into dd_rescue.

Some fuzz testing has been applied to the plugin's decompression routines,
though more will have to be done to feel confident about feeding untrusted
data to the decompressor; the plugin is still young and might expose bugs.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
# Remove build time references so build-compare can do its work
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{SOURCE99} '+%%H:%%M')
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{SOURCE99} '+%%b %%e %%Y')
sed -i "s/__TIME__/\"$FAKE_BUILDTIME\"/g" dd_rescue.c
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/g" dd_rescue.c

%build
autoheader
autoconf
%configure
# avoid running dependency generation step
touch .dep
make RPM_OPT_FLAGS="%{optflags}" LIBDIR=%{_libdir} LIB=%{_lib} %{?_smp_mflags}

%install
%make_install RPM_OPT_FLAGS="%{optflags}" INSTALLDIR=%{buildroot}/%{_bindir} LIB=%{_lib} LIBDIR=%{_libdir} \
    INSTASROOT= INSTALLFLAGS=

mkdir %{buildroot}/bin
ln -sf %{_bindir}/dd_rescue %{buildroot}/bin

%check
make %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags} -fcommon" check

%files
%defattr(-,root,root,-)
%doc README.dd_rescue TODO
%license COPYING
%{_bindir}/dd_rescue
/bin/dd_rescue
%{_libdir}/libddr_hash.so
%{_libdir}/libddr_MD5.so
%{_libdir}/libddr_null.so
%{_mandir}/man1/dd_rescue.1%{ext_man}

%files crypt
%defattr(-,root,root)
%{_mandir}/man1/ddr_crypt.1%{ext_man}
%{_libdir}/libddr_crypt.so

%files lzo
%defattr(-,root,root,-)
%{_libdir}/libddr_lzo.so
%{_mandir}/man1/ddr_lzo.1%{ext_man}
%doc CRYPT_TODO PADDING

%changelog
