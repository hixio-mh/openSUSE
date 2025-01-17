#
# spec file for package kernel-obs-build
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
# needsrootforbuild


#!BuildIgnore: post-build-checks

%define patchversion 5.7.7
%define variant %{nil}
%define vanilla_only 0

%include %_sourcedir/kernel-spec-macros

Name:           kernel-obs-build
BuildRequires:  coreutils
BuildRequires:  device-mapper
BuildRequires:  util-linux

%if 0%{?suse_version}
%if %vanilla_only
%define kernel_flavor -vanilla
%else
%ifarch %ix86
%define kernel_flavor -pae
%else
%ifarch armv7l armv7hl
%define kernel_flavor -lpae
%else
%define kernel_flavor -default
%endif
%endif
%endif
%endif
BuildRequires:  kernel%kernel_flavor-srchash-cba119b9d536c22bb0a3705ec58f0411fee53b7e

%if 0%{?rhel_version}
BuildRequires:  kernel
%define kernel_flavor ""
%endif

ExclusiveArch:  aarch64 armv6hl armv7hl %ix86 ppc64 ppc64le riscv64 s390x x86_64
%if 0%{?suse_version} < 1315
# For SLE 11
BuildRequires:  mkinitrd
BuildRequires:  perl-Bootloader
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%else
BuildRequires:  dracut
%endif
Summary:        package kernel and initrd for OBS VM builds
License:        GPL-2.0
Group:          SLES
Version:        5.7.7
%if 0%{?is_kotd}
Release:        <RELEASE>.gcba119b
%else
Release:        0
%endif

%description
This package is repackaging already compiled kernels to make them usable
inside of Open Build Service (OBS) VM builds. An initrd with some basic
kernel modules is generated as well, but further kernel modules can be
loaded during build when installing the kernel package.

%prep

%build
mkdir -p /usr/lib/dracut/modules.d/80obs
cat > /usr/lib/dracut/modules.d/80obs/module-setup.sh <<EOF
#!/bin/bash

# called by dracut
check() {
    return 0
}

# called by dracut
installkernel() {
    hostonly='' instmods obs
}

# called by dracut
install() {
    inst_hook pre-udev 10 "\$moddir"/setup_obs.sh
}
EOF
chmod a+rx /usr/lib/dracut/modules.d/80obs/module-setup.sh
cat > /usr/lib/dracut/modules.d/80obs/setup_obs.sh <<EOF
#!/bin/sh
info "Loading kernel modules for OBS"
info "  Loop..."
modprobe loop max_loop=64 lbs=0 || modprobe loop max_loop=64
info "  binfmt misc..."
modprobe binfmt_misc
EOF
chmod a+rx /usr/lib/dracut/modules.d/80obs/setup_obs.sh
# Configure systemd in kernel-obs-build's initrd not to limit TasksMax,
# we run with build as PID 1 (boo#965564)
echo "DefaultTasksMax=infinity" >> /etc/systemd/system.conf
echo "DefaultTasksAccounting=no" >> /etc/systemd/system.conf

# a longer list to have them also available for qemu cross builds where x86_64 kernel runs in eg. arm env.
# this list of modules where available on build workers of build.opensuse.org, so we stay compatible.
export KERNEL_MODULES="loop dm-crypt dm-mod dm-snapshot binfmt-misc fuse kqemu squashfs ext2 ext3 ext4 reiserfs btrfs xfs nf_conntrack_ipv6 binfmt_misc virtio_pci virtio_mmio virtio_blk virtio_rng fat vfat nls_cp437 nls_iso8859-1 ibmvscsi sd_mod e1000 ibmveth"

# manually load all modules to make sure they're available
for i in $KERNEL_MODULES; do
(
  echo "info '  $i'"
  echo "modprobe $i"
) >> /usr/lib/dracut/modules.d/80obs/setup_obs.sh
done

ROOT=""
[ -e "/dev/vda" ] && ROOT="-d /dev/vda"
[ -e /dev/hda1 ] && ROOT="-d /dev/hda1" # for xen builds
%define kernel_name vmlinu?
%ifarch s390 s390x
%define kernel_name image
%endif
%ifarch %arm
%define kernel_name zImage
%endif
%ifarch aarch64 riscv64
%define kernel_name Image
%endif

%if 0%{?suse_version} && 0%{?suse_version} < 1315
# For SLE 11
/sbin/mkinitrd $ROOT \
               -m "$KERNEL_MODULES" \
               -k /boot/%{kernel_name}-*-default -M /boot/System.map-*-default -i /tmp/initrd.kvm -B
%else
dracut --host-only --no-hostonly-cmdline --drivers="$KERNEL_MODULES" --force /tmp/initrd.kvm `echo /boot/%{kernel_name}-*%{kernel_flavor} | sed -n -e 's,[^-]*-\(.*'%{kernel_flavor}'\),\1,p'`
%endif

#cleanup
rm -rf /usr/lib/dracut/modules.d/80obs

%install
install -d -m 0755 $RPM_BUILD_ROOT
cp -v /boot/%{kernel_name}-*%{kernel_flavor} $RPM_BUILD_ROOT/.build.kernel.kvm
cp -v /tmp/initrd.kvm $RPM_BUILD_ROOT/.build.initrd.kvm

#inform worker about arch
#see obs-build commit e47399d738e51
uname -m > $RPM_BUILD_ROOT/.build.hostarch.kvm

%files
%defattr(-,root,root)
/.build.kernel.*
/.build.initrd.*
/.build.hostarch.*

%changelog
