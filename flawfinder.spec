Name:		flawfinder
Summary:	Examines C/C++ source code for security flaws
Version:	0.20
Release:	1
License:	GPL
Group:		Development
Group(de):	Entwicklung
Group(es):	Desarrollo
Group(pl):	Programowanie
Group(pt_BR):	Desenvolvimento
Group(ru):	Разработка
Group(uk):	Розробка
Source0:	http://www.dwheeler.com/flawfinder/%{name}-%{version}.tar.gz
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flawfinder scans through C/C++ source code, finding potentially
dangerous code. It's released under the GNU Public License (GPL).

%prep
%setup -q 

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1
install -c flawfinder ${RPM_BUILD_ROOT}%{_bindir}/flawfinder
install -c flawfinder.1.gz ${RPM_BUILD_ROOT}%{_mandir}/man1/flawfinder.1.gz

gzip -9nf README ChangeLog COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,COPYING}.gz
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/flawfinder
