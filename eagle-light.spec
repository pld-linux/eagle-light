
# TODO:
# - fix %files
# - add libraries from homepage
# - enhance description

%define		_ver	4.13r1
Summary:	Eagle Layout Editor
Summary(pl):	Edytor p³ytek drukowanych Eagle
Name:		eagle-light
Version:	4.13r1
Release:	0.2
License:	Freeware
Group:		X11/Applications/Science
Source0:	ftp://ftp.cadsoft.de/pub/program/%{_ver}/eagle-lin-eng-%{_ver}.tgz
# Source0-md5:	c9607298d0c7ca1545397f996d14c1e8
Source1:	%{name}.desktop
URL:		http://www.cadsoft.de/freeware.htm/
# arch-dependent binaries MUST NOT be in /usr/share
BuildRequires:	FHS-fixes
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eagle Layout Editor. Limitations:
- The useable board area is limited to 100 x 80 mm (4 x 3.2 inches).
- Only two signal layers can be used (Top and Bottom).
- The schematic editor can only create one sheet.
To run Eagle, you need licence key. Freeware Licence key is in:
/usr/share/eagle-light/bin/

%description -l pl
Edytor p³ytek drukowanych Eagle. Ograniczenia:
- Obszar p³ytki jest ograniczony do 100 x 80 mm (4 x 3.2 cale)
- Tylko dwie sygna³owe warstwy mog± byæ u¿ywane (wierzchnia i spodnia)
- Edytor schematów mo¿e stworzyæ jeden arkusz
Aby uruchomic Eagle, potrzebny jest klucz licencyjny. Klucz licencyjny
Freeware znajduje siê w katalogu:
/usr/share/eagle-light/bin/

%prep
%setup -q -n eagle-lin-eng-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{bin,cam,dru,lbr,projects/examples/{hexapod,singlesided,tutorial},scr,ulp} \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_desktopdir}

install man/eagle.1 $RPM_BUILD_ROOT%{_mandir}/man1
#install bin/eagle $RPM_BUILD_ROOT%{_bindir}/eagle
install bin/eagle.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
ln -s %{_datadir}/%{name}/bin/eagle $RPM_BUILD_ROOT%{_bindir}/eagle
touch $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/eagle.key
install cam/* $RPM_BUILD_ROOT%{_datadir}/%{name}/cam
install dru/* $RPM_BUILD_ROOT%{_datadir}/%{name}/dru
install lbr/* $RPM_BUILD_ROOT%{_datadir}/%{name}/lbr
install projects/DESCRIPTION $RPM_BUILD_ROOT%{_datadir}/%{name}/projects
install projects/examples/hexapod/* $RPM_BUILD_ROOT%{_datadir}/%{name}/projects/examples/hexapod
install projects/examples/singlesided/* $RPM_BUILD_ROOT%{_datadir}/%{name}/projects/examples/singlesided
install projects/examples/tutorial/* $RPM_BUILD_ROOT%{_datadir}/%{name}/projects/examples/tutorial
install scr/* $RPM_BUILD_ROOT%{_datadir}/%{name}/scr
install ulp/* $RPM_BUILD_ROOT%{_datadir}/%{name}/ulp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/UPDATE doc/library.txt README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%{_datadir}/%{name}/bin/eagle.key
%attr(755,root,root) %{_datadir}/%{name}/bin/eagle
...the rest of file listing, not duplicates of previous entries!
