# at-spi2-atk is used by gtk-3.0, gtk-3.0 is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api	2.0
%define	major	0
%define	libname	%mklibname atk-bridge %{api} %{major}
%define	devname	%mklibname atk-bridge -d
%define	lib32name	%mklib32name atk-bridge %{api} %{major}
%define	dev32name	%mklib32name atk-bridge -d

%bcond_with	crosscompile

Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Name:		at-spi2-atk
Version:	2.38.0
Release:	3
Group:		System/Libraries
License:	LGPLv2.1+
Url:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:	https://download.gnome.org/sources/at-spi2-atk/%url_ver/%{name}-%{version}.tar.xz
Source100:	at-spi2-atk.rpmlintrc

BuildRequires:  meson
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(atspi-2)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(glib-2.0)
Requires:       at-spi2-core

%if %{with compat32}
BuildRequires:	devel(libatk-1.0)
BuildRequires:	devel(libxml2)
BuildRequires:	devel(libatspi)
BuildRequires:	devel(libdbus-1)
BuildRequires:	devel(libglib-2.0)
BuildRequires:	devel(libz)
BuildRequires:	devel(libffi)
%endif

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

%if %{with compat32}
%package -n %{lib32name}
Summary:	Main library for %{name} (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
This package contains the library for %{name}.

%package -n %{dev32name}
Summary:	A GTK+ module that bridges ATK to D-Bus at-spi (32-bit)
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
This package includes the development libraries and header files 
for %{name}.
%endif

%prep
%autosetup -p1
%if %{with compat32}
%meson32
%endif
%meson

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%meson_build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%meson_install

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

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libatk-bridge-%{api}.so.%{major}*
%{_prefix}/lib/gtk-2.0/modules/libatk-bridge.so
%{_prefix}/lib/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop

%files -n %{dev32name}
%{_prefix}/lib/libatk-bridge-%{api}.so
%{_prefix}/lib/pkgconfig/atk-bridge-%{api}.pc
%endif
