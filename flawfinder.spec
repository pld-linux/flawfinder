%include	/usr/lib/rpm/macros.python
Summary:	Examines C/C++ source code for security flaws
Summary(pl):	Wyszukiwarka zagro¿eñ bezpieczeñstwa w kodzie C/C++
Name:		flawfinder
Version:	1.23
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.dwheeler.com/flawfinder/%{name}-%{version}.tar.gz
# Source0-md5:	f783cf53868b9f2479333e254409b79f
Patch0:		%{name}-python.patch
URL:		http://www.dwheeler.com/flawfinder/
BuildRequires:	rpm-pythonprov
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flawfinder scans through C/C++ source code, finding potentially
dangerous code. It's released under the GNU General Public License
(GPL).

%description -l pl
Flawfinder przeszukuje kod ¼ród³owy C/C++, znajduj±c potencjalnie
niebezpieczne fragmenty.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install flawfinder $RPM_BUILD_ROOT%{_bindir}
install flawfinder.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README flawfinder.pdf flaw-defect-report correct-results*
%attr(755,root,root) %{_bindir}/flawfinder
%{_mandir}/man1/*
