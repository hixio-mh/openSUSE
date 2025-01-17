#
# spec file for package pcm
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


Name:           pcm
Version:        201902
Release:        0
Summary:        Processor Counter Monitor
License:        BSD-3-Clause
Group:          System/Monitoring
URL:            https://github.com/opcm/pcm
Source:         https://github.com/opcm/pcm/archive/%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  make
ExclusiveArch:  %ix86 x86_64

%description
Processor Counter Monitor (PCM) is an application programming interface (API)
and a set of tools based on the API to monitor performance and energy metrics
of Intel Core, Xeon, Atom and Xeon Phi processors.

%prep
%setup -q
# do not mess with optflags
sed -i '/-Wall -g -O3/d' Makefile
sed -e 's:-O0 -g3 -Wall:%{optflags}:g' \
    -i daemon/client/Debug/subdir.mk \
    -i daemon/daemon/Debug/subdir.mk

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%make_build

%install
# install targets are overrated
for i in *.x; do
  install -D -m0755 $i %{buildroot}%{_sbindir}/${i/.x/}
done

%files
%license LICENSE
%doc *HOWTO*
%{_sbindir}/pcm
%{_sbindir}/pcm-core
%{_sbindir}/pcm-iio
%{_sbindir}/pcm-latency
%{_sbindir}/pcm-lspci
%{_sbindir}/pcm-memory
%{_sbindir}/pcm-msr
%{_sbindir}/pcm-numa
%{_sbindir}/pcm-pcicfg
%{_sbindir}/pcm-pcie
%{_sbindir}/pcm-power
%{_sbindir}/pcm-sensor
%{_sbindir}/pcm-tsx

%changelog
