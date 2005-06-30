
# TODO:
# - If you have any idea how to PLDize this program, do it:)
# - in first run eagle.key should be writable for user
# - add manual and tutorial to doc
# - add shortcut? to binary file 
# - Is banner in rpm needed to introduce how to run it?

Summary:	Eagle Layout Editor
Summary(pl):	Edytor p³ytek drukowanych Eagle
Name:		eagle-light
Version:	4.15
Release:	0.1
License:	Freeware
Group:		X11/Applications/Science
Source0:	ftp://ftp.cadsoft.de/pub/program/%{version}/eagle-lin-eng-%{version}.tgz
# Source0-md5:	b9a3ec50033785903cfccba86de0b367
Source1:	ftp://ftp.cadsoft.de/pub/program/%{version}/manual-eng.pdf
# Source1-md5:	1e85f214b4229023ec22167ee8c6b485
Source2:	ftp://ftp.cadsoft.de/pub/program/%{version}/tutorial-eng.pdf
# Source2-md5:	9ed24f9106432f237d3991c291d95b04
Source3:        %{name}.desktop
URL:		http://www.cadsoft.de/freeware.htm/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _eagledir %{_libdir}/%{name}-%{version}

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
cp -f %{SOURCE1} %{SOURCE2} doc/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eagledir}/{bin,cam,dru,lbr,projects/examples/{hexapod,singlesided,tutorial},scr,ulp} \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_bindir}  \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_desktopdir}

install man/eagle.1 $RPM_BUILD_ROOT%{_mandir}/man1
install bin/eagle $RPM_BUILD_ROOT%{_eagledir}/bin
install bin/eagle.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install bin/{eagle.def,freeware.key} $RPM_BUILD_ROOT%{_eagledir}/bin
touch $RPM_BUILD_ROOT%{_eagledir}/bin/eagle.key
install cam/* $RPM_BUILD_ROOT%{_eagledir}/cam
install dru/* $RPM_BUILD_ROOT%{_eagledir}/dru
install lbr/* $RPM_BUILD_ROOT%{_eagledir}/lbr
install projects/DESCRIPTION $RPM_BUILD_ROOT%{_eagledir}/projects
install projects/examples/hexapod/* $RPM_BUILD_ROOT%{_eagledir}/projects/examples/hexapod
install projects/examples/singlesided/* $RPM_BUILD_ROOT%{_eagledir}/projects/examples/singlesided
install projects/examples/tutorial/* $RPM_BUILD_ROOT%{_eagledir}/projects/examples/tutorial
install scr/* $RPM_BUILD_ROOT%{_eagledir}/scr
install ulp/* $RPM_BUILD_ROOT%{_eagledir}/ulp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/UPDATE doc/library.txt README
%{_mandir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
%attr(755,root,root) %{_eagledir}/bin/eagle
# I'm not sure that eagle.key should have 665 atributies
#%attr(665,root,users)
%{_eagledir}/bin/eagle.key
%{_eagledir}/bin/freeware.key
%{_eagledir}/bin/eagle.def
# - all files shuld be in folders ../ to eagle binary. Stupid :/
%{_eagledir}/cam
%{_eagledir}/dru
%{_eagledir}/lbr
%{_eagledir}/projects
%{_eagledir}/scr
%{_eagledir}/ulp
