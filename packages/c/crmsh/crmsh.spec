#
# spec file for package crmsh
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%bcond_with regression_tests

%global gname haclient
%global uname hacluster
%global crmsh_docdir %{_defaultdocdir}/%{name}

%global upstream_version tip
%global upstream_prefix crmsh
%global crmsh_release 1

%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?rhel} || 0%{?fedora}
%define pkg_group System Environment/Daemons
%else
%define pkg_group Productivity/Clustering/HA
%endif

Name:           crmsh
Summary:        High Availability cluster command-line interface
License:        GPL-2.0-or-later
Group:          %{pkg_group}
Version:        4.2.0+git.1594286044.7a596d12
Release:        0
Url:            http://crmsh.github.io
Source0:        %{name}-%{version}.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
# Requiring pacemaker makes crmsh harder to build on other distributions,
# and is mostly a convenience feature. So only do it for SUSE.
Requires(pre):  pacemaker
%endif
Requires:       %{name}-scripts >= %{version}-%{release}
Requires:       /usr/bin/which
Requires:       python3 >= 3.4
Requires:       python3-lxml
Requires:       python3-parallax
Requires:       python3-python-dateutil
BuildRequires:  python3-lxml
BuildRequires:  python3-setuptools

%if 0%{?suse_version}
# only require csync2 on SUSE since bootstrap
# only works for SUSE at the moment anyway
Requires:       csync2
%endif

%if 0%{?suse_version}
Requires:       python3-PyYAML
# Suse splits this off into a separate package
Requires:       python3-curses
BuildRequires:  fdupes
BuildRequires:  python3-curses
%endif

%if 0%{?fedora_version}
Requires:       PyYAML
%endif

# Required for core functionality
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  python3

%if 0%{?suse_version} > 1210
# xsltproc is necessary for manpage generation; this is split out into
# libxslt-tools as of openSUSE 12.2.  Possibly strictly should be
# required by asciidoc
BuildRequires:  libxslt-tools
%endif

%if 0%{?suse_version} > 1110 || 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?rhel} || 0%{?fedora}
BuildArch:      noarch
%endif

%description
The crm shell is a command-line interface for High-Availability
cluster management on GNU/Linux systems. It simplifies the
configuration, management and troubleshooting of Pacemaker-based
clusters, by providing a powerful and intuitive set of features.

%package test
Summary:        Test package for crmsh
Group:          %{pkg_group}
Requires:       crmsh
%if %{with regression_tests}
Requires(post):  mailx
Requires(post):  procps
Requires(post):  python3-python-dateutil
Requires(post):  python3-tox
Requires(post):  python3-parallax
Requires(post):  pacemaker
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif
%if 0%{?suse_version}
Requires(post):  libglue-devel
%else
Requires(post):  cluster-glue-libs-devel
%endif
%if 0%{?fedora_version}
Requires(post):  PyYAML
%else
Requires(post):  python3-PyYAML
%endif
%endif

%description test
The crm shell is a command-line interface for High-Availability
cluster management on GNU/Linux systems. It simplifies the
configuration, management and troubleshooting of Pacemaker-based
clusters, by providing a powerful and intuitive set of features.
This package contains the regression test suite for crmsh.

%package scripts
Summary:        Crm Shell Cluster Scripts
Group:          Productivity/Clustering/HA

%description scripts
Cluster scripts for crmsh. The cluster scripts can be run
directly from the crm command line, or used by user interfaces
like hawk to implement configuration wizards.

%prep
%setup -q

# replace the shebang in all the scripts
# with ${_bindir}/python3
find . -type f -exec perl -pi -e 'BEGIN{undef $/};s[^#\!/usr/bin/python[3]?][#\!%{_bindir}/python3]' {} \;
find . -type f -exec perl -pi -e 'BEGIN{undef $/};s[^#\!/usr/bin/env python[3]?][#\!%{_bindir}/python3]' {} \;

%build
./autogen.sh

%{configure}            \
    --sysconfdir=%{_sysconfdir} \
    --localstatedir=%{_var}             \
    --with-version=%{version}    \
    --docdir=%{crmsh_docdir}

make %{_smp_mflags} VERSION="%{version}" sysconfdir=%{_sysconfdir} localstatedir=%{_var}

%if %{with regression_tests}
tox
if [ ! $? ]; then
    echo "Unit tests failed."
    exit 1
fi
%endif

%install
make DESTDIR=%{buildroot} docdir=%{crmsh_docdir} install
install -Dm0644 contrib/bash_completion.sh %{buildroot}%{_datadir}/bash-completion/completions/crm
if [ -f %{buildroot}%{_bindir}/crm ]; then
	install -Dm0755 %{buildroot}%{_bindir}/crm %{buildroot}%{_sbindir}/crm
	rm %{buildroot}%{_bindir}/crm
fi
%if 0%{?suse_version}
%fdupes %{buildroot}
%endif

%if %{with regression_tests}
# Run regression tests after installing the package
# NB: this is called twice by OBS, that's why we touch the file
%post test
testfile=`mktemp -t .crmsh_regression_tests_ran_XXXXXX`
# check if time in file is less than 2 minutes ago
if [ -e $testfile ] && [ "$(( $(date +%s) - $(cat $testfile) ))" -lt 120 ]; then
	echo "Skipping regression tests..."
	exit 0
fi
# write current time to file
rm -f "$testfile"
echo "$(date +%s)" > "$testfile"
%{_datadir}/%{name}/tests/regression.sh
result1=$?
cd %{_datadir}/%{name}/tests
./cib-tests.sh
result2=$?
[ $result1 -ne 0 ] && (echo "Regression tests failed."; cat ${buildroot}/crmtestout/regression.out)
[ $result2 -ne 0 ] && echo "CIB tests failed."
[ $result1 -eq 0 -a $result2 -eq 0 ]
%endif

%files
###########################################################
%defattr(-,root,root)

%{_sbindir}/crm
%{python3_sitelib}/crmsh*

%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/tests
%exclude %{_datadir}/%{name}/scripts

%doc %{_mandir}/man8/*
%{crmsh_docdir}/COPYING
%{crmsh_docdir}/AUTHORS
%{crmsh_docdir}/crm.8.html
%{crmsh_docdir}/crmsh_hb_report.8.html
%{crmsh_docdir}/ChangeLog
%{crmsh_docdir}/README.md
%{crmsh_docdir}/contrib/*

%config %{_sysconfdir}/crm

%dir %{crmsh_docdir}
%dir %{crmsh_docdir}/contrib
%dir %attr (770, %{uname}, %{gname}) %{_var}/cache/crm
%dir %attr (770, %{uname}, %{gname}) %{_var}/log/crmsh
%{_datadir}/bash-completion/completions/crm

%files scripts
%defattr(-,root,root)
%{_datadir}/%{name}/scripts

%files test
%defattr(-,root,root)
%{_datadir}/%{name}/tests

%changelog
