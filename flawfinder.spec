Summary:	Examines C/C++ source code for security flaws
Summary(pl):	Wyszukiwarka zagroøeÒ bezpieczeÒstwa w kodzie C/C++
Name:		flawfinder
Version:	0.20
Release:	1
License:	GPL
Group:		Development
Group(de):	Entwicklung
Group(es):	Desarrollo
Group(pl):	Programowanie
Group(pt_BR):	Desenvolvimento
Group(ru):	Ú¡⁄“¡¬œ‘À¡
Group(uk):	Úœ⁄“œ¬À¡
Source0:	http://www.dwheeler.com/flawfinder/%{name}-%{version}.tar.gz
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flawfinder scans through C/C++ source code, finding potentially
dangerous code. It's released under the GNU Public License (GPL).

%description -l pl
Flawfinder przeszukuje kod ºrÛd≥owy C/C++, znajduj±c potencjalnie
niebezpieczne fragmenty.

%prep
%setup -q 

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}{%{_bindir},%{_mandir}/man1}

install flawfinder ${RPM_BUILD_ROOT}%{_bindir}/flawfinder
install flawfinder.1.gz ${RPM_BUILD_ROOT}%{_mandir}/man1/flawfinder.1.gz

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog}.gz
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/flawfinder
