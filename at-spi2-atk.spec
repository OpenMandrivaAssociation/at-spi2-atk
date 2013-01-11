Name:		at-spi2-atk
Version:	2.6.2
Release:	3
Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.6/%{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(atspi-2)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(glib-2.0)

Requires:       at-spi2-core

%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

This package includes a gtk-module that bridges ATK to the new
D-Bus based at-spi.


%package devel
Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package includes the header files for
the %{name} library.

%prep
%setup -q

%build
%configure2_5x \
	--disable-rpath

%make

%install
%makeinstall_std
find %{buildroot} -name "*.la" -delete

%files
%doc COPYING AUTHORS README
%dir %{_libdir}/gtk-2.0
%dir %{_libdir}/gtk-2.0/modules
%{_libdir}/gtk-2.0/modules/libatk-bridge.so
%{_datadir}/glib-2.0/schemas/org.a11y.atspi.gschema.xml
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop
%{_libdir}/libatk-bridge-2.0.so.*

%files devel
%{_includedir}/at-spi2-atk/2.0/atk-bridge.h
%{_libdir}/libatk-bridge-2.0.so
%{_libdir}/pkgconfig/atk-bridge-2.0.pc

%changelog
* Tue Nov 13 2012 Arkady L. Shane <ashejn@rosalab.ru> 2.6.2-1
- update to 2.6.2

* Tue Oct 30 2012 Arkady L. Shane <ashejn@rosalab.ru> 2.6.1-1
- update to 2.6.1

* Fri Sep 28 2012 Arkady L. Shane <ashejn@rosalab.ru> 2.6.0-1
- update to 2.6.0

* Sun May 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.5.1-1
+ Revision: 797183
- verson update 2.5.1

* Sat Mar 10 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.2.2-1
+ Revision: 783908
- new version 2.2.2
- cleaned up spec

* Tue May 24 2011 Götz Waschk <waschk@mandriva.org> 2.0.2-1
+ Revision: 678053
- update to new version 2.0.2

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 2.0.1-1
+ Revision: 659144
- update to new version 2.0.1

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 2.0.0-1
+ Revision: 650484
- new version 2.0.0

* Tue Nov 16 2010 Götz Waschk <waschk@mandriva.org> 0.4.1-1mdv2011.0
+ Revision: 597897
- update to new version 0.4.1

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 581616
- update to new version 0.4.0

* Tue Sep 14 2010 Götz Waschk <waschk@mandriva.org> 0.3.92-1mdv2011.0
+ Revision: 578145
- update to new version 0.3.92

* Tue Aug 31 2010 Götz Waschk <waschk@mandriva.org> 0.3.91.1-1mdv2011.0
+ Revision: 574686
- update to new version 0.3.91.1

* Tue Aug 31 2010 Götz Waschk <waschk@mandriva.org> 0.3.91-1mdv2011.0
+ Revision: 574618
- new version
- drop patches

* Tue Aug 17 2010 Götz Waschk <waschk@mandriva.org> 0.3.90-1mdv2011.0
+ Revision: 570824
- update to new version 0.3.90

* Tue Aug 03 2010 Götz Waschk <waschk@mandriva.org> 0.3.6-1mdv2011.0
+ Revision: 565434
- update build deps
- new version
- fix source URL
- fix makefile

* Thu Jul 29 2010 Götz Waschk <waschk@mandriva.org> 0.3.5-1mdv2011.0
+ Revision: 563133
- update build deps
- new version
- update file list

* Wed Mar 31 2010 Götz Waschk <waschk@mandriva.org> 0.1.8-1mdv2010.1
+ Revision: 530227
- update to new version 0.1.8

* Fri Feb 19 2010 Götz Waschk <waschk@mandriva.org> 0.1.7-1mdv2010.1
+ Revision: 508297
- update to new version 0.1.7

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 0.1.6-1mdv2010.1
+ Revision: 502690
- update to new version 0.1.6

* Thu Jan 28 2010 Götz Waschk <waschk@mandriva.org> 0.1.5-1mdv2010.1
+ Revision: 497519
- import at-spi2-atk

