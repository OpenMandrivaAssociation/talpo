%define name talpo
%define version 0.0.20110803

Name:		%{name}
Version:	%{version}
Release:	1
License:	GPLv3
Summary:	Talpo is GCC MELT user-programmable checker
Group:		Development/C
URL:		https://gitorious.org/%{name}/%{name}
Source0:	%{name}-%{version}.tar.bz2
Requires:	gccmelt
BuildRequires:	gccmelt

%description
GCC MELT is a GCC plugin providing a lispy domain specific
language to easily code GCC extensions in.

Talpo is such of one of theses extensions, aiming at providing
compile-time complex and easy-to-use checking.

%package sources
Summary:	Talpo's MELT sources
Suggests:	gccmelt
BuildArch:	noarch

%description sources
This packages contains Talpo's MELT sources files, if you want
or need to have a look at it.

%files
%doc README

%files sources
%{_datadir}/gcc-melt/%{name}/*.melt

%prep
%setup -q

%build
%make -f Makefile-plugin

%install
%makeinstall_std PREFIX=%{_prefix}/

%clean
rm -fr %{buildroot}
