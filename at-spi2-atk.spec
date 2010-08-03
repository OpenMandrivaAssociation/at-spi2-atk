Name:           at-spi2-atk
Version:        0.3.6
Release:        %mkrel 1
Summary:        A GTK+ module that bridges ATK to D-Bus at-spi

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
#gw from Fedora: add mising desktop file
Patch0:		at-spi2-atk-fix-build.patch
Patch1:		at-spi2-atk-0.3.5-fix-makefile-tabs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  at-spi2-core
BuildRequires:  dbus-glib-devel
BuildRequires:  libxml2-devel
BuildRequires:  atk-devel
BuildRequires:  libGConf2-devel
BuildRequires:  libx11-devel
BuildRequires:  intltool

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


%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x --enable-relocate
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make


%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std

rm $RPM_BUILD_ROOT%{_libdir}/gtk-?.0/modules/at-spi-dbus/modules/libatk-bridge.la
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%preun
%preun_uninstall_gconf_schemas at-spi2

%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS README
%_sysconfdir/gconf/schemas/at-spi2.schemas
%{_libdir}/gtk-2.0/modules/at-spi-dbus/modules/libatk-bridge.so
%{_libdir}/gtk-3.0/modules/at-spi-dbus/modules/libatk-bridge.so
%dir %{_datadir}/gnome/autostart
%{_datadir}/gnome/autostart/atk-bridge.desktop

