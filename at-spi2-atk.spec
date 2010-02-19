Name:           at-spi2-atk
Version:        0.1.7
Release:        %mkrel 1
Summary:        A GTK+ module that bridges ATK to D-Bus at-spi

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:        http://download.gnome.org/sources/at-spi2-atk/0.1/%{name}-%{version}.tar.bz2
#gw from Fedora: add mising desktop file
Patch:		at-spi2-atk-fix-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  at-spi2-core
BuildRequires:  dbus-glib-devel
BuildRequires:  libxml2-devel
BuildRequires:  atk-devel
BuildRequires:  gtk2-devel

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
%patch -p1

%build
%configure2_5x --enable-relocate
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/at-spi-dbus/modules/libatk-bridge.la

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS README
%{_libdir}/gtk-2.0/modules/at-spi-dbus/modules/libatk-bridge.so
%dir %{_datadir}/gnome/autostart
%{_datadir}/gnome/autostart/atk-bridge.desktop

