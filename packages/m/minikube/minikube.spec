#
# spec file for package minikube
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


Name:           minikube
Version:        1.11.0
Release:        0
Summary:        Tool to run Kubernetes locally
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/kubernetes/minikube
Source:         https://github.com/kubernetes/minikube/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        minikube-rpmlintrc
BuildRequires:  git-core
BuildRequires:  golang-github-jteeuwen-go-bindata
BuildRequires:  golang-packaging
BuildRequires:  libvirt-devel >= 1.2.14
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  wget
BuildRequires:  golang(API) = 1.14
Recommends:     docker-machine-driver-kvm2
Recommends:     kubernetes-client
Recommends:     libvirt
Recommends:     libvirt-daemon-qemu
Recommends:     qemu-kvm
ExclusiveArch:  %{ix86} x86_64 aarch64

%description
Minikube is a tool that allows running Kubernetes locally. Minikube
runs a single-node Kubernetes cluster inside a VM on your machine for
users looking to try out Kubernetes or develop with it day-to-day.

# vendor/github.com/libvirt/libvirt-go/domain_events.go:334: type [1073741824]_Ctype_struct__virDomainEventGraphicsSubjectIdentity too large
%ifnarch i586
%package -n docker-machine-driver-kvm2
Summary:        KVM driver for docker-machine
Group:          System/Management

%description -n docker-machine-driver-kvm2
KVM driver for docker-machine which is using libvirt for setting up
virtual machines with Docker.
%endif

%prep
%setup -q
tar -zxf %{SOURCE1}
sed -i -e "s|GO111MODULE := on|GO111MODULE := off|" Makefile

%build
%{goprep} k8s.io/minikube
export GOPATH=%{_builddir}/go
cd $GOPATH/src/k8s.io/minikube
mkdir $GOPATH/bin
ln -s %{_bindir}/go-bindata $GOPATH/bin/go-bindata
export IN_DOCKER=0
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git init
echo '*' > .gitignore
touch .dummy
git add -f .dummy .gitignore
git commit -m "trick hack/get_k8s_version.py"
make %{?_smp_mflags} out/minikube
%ifnarch i586
%ifarch aarch64
make %{?_smp_mflags} out/docker-machine-driver-kvm2-arm64
%else
make %{?_smp_mflags} out/docker-machine-driver-kvm2
%endif
%endif

%check
export GOPATH=%{_builddir}/go
cd $GOPATH/src/k8s.io/minikube
make %{?_smp_mflags} test || true

%install
output_path="%{_builddir}/go/src/k8s.io/minikube/out/"
binaries=(minikube)
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/minikube
%ifnarch i586
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/docker-machine-driver-kvm2*
%ifarch aarch64
# Add a symlink without '-arm64' suffix
pushd %{buildroot}%{_bindir}
ln -s docker-machine-driver-kvm2* docker-machine-driver-kvm2
popd
%endif
%endif

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_bindir}/minikube

%ifnarch i586
%files -n docker-machine-driver-kvm2
%license LICENSE
%{_bindir}/docker-machine-driver-kvm2*
%endif

%changelog
