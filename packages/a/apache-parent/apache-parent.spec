#
# spec file for package apache-parent
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           apache-parent
Version:        21
Release:        0
Summary:        Parent POM file for Apache projects
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://apache.org/
Source0:        http://repo1.maven.org/maven2/org/apache/apache/%{version}/apache-%{version}-source-release.zip
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildArch:      noarch

%description
This package contains the parent pom file for apache projects.

%prep
%setup -q -n apache-%{version}

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :maven-enforcer-plugin

%install
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom

%files
%license LICENSE
%doc NOTICE
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%changelog
