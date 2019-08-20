#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-codehaus-jackson
Version  : 1.9.2
Release  : 5
URL      : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-core-asl/1.9.2/jackson-core-asl-1.9.2.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-core-asl/1.9.2/jackson-core-asl-1.9.2.jar
Source1  : https://repo.maven.apache.org/maven2/org/codehaus/jackson/jackson-core-asl/1.0.1/jackson-core-asl-1.0.1.jar
Source2  : https://repo.maven.apache.org/maven2/org/codehaus/jackson/jackson-core-asl/1.0.1/jackson-core-asl-1.0.1.pom
Source3  : https://repo.maven.apache.org/maven2/org/codehaus/jackson/jackson-mapper-asl/1.0.1/jackson-mapper-asl-1.0.1.jar
Source4  : https://repo.maven.apache.org/maven2/org/codehaus/jackson/jackson-mapper-asl/1.0.1/jackson-mapper-asl-1.0.1.pom
Source5  : https://repo.maven.apache.org/maven2/org/codehaus/jackson/jackson-mapper-asl/1.9.13/jackson-mapper-asl-1.9.13.jar
Source6  : https://repo.maven.apache.org/maven2/org/codehaus/jackson/jackson-mapper-asl/1.9.13/jackson-mapper-asl-1.9.13.pom
Source7  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-core-asl/1.1.1/jackson-core-asl-1.1.1.jar
Source8  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-core-asl/1.1.1/jackson-core-asl-1.1.1.pom
Source9  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-core-asl/1.9.13/jackson-core-asl-1.9.13.jar
Source10  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-core-asl/1.9.13/jackson-core-asl-1.9.13.pom
Source11  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-core-asl/1.9.2/jackson-core-asl-1.9.2.pom
Source12  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-jaxrs/1.9.13/jackson-jaxrs-1.9.13.jar
Source13  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-jaxrs/1.9.13/jackson-jaxrs-1.9.13.pom
Source14  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-jaxrs/1.9.2/jackson-jaxrs-1.9.2.jar
Source15  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-jaxrs/1.9.2/jackson-jaxrs-1.9.2.pom
Source16  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-mapper-asl/1.9.2/jackson-mapper-asl-1.9.2.jar
Source17  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-mapper-asl/1.9.2/jackson-mapper-asl-1.9.2.pom
Source18  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-xc/1.8.3/jackson-xc-1.8.3.jar
Source19  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-xc/1.8.3/jackson-xc-1.8.3.pom
Source20  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-xc/1.9.13/jackson-xc-1.9.13.jar
Source21  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-xc/1.9.13/jackson-xc-1.9.13.pom
Source22  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-xc/1.9.2/jackson-xc-1.9.2.jar
Source23  : https://repo1.maven.org/maven2/org/codehaus/jackson/jackson-xc/1.9.2/jackson-xc-1.9.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-codehaus-jackson-data = %{version}-%{release}
Requires: mvn-codehaus-jackson-license = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-codehaus-jackson package.
Group: Data

%description data
data components for the mvn-codehaus-jackson package.


%package license
Summary: license components for the mvn-codehaus-jackson package.
Group: Default

%description license
license components for the mvn-codehaus-jackson package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-codehaus-jackson
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-codehaus-jackson/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.2/jackson-core-asl-1.9.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.0.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.0.1/jackson-core-asl-1.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.0.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.0.1/jackson-core-asl-1.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.0.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.0.1/jackson-mapper-asl-1.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.0.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.0.1/jackson-mapper-asl-1.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.13
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.13/jackson-mapper-asl-1.9.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.13
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.13/jackson-mapper-asl-1.9.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.1.1
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.1.1/jackson-core-asl-1.1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.1.1
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.1.1/jackson-core-asl-1.1.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.13
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.13/jackson-core-asl-1.9.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.13
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.13/jackson-core-asl-1.9.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.2
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.2/jackson-core-asl-1.9.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.13
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.13/jackson-jaxrs-1.9.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.13
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.13/jackson-jaxrs-1.9.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.2
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.2/jackson-jaxrs-1.9.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.2
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.2/jackson-jaxrs-1.9.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.2
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.2/jackson-mapper-asl-1.9.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.2
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.2/jackson-mapper-asl-1.9.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.8.3
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.8.3/jackson-xc-1.8.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.8.3
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.8.3/jackson-xc-1.8.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.13
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.13/jackson-xc-1.9.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.13
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.13/jackson-xc-1.9.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.2
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.2/jackson-xc-1.9.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.2
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.2/jackson-xc-1.9.2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.0.1/jackson-core-asl-1.0.1.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.0.1/jackson-core-asl-1.0.1.pom
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.1.1/jackson-core-asl-1.1.1.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.1.1/jackson-core-asl-1.1.1.pom
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.13/jackson-core-asl-1.9.13.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.13/jackson-core-asl-1.9.13.pom
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.2/jackson-core-asl-1.9.2.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-core-asl/1.9.2/jackson-core-asl-1.9.2.pom
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.13/jackson-jaxrs-1.9.13.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.13/jackson-jaxrs-1.9.13.pom
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.2/jackson-jaxrs-1.9.2.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-jaxrs/1.9.2/jackson-jaxrs-1.9.2.pom
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.0.1/jackson-mapper-asl-1.0.1.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.0.1/jackson-mapper-asl-1.0.1.pom
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.13/jackson-mapper-asl-1.9.13.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.13/jackson-mapper-asl-1.9.13.pom
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.2/jackson-mapper-asl-1.9.2.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-mapper-asl/1.9.2/jackson-mapper-asl-1.9.2.pom
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.8.3/jackson-xc-1.8.3.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.8.3/jackson-xc-1.8.3.pom
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.13/jackson-xc-1.9.13.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.13/jackson-xc-1.9.13.pom
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.2/jackson-xc-1.9.2.jar
/usr/share/java/.m2/repository/org/codehaus/jackson/jackson-xc/1.9.2/jackson-xc-1.9.2.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-codehaus-jackson/LICENSE
