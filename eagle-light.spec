
# TODO:
# - If you have any idea how to PLDize this program, do it:)
# - in first run eagle.key should be writable for user or use 
#   sudo /usr/lib/eagle-light/bin/eagle to change license
# - Is banner in rpm needed to introduce how to run it?

Summary:	Eagle Layout Editor
Summary(pl.UTF-8):	Edytor płytek drukowanych Eagle
Name:		eagle-light
Version:	7.7.0
Release:	1
License:	Freeware
Group:		X11/Applications/Science
Source0:	ftp://ftp.cadsoft.de/eagle/program/latest/eagle-lin32-%{version}.run
# Source0-md5:	2538a6e89825e7f17a475c139772e92a
Source1:        ftp://ftp.cadsoft.de/eagle/program/latest/eagle-lin64-%{version}.run
# Source1-md5:	32af1a9e3af2a95121dc332a520e9486
Source2:	ftp://ftp.cadsoft.de/eagle/program/latest/elektro-tutorial.pdf
# Source2-md5:	4454bfbf5b6137d3bfb47a4cefde0630
Source3:        %{name}.desktop
URL:		http://www.cadsoft.de/freeware.htm
ExclusiveArch:	%{ix86} %{x8664}
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
%ifarch %{ix86}
SOURCE=%{S:0}
sh %{SOURCE0} `pwd`
%endif
%ifarch %{x8664}
SOURCE=%{s:1}
sh %{SOURCE1} `pwd`
%endif

mv -f eagle-%{version}/* .
rm -rf eagle-%{version}

cp -f %{SOURCE2} doc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_eagledir}/{bin,cam,dru,lbr,projects,scr,ulp,bin/icons,doc} \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_desktopdir}

cp -af doc/eagle.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -af bin/eagle $RPM_BUILD_ROOT%{_eagledir}/bin
cp -af bin/eagleicon50.png $RPM_BUILD_ROOT%{_pixmapsdir}/eagle.png
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
%ifarch %{x8664}
sed -i 's#/usr/lib/#/usr/lib64/#' $RPM_BUILD_ROOT%{_desktopdir}/*.desktop
%endifi
# some doc files must be in bin dir because eagle use them internally
cp -af bin/{eagle.def,freeware.key,*.png,*.qm,*.htm} $RPM_BUILD_ROOT%{_eagledir}/bin
touch $RPM_BUILD_ROOT%{_eagledir}/bin/eagle.key
cp -arf cam/* $RPM_BUILD_ROOT%{_eagledir}/cam
cp -arf dru/* $RPM_BUILD_ROOT%{_eagledir}/dru
cp -arf lbr/* $RPM_BUILD_ROOT%{_eagledir}/lbr
cp -arf projects/* $RPM_BUILD_ROOT%{_eagledir}/projects
cp -arf scr/* $RPM_BUILD_ROOT%{_eagledir}/scr
cp -arf ulp/* $RPM_BUILD_ROOT%{_eagledir}/ulp
# copy icons
cp -arf bin/icons/* $RPM_BUILD_ROOT%{_eagledir}/bin/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/UPDATE_* doc/README_* doc/library_*.txt doc/*.pdf doc/ulp/*.pdf
%{_mandir}/*
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%dir %{_eagledir}
%dir %{_eagledir}/bin
%dir %{_eagledir}/bin/icons
%attr(755,root,root) %{_eagledir}/bin/eagle
# I'm not sure that eagle.key should have 665 atributtes
#%attr(665,root,users)
%{_eagledir}/bin/eagle.key
%{_eagledir}/bin/freeware.key
%{_eagledir}/bin/eagle.def
%{_eagledir}/bin/*.png
%{_eagledir}/bin/*.htm
%lang(de) %{_eagledir}/bin/*_de.qm
%lang(hu) %{_eagledir}/bin/*_hu.qm
%lang(ru) %{_eagledir}/bin/*_ru.qm
%lang(zh) %{_eagledir}/bin/*_zh*.qm
# - all files should be in folders ../ to eagle binary. Stupid :/
%{_eagledir}/cam
%{_eagledir}/dru
%{_eagledir}/lbr
%{_eagledir}/projects
%{_eagledir}/scr
%{_eagledir}/ulp
%{_eagledir}/doc
%{_eagledir}/bin/icons/*.svg

