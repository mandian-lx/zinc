%{?_javapackages_macros:%_javapackages_macros}

Name:           zinc
Version:        0.3.1
Release:        4.1
Summary:        Incremental scala compiler
Group:		Development/Java
License:        ASL 2.0
URL:            https://github.com/typesafehub/zinc
BuildArch:      noarch

Source0:        https://github.com/typesafehub/zinc/archive/v%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/com/typesafe/zinc/zinc/%{version}/zinc-%{version}.pom
# ASL mandates that the licence file be included in redistributed source
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt

# Patch fixes compilation failure, which is probably caused by
# incompatible Scala version
Patch0:         0001-Fix-file-filtering.patch

BuildRequires:  javapackages-local
BuildRequires:  mvn(org.scala-lang:scala-library)
BuildRequires:  mvn(org.scala-sbt:incremental-compiler)
BuildRequires:  mvn(com.martiansoftware:nailgun-server)

%description
Zinc is a stand-alone version of sbt's incremental compiler.

%prep
%setup -q
rm -rf src/scriptit dist nailgun project

%patch0 -p1

cp %{SOURCE1} pom.xml
cp %{SOURCE2} LICENSE.txt

%pom_xpath_remove "pom:dependency[pom:classifier='sources']"
%pom_change_dep :incremental-compiler org.scala-sbt:

%build
scalac -cp $(build-classpath sbt nailgun) src/main/scala/com/typesafe/zinc/*
jar cf zinc.jar com
%mvn_artifact pom.xml zinc.jar

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE.txt

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.1-1
- Initial packaging

