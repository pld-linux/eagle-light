
# TODO:
# - freeware.key should be in this same directory as eagle binary
# - add libraries from homepage
# - enhance description

%define		_ver	4.13r1
Summary:	Eagle Layout Editor
Summary(pl):	Edytor p³ytek drukowanych Eagle
Name:		eagle-light
Version:	4.13r1
Release:	0.1
License:	Freeware
Group:		X11/Applications/Science
Source0:	ftp://ftp.cadsoft.de/pub/program/%{_ver}/eagle-lin-eng-%{_ver}.tgz
# Source0-md5:	c9607298d0c7ca1545397f996d14c1e8
Source1:	%{name}.desktop
URL:		http://www.cadsoft.de/freeware.htm/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eagle Layout Editor. Limitations:
- The useable board area is limited to 100 x 80 mm (4 x 3.2 inches).
- Only two signal layers can be used (Top and Bottom).
- The schematic editor can only create one sheet.

%description -l pl
Edytor p³ytek drukowanych Eagle Limity:
- Obszar p³ytki jest ograniczony do 100 x 80 mm (4 x 3.2 cale)
- Tylko dwa sygna³owe warstwy mog± byæ u¿ywane (wierzchnia i spodnia)
- Edytor schematów mo¿e stworzyæ jeden arkusz
%prep
%setup -q -n eagle-lin-eng-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{bin,cam,lbr,projects/examples/{hexapod,singlesided,tutorial},scr,ulp} \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_desktopdir}
mv man/eagle.1 $RPM_BUILD_ROOT%{_mandir}/man1
mv bin/eagle $RPM_BUILD_ROOT%{_bindir}/eagle
mv bin/eagle.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
install cam/* $RPM_BUILD_ROOT%{_datadir}/%{name}/cam
install lbr/* $RPM_BUILD_ROOT%{_datadir}/%{name}/lbr
install projects/DESCRIPTION $RPM_BUILD_ROOT%{_datadir}/%{name}/projects
install projects/examples/hexapod/* $RPM_BUILD_ROOT%{_datadir}/%{name}/projects/examples/hexapod
install projects/examples/singlesided/* $RPM_BUILD_ROOT%{_datadir}/%{name}/projects/examples/singlesided
install projects/examples/tutorial/* $RPM_BUILD_ROOT%{_datadir}/%{name}/projects/examples/tutorial
install scr/* $RPM_BUILD_ROOT%{_datadir}/%{name}/scr
install ulp/* $RPM_BUILD_ROOT%{_datadir}/%{name}/ulp

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if ! grep -qs '^%{_libdir}/%{name}$' /etc/ld.so.conf ; then
	echo "%{_libdir}/%{name}" >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun
umask 022
if [ "$1" = '0' ]; then
	grep -v '^%{_libdir}/%{name}$' /etc/ld.so.conf > /etc/ld.so.conf.new 2>/dev/null
	mv -f /etc/ld.so.conf.new /etc/ld.so.conf
fi
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/UPDATE doc/library.txt README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/
