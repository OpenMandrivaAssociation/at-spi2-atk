Name:           at-spi2-atk
Version:        2.0.0
Release:        %mkrel 1
Summary:        A GTK+ module that bridges ATK to D-Bus at-spi

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  at-spi2-core-devel
BuildRequires:  dbus-devel
BuildRequires:	glib2-devel
BuildRequires:  atk-devel
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

%build
%configure2_5x --disable-rpath
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std

rm -f %buildroot%_libdir/*/modules/*.la

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS README
%_libdir/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop
%_libdir/gtk-2.0/modules/libatk-bridge.so
%_libdir/gtk-3.0/modules/libatk-bridge.so
%_datadir/glib-2.0/schemas/org.a11y.atspi.gschema.xml
