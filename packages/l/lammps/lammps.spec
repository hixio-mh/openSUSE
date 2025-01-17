#
# spec file for package lammps
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017-2020 Christoph Junghans
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


# Build with OpenMPI
%if 0%{?sle_version} == 0
%define mpiver  openmpi2
%else
%if 0%{?sle_version} <= 120300
%define mpiver  openmpi
%else
  %if 0%{?sle_version} <= 150000
  %define mpiver  openmpi2
  %else
  %define mpiver  openmpi3
  %endif
%endif
%endif

Name:           lammps
Version:        20200505
Release:        0
%define         uversion patch_5May2020
Summary:        Molecular Dynamics Simulator
License:        GPL-2.0-only AND GPL-3.0-or-later
Group:          Productivity/Scientific/Chemistry
URL:            https://lammps.sandia.gov
Source0:        https://github.com/lammps/lammps/archive/%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz
Source1:        https://github.com/lammps/lammps-testing/archive/%{uversion}.tar.gz#/%{name}-testing-%{uversion}.tar.gz
# PATCH-FIX-UPSTREAM disable_noopt.patch, gcc flags a false positive [gh#lammps/lammps#2078]
Patch0:         disable_noopt.patch 
BuildRequires:  %{mpiver}
BuildRequires:  %{mpiver}-devel
BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gsl-devel
BuildRequires:  kim-api-devel >= 2.1
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
BuildRequires:  python-devel
BuildRequires:  voro++-devel
BuildRequires:  zlib-devel
%ifnarch ppc64 %ix86
%global         with_kokkos 1
BuildRequires:  kokkos-devel >= 3.1
%endif
Requires:       %{name}-data
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale 
Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for soft materials (biomolecules, polymers) and 
solid-state materials (metals, semiconductors) and coarse-grained or 
mesoscopic systems. It can be used to model atoms or, more generically, as a 
parallel particle simulator at the atomic, meso, or continuum scale.

LAMMPS runs on single processors or in parallel using message-passing 
techniques and a spatial-decomposition of the simulation domain. The code is 
designed to be easy to modify or extend with new functionality.

%package -n liblammps0
Summary:        LAMMPS library
Group:          System/Libraries

%description -n liblammps0
LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale 
Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for soft materials (biomolecules, polymers) and 
solid-state materials (metals, semiconductors) and coarse-grained or 
mesoscopic systems. It can be used to model atoms or, more generically, as a 
parallel particle simulator at the atomic, meso, or continuum scale.

LAMMPS runs on single processors or in parallel using message-passing 
techniques and a spatial-decomposition of the simulation domain. The code is 
designed to be easy to modify or extend with new functionality.

This package contains the library of LAMMPS package.

%package devel
Summary:        Development headers and libraries for LAMMPS
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       liblammps0 = %{version}

%description devel
LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale 
Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for soft materials (biomolecules, polymers) and 
solid-state materials (metals, semiconductors) and coarse-grained or 
mesoscopic systems. It can be used to model atoms or, more generically, as a 
parallel particle simulator at the atomic, meso, or continuum scale.

LAMMPS runs on single processors or in parallel using message-passing 
techniques and a spatial-decomposition of the simulation domain. The code is 
designed to be easy to modify or extend with new functionality.

This package contains development headers and libraries for LAMMPS.

%package -n python-%{name}
Summary:        LAMMPS python module
Group:          Development/Languages/Python
Requires:       liblammps0 = %{version}

%description -n python-%{name}
LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale 
Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for soft materials (biomolecules, polymers) and 
solid-state materials (metals, semiconductors) and coarse-grained or 
mesoscopic systems. It can be used to model atoms or, more generically, as a 
parallel particle simulator at the atomic, meso, or continuum scale.

LAMMPS runs on single processors or in parallel using message-passing 
techniques and a spatial-decomposition of the simulation domain. The code is 
designed to be easy to modify or extend with new functionality.

This subpackage contains LAMMPS's Python module.

%package data
Summary:        LAMMPS data
Group:          Productivity/Scientific/Chemistry
BuildArch:      noarch

%description data
LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale 
Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for soft materials (biomolecules, polymers) and 
solid-state materials (metals, semiconductors) and coarse-grained or 
mesoscopic systems. It can be used to model atoms or, more generically, as a 
parallel particle simulator at the atomic, meso, or continuum scale.

LAMMPS runs on single processors or in parallel using message-passing 
techniques and a spatial-decomposition of the simulation domain. The code is 
designed to be easy to modify or extend with new functionality.

This subpackage contains LAMMPS's potential files


%prep
%setup -a 1 -q -n %{name}-%{uversion}
%patch0 -p1
# see [gh#lammps/lammps#2079], this is a bug in older version 
# of the ocl package, compare [GCC#58241]
%ifarch ppc64le
sed -i '/CMAKE_CXX_EXTENSIONS/s/OFF/ON/' cmake/CMakeLists.txt
%endif

%build
source %{_libdir}/mpi/gcc/%{mpiver}/bin/mpivars.sh

%{cmake} \
  -C ../cmake/presets/all_on.cmake \
  -C ../cmake/presets/nolib.cmake \
  -DCMAKE_Fortran_COMPILER="$(type -p gfortran)" \
  -DCMAKE_TUNE_FLAGS='' \
  -DBUILD_TOOLS=ON \
  -DBUILD_OMP=ON \
  %{?with_kokkos:-DPKG_KOKKOS=ON -DEXTERNAL_KOKKOS=ON} \
  -DBUILD_MPI=ON -DPKG_PYTHON=ON \
  -DPKG_KIM=ON -DENABLE_TESTING=ON -DPKG_VORONOI=ON \
  -DPKG_GPU=ON -DGPU_API=OpenCL -DFFT=FFTW3 \
  -DPYTHON_INSTDIR=%{python_sitearch} -DCMAKE_INSTALL_SYSCONFDIR=/etc \
%ifnarch x86_64 i586
  -DPKG_USER-INTEL=OFF \
%endif  
  -DLAMMPS_TESTING_SOURCE_DIR=$(echo $PWD/../lammps-testing-*) ../cmake
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH='%{buildroot}%{_libdir}:%{_libdir}/mpi/gcc/%{mpiver}/%{_lib}'
%ctest

%post -n liblammps0 -p /sbin/ldconfig
%postun -n liblammps0 -p /sbin/ldconfig

%files
%doc README
%license LICENSE
%{_bindir}/lmp
%{_mandir}/man1/lmp.1.*
%{_bindir}/msi2lmp
%{_mandir}/man1/msi2lmp.1.*
%{_bindir}/binary2txt
%{_bindir}/chain.x

%files -n liblammps0
%{_libdir}/liblammps.so.*

%files devel
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/liblammps.so
%{_libdir}/pkgconfig/liblammps.pc
%{_libdir}/cmake/LAMMPS

%files -n python-%{name}
%{python_sitearch}/%{name}.py

%files data
%license LICENSE
%{_datadir}/%{name}
%config %{_sysconfdir}/profile.d/lammps.*

%changelog
