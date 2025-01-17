#
# spec file for package xstream
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2007, JPackage Project
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


%bcond_with  hibernate
Name:           xstream
Version:        1.4.9
Release:        0
Summary:        Java XML serialization library
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://x-stream.github.io/
Source0:        http://repo1.maven.org/maven2/com/thoughtworks/%{name}/%{name}-distribution/%{version}/%{name}-distribution-%{version}-src.zip
# Fixes deserialization of void
# https://bugzilla.redhat.com/show_bug.cgi?id=1441542
# backport of https://github.com/x-stream/xstream/commit/b3570be2f39234e61f99f9a20640756ea71b1b40
Patch0:         0001-Prevent-deserialization-of-void.patch
Patch1:         xstream-1.4.9-javadoc.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(javassist:javassist)
BuildRequires:  mvn(joda-time:joda-time)
BuildRequires:  mvn(net.sf.kxml:kxml2)
BuildRequires:  mvn(net.sf.kxml:kxml2-min)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.jettison:jettison)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(org.jdom:jdom)
BuildRequires:  mvn(org.jdom:jdom2)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(stax:stax)
BuildRequires:  mvn(stax:stax-api)
BuildRequires:  mvn(xom:xom)
BuildRequires:  mvn(xpp3:xpp3)
BuildRequires:  mvn(xpp3:xpp3_min)
BuildRequires:  unzip
BuildArch:      noarch
%if %{with hibernate}
BuildRequires:  mvn(org.hibernate:hibernate-core)
BuildRequires:  mvn(org.hibernate:hibernate-envers)
%endif

%description
XStream is a simple library to serialize objects to XML
and back again. A high level facade is supplied that
simplifies common use cases. Custom objects can be serialized
without need for specifying mappings. Speed and low memory
footprint are a crucial part of the design, making it suitable
for large object graphs or systems with high message throughput.
No information is duplicated that can be obtained via reflection.
This results in XML that is easier to read for humans and more
compact than native Java serialization. XStream serializes internal
fields, including private and final. Supports non-public and inner
classes. Classes are not required to have default constructor.
Duplicate references encountered in the object-model will be
maintained. Supports circular references. By implementing an
interface, XStream can serialize directly to/from any tree
structure (not just XML). Strategies can be registered allowing
customization of how particular types are represented as XML.
When an exception occurs due to malformed XML, detailed diagnostics
are provided to help isolate and fix the problem.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description    javadoc
%{name} API documentation.

%if %{with hibernate}
%package        hibernate
Summary:        The hibernate module for %{name}
Requires:       %{name} = %{version}-%{release}

%description    hibernate
This package contains the hibernate module for %{name}.
%endif

%package        benchmark
Summary:        The benchmark module for %{name}
Requires:       %{name} = %{version}-%{release}

%description    benchmark
This package contains the benchmark module for %{name}.

%package parent
Summary:        Parent POM for %{name}
Requires:       %{name} = %{version}-%{release}

%description parent
Parent POM for %{name}.

%prep
%setup -q
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%patch0 -p1
%patch1 -p1

# Remove org.apache.maven.wagon:wagon-webdav
%pom_xpath_remove "pom:project/pom:build/pom:extensions"
# Require org.codehaus.xsite:xsite-maven-plugin
%pom_disable_module xstream-distribution

# missing artifacts:
#  org.openjdk.jmh:jmh-core:jar:1.11.1
#  org.openjdk.jmh:jmh-generator-annprocess:jar:1.11.1
%pom_disable_module xstream-jmh

%pom_remove_plugin :xsite-maven-plugin
%pom_remove_plugin :jxr-maven-plugin
# Unwanted
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-eclipse-plugin
%pom_remove_plugin :maven-release-plugin

%pom_xpath_set "pom:dependency[pom:groupId = 'org.codehaus.woodstox' ]/pom:artifactId" woodstox-core-asl
%pom_xpath_set "pom:dependency[pom:groupId = 'org.codehaus.woodstox' ]/pom:artifactId" woodstox-core-asl xstream
%pom_xpath_set "pom:dependency[pom:groupId = 'cglib' ]/pom:artifactId" cglib
%pom_xpath_set "pom:dependency[pom:groupId = 'cglib' ]/pom:artifactId" cglib xstream
# Replace old xmlpull dependency with xpp3
%pom_change_dep :xmlpull xpp3:xpp3:1.1.4c xstream
# Require unavailable proxytoys:proxytoys
%pom_remove_plugin :maven-dependency-plugin xstream

# provided by JDK
%pom_remove_dep javax.activation:activation xstream

%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'cglib' ]/pom:artifactId" cglib xstream-hibernate
%pom_xpath_inject "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'junit' ]" "<scope>test</scope>" xstream-hibernate
%pom_remove_plugin :maven-dependency-plugin xstream-hibernate

%pom_xpath_inject "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'junit' ]" "<scope>test</scope>" xstream-benchmark

%if %{without hibernate}
%pom_disable_module xstream-hibernate
%endif

%{mvn_file} :%{name} %{name}/%{name} %{name}
%{mvn_file} :%{name}-benchmark %{name}/%{name}-benchmark %{name}-benchmark

%{mvn_package} :%{name}

%build
# test skipped for unavailable test deps (com.megginson.sax:xml-writer)
%{mvn_build} -f -s -- -Dsource=1.6

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%doc README.txt
%dir %{_javadir}/%{name}

%files parent -f .mfiles-%{name}-parent
%if %{with hibernate}
%files hibernate -f .mfiles-%{name}-hibernate
%endif

%files benchmark -f .mfiles-%{name}-benchmark

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
