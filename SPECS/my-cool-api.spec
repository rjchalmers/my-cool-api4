
Name: my-cool-api
Version: 1.0.0
Release: 1%{?dist}
Group: Application/Web
License: Internal BBC use only
Summary: my-cool-api
Source0: src.tar.gz
Requires: express
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch



%description
my-cool-api built by the Spectacle

%prep
%setup -T -c spectacle

%build
mkdir -p %{_builddir}/src
tar -C %{_builddir}/src -xzf %{SOURCE0}

%install
mkdir -p %{buildroot}/usr/lib/my-app
cp -R --preserve=timestamps %{_builddir}/src/server.js %{buildroot}/usr/lib/my-app/server.js

%pre


%preun


%post


%postun


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
/usr/lib/my-app/server.js


