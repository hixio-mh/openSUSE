#
# spec file for package mosquitto
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


%define home    %{_localstatedir}/lib/%{name}
%define c_lib   libmosquitto1
%define cpp_lib libmosquittopp1
%if 0%{?suse_version} > 1230 || 0%{?rhel_version} > 600 || 0%{?centos_version} > 600 || 0%{?fedora_version} >= 20 || 0%{?el7}%{?fc20}%{?fc21}%{?fc22}%{?fc23}%{?fc24}%{?fc25}
%bcond_without  systemd
%else
%bcond_with     systemd
%endif
%bcond_without  websockets
Name:           mosquitto
Version:        1.6.10
Release:        0
Summary:        A MQTT v3.1/v3.1.1 Broker
License:        EPL-1.0
Group:          Productivity/Networking/Other
URL:            https://mosquitto.org/
Source:         https://mosquitto.org/files/source/mosquitto-%{version}.tar.gz
Source98:       https://mosquitto.org/files/source/mosquitto-%{version}.tar.gz.asc#/%{name}-%{version}.tar.gz.sig
Source99:       %{name}.keyring
Source1:        mosquitto.service
Source4:        README-conf-d
Source5:        README-ca_certificates
Source6:        README-certs
Patch0:         mosquitto-1.4.1_apparmor.patch
Patch1:         mosquitto-1.6.8-config.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcares-devel
BuildRequires:  openssl-devel >= 1.0.0
BuildRequires:  tcpd-devel
BuildRequires:  uthash-devel
Requires(pre):  shadow
%if %{with websockets}
BuildRequires:  libwebsockets-devel
%endif
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%endif

%description
Mosquitto is a message broker that implements the
MQ Telemetry Transport protocol versions 3.1 and 3.1.1. MQTT provides a
lightweight method of carrying out messaging using a publish/subscribe model.
This makes it suitable for "machine to machine" messaging such as with low
power sensors or mobile devices such as phones, embedded computers or
microcontrollers like the Arduino. A good example of this is all of the work
that Andy Stanford-Clark (one of the originators of MQTT) has done in home
monitoring and automation with his twittering house and twittering ferry.

%package -n %{c_lib}
Summary:        Shared C Library for %{name}
Group:          Development/Libraries/C and C++

%description -n %{c_lib}
Mosquitto is a message broker that implements the
MQ Telemetry Transport protocol versions 3.1 and 3.1.1. MQTT provides a
lightweight method of carrying out messaging using a publish/subscribe model.

This package holds the shared C library.

%package -n %{cpp_lib}
Summary:        Shared C++ Library for %{name}
Group:          Development/Libraries/C and C++

%description -n %{cpp_lib}
Mosquitto is a message broker that implements the
MQ Telemetry Transport protocol versions 3.1 and 3.1.1. MQTT provides a
lightweight method of carrying out messaging using a publish/subscribe model.

This package holds the shared C++ library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}
Requires:       %{cpp_lib} = %{version}
Provides:       libmosquitto-devel = %{version}-%{release}
Provides:       libmosquittopp-devel = %{version}-%{release}

%description devel
Mosquitto is a message broker that implements the
MQ Telemetry Transport protocol versions 3.1 and 3.1.1. MQTT provides a
lightweight method of carrying out messaging using a publish/subscribe model.

This package holds the development files.

%package clients
Summary:        Client for Mosquitto
Group:          Productivity/Networking/Other

%description clients
Mosquitto is a message broker that implements the
MQ Telemetry Transport protocol versions 3.1 and 3.1.1. MQTT provides a
lightweight method of carrying out messaging using a publish/subscribe model.
This makes it suitable for "machine to machine" messaging such as with low
power sensors or mobile devices such as phones, embedded computers or
microcontrollers like the Arduino. A good example of this is all of the work
that Andy Stanford-Clark (one of the originators of MQTT) has done in home
monitoring and automation with his twittering house and twittering ferry.

Client for Mosquitto.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
find misc -type f -exec chmod a-x "{}" "+"

%build
%cmake \
  -DCMAKE_INSTALL_SYSCONFDIR=/etc \
  %if %{with websockets}
  -DWITH_WEBSOCKETS=ON \
  %endif
  -DUSE_LIBWRAP=OFF
make

%install
%cmake_install
%if %{with systemd}
install -D -m 0644 %{SOURCE1} \
  %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%endif
install -Dd -m 0750 %{buildroot}%{home}
chmod -R o= %{buildroot}%{_sysconfdir}/%{name}/
%if 0%{?suse_version}
install -D -m 644 security/mosquitto.apparmor %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.mosquitto
install -D -m 755 -d                          %{buildroot}%{_sysconfdir}/apparmor.d/local/
echo "# Site-specific additions and overrides for 'usr.sbin.mosquitto'" > %{buildroot}%{_sysconfdir}/apparmor.d/local/usr.sbin.mosquitto
%endif
install -D -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/mosquitto/conf.d/README
install -D -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/mosquitto/ca_certificates/README
install -D -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/mosquitto/certs/README

%pre
getent group %{name} || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} || %{_sbindir}/useradd -g %{name} -s /bin/false -r -c "%{name}" -d %{home} %{name}
# START BIG SYSTEMD
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre %{name}.service
%endif

%preun
%if 0%{?suse_version}
%service_del_preun %{name}.service
%else
%systemd_preun %{name}.service
%endif

%post
%if 0%{?suse_version}
%service_add_post %{name}.service
%else
%systemd_post %{name}.service
%endif

%postun
%if 0%{?suse_version}
%service_del_postun %{name}.service
%else
%systemd_postun_with_restart %{name}.service
%endif
%endif
# /END BIG SYSTEMD

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%post -n %{cpp_lib} -p /sbin/ldconfig
%postun -n %{cpp_lib} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE.txt
%doc edl-v10 epl-v10
%doc CONTRIBUTING.md ChangeLog.txt readme.md *.html *.example
%doc examples/ logo/ security/ misc/
%config(noreplace) %attr(-,root,%{name}) %{_sysconfdir}/mosquitto/
%{_bindir}/mosquitto_passwd
%{_sbindir}/mosquitto
%{_mandir}/man1/mosquitto_passwd.1%{ext_man}
%{_mandir}/man5/mosquitto.conf.5%{ext_man}
%{_mandir}/man7/mosquitto-tls.7%{ext_man}
%{_mandir}/man7/mqtt.7%{ext_man}
%{_mandir}/man8/mosquitto.8%{ext_man}
%if %{with systemd}
%{_unitdir}/%{name}.service
%if 0%{?suse_version}
%{_sbindir}/rc%{name}
%endif
%endif
%dir %attr(-,%{name},%{name}) %{home}
%if 0%{?suse_version}
%dir %{_sysconfdir}/apparmor.d/
%dir %{_sysconfdir}/apparmor.d/local/
%config %{_sysconfdir}/apparmor.d/usr.sbin.mosquitto
%config(noreplace) %{_sysconfdir}/apparmor.d/local/usr.sbin.mosquitto
%endif

%files clients
%defattr(-,root,root,-)
%license LICENSE.txt
%doc edl-v10 epl-v10
%{_bindir}/mosquitto_pub
%{_bindir}/mosquitto_sub
%{_bindir}/mosquitto_rr
%{_mandir}/man1/mosquitto_pub.1%{ext_man}
%{_mandir}/man1/mosquitto_sub.1%{ext_man}
%{_mandir}/man1/mosquitto_rr.1%{ext_man}

%files -n %{c_lib}
%defattr(-,root,root)
%license LICENSE.txt
%doc edl-v10 epl-v10
%{_libdir}/libmosquitto.so.*

%files -n %{cpp_lib}
%defattr(-,root,root)
%license LICENSE.txt
%doc edl-v10 epl-v10
%{_libdir}/libmosquittopp.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libmosquitto.so
%{_libdir}/libmosquittopp.so
%{_includedir}/mosquitto.h
%{_includedir}/mosquitto_broker.h
%{_includedir}/mosquitto_plugin.h
%{_includedir}/mosquittopp.h
%{_mandir}/man3/libmosquitto.3%{ext_man}
%{_libdir}/pkgconfig/libmosquitto.pc
%{_libdir}/pkgconfig/libmosquittopp.pc

%changelog
