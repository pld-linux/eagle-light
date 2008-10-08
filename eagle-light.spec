
# TODO:
# - If you have any idea how to PLDize this program, do it:)
# - in first run eagle.key should be writable for user or use 
#   sudo /usr/lib/eagle-light/bin/eagle to change license
# - Is banner in rpm needed to introduce how to run it?

Summary:	Eagle Layout Editor
Summary(pl.UTF-8):	Edytor płytek drukowanych Eagle
Name:		eagle-light
Version:	5.0.0
Release:	0.8
License:	Freeware
Group:		X11/Applications/Science
Source0:	ftp://ftp.cadsoft.de/pub/program/5.0/eagle-lin-%{version}.run
# Source0-md5:	0a542e7187a0f8654a579e7c771cbb37
Source1:	ftp://ftp.cadsoft.de/pub/program/5.0/elektro-tutorial.pdf
# Source1-md5:	b17cf06236abf3057d27e0f883cdf4b2
Source2:        %{name}.desktop
URL:		http://www.cadsoft.de/freeware.htm
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _eagledir %{_libdir}/eagle-light
# binutils have problems to strip bin/eagle so need disable striping
%define no_install_post_strip 1

%description
Eagle Layout Editor. Limitations:
- The useable board area is limited to 100 x 80 mm (4 x 3.2 inches).
- Only two signal layers can be used (Top and Bottom).
- The schematic editor can only create one sheet.
To run Eagle, you need licence key. Freeware Licence key is in:
/usr/share/eagle-light/bin/

%description -l pl.UTF-8
Edytor płytek drukowanych Eagle. Ograniczenia:
- Obszar płytki jest ograniczony do 100 x 80 mm (4 x 3.2 cale)
- Tylko dwie sygnałowe warstwy mogą być używane (wierzchnia i spodnia)
- Edytor schematów może stworzyć jeden arkusz
Aby uruchomic Eagle, potrzebny jest klucz licencyjny. Klucz licencyjny
Freeware znajduje się w katalogu:
/usr/share/eagle-light/bin/

%prep
%setup -q -c -T

sh %{SOURCE0} `pwd`
mv -f eagle-%{version}/* .
rm -rf eagle-%{version}

cp -f %{SOURCE1} doc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_eagledir}/{bin,cam,dru,lbr,projects,scr,ulp} \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_desktopdir}

cp -af doc/eagle.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -af bin/eagle $RPM_BUILD_ROOT%{_eagledir}/bin
cp -af bin/eagleicon50.png $RPM_BUILD_ROOT%{_pixmapsdir}/eagle.png
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
# some doc files must be in bin dir because eagle use them internally
cp -af bin/{eagle.def,freeware.key,platforms-*.png,*.qm,*.htm} $RPM_BUILD_ROOT%{_eagledir}/bin
touch $RPM_BUILD_ROOT%{_eagledir}/bin/eagle.key
cp -arf cam/* $RPM_BUILD_ROOT%{_eagledir}/cam
cp -arf dru/* $RPM_BUILD_ROOT%{_eagledir}/dru
cp -arf lbr/* $RPM_BUILD_ROOT%{_eagledir}/lbr
cp -arf projects/* $RPM_BUILD_ROOT%{_eagledir}/projects
cp -arf scr/* $RPM_BUILD_ROOT%{_eagledir}/scr
cp -arf ulp/* $RPM_BUILD_ROOT%{_eagledir}/ulp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/UPDATE_* doc/README_* doc/library_*.txt doc/*.pdf
%{_mandir}/*
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%dir %{_eagledir}
%dir %{_eagledir}/bin
%attr(755,root,root) %{_eagledir}/bin/eagle
# I'm not sure that eagle.key should have 665 atributtes
#%attr(665,root,users)
%{_eagledir}/bin/eagle.key
%{_eagledir}/bin/freeware.key
%{_eagledir}/bin/eagle.def
%{_eagledir}/bin/*.png
%{_eagledir}/bin/*.htm
%lang(de) %{_eagledir}/bin/*_de.qm
# - all files should be in folders ../ to eagle binary. Stupid :/
%{_eagledir}/cam
%{_eagledir}/dru
%{_eagledir}/lbr
%{_eagledir}/projects
%{_eagledir}/scr
%{_eagledir}/ulp
