%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api	2.0
%define	major	0
%define	libname	%mklibname atk-bridge %{api} %{major}
%define	devname	%mklibname atk-bridge -d

%bcond_with	crosscompile

Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Name:		at-spi2-atk
Version:	2.18.1
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:	https://download.gnome.org/sources/at-spi2-atk/%url_ver/%{name}-%{version}.tar.xz
Source100:	at-spi2-atk.rpmlintrc

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

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Conflicts:	%{name} < 2.6.2-5

%description -n %{libname}
This package contains the library for %{name}.

%package -n %{devname}
Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel
Obsoletes:	%{name}-devel

%description -n %{devname}
This package includes the development libraries and header files 
for %{name}.

%prep
%setup -q

%build
%if %{with crosscompile}
export ac_cv_alignof_char=1
export ac_cv_alignof_dbind_pointer=4
export ac_cv_alignof_dbind_struct=1
export ac_cv_alignof_dbus_bool_t=4
export ac_cv_alignof_dbus_int16_t=2
export ac_cv_alignof_dbus_int32_t=4
export ac_cv_alignof_dbus_int64_t=4
export ac_cv_alignof_double=4
%endif
%configure \
	--disable-rpath

%make

%install
%makeinstall_std

%files
%doc COPYING AUTHORS README
%dir %{_libdir}/gtk-2.0
%dir %{_libdir}/gtk-2.0/modules
%{_libdir}/gtk-2.0/modules/libatk-bridge.so
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop

%files -n %{libname}
%{_libdir}/libatk-bridge-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/at-spi2-atk/%{api}/atk-bridge.h
%{_libdir}/libatk-bridge-%{api}.so
%{_libdir}/pkgconfig/atk-bridge-%{api}.pc


