%define name talpo
%define version 0.0.20110805.5gitbe6de7d

%define _meltsources %(gcc -print-file-name=plugin/melt-source)
%define _meltmodules %(gcc -print-file-name=plugin/melt-modules)

Name:		%{name}
Version:	%{version}
Release:	1
License:	GPLv3
Summary:	Talpo is GCC MELT user-programmable checker
Group:		Development/C
URL:		https://gitorious.org/%{name}/%{name}
Source0:	%{name}-%{version}.tar.bz2
Requires:	%{name}-sources
Requires:	%{name}-modules
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
This packages contains Talpo's MELT sources files.

%package modules
Summary:	Talpo's MELT modules
Suggests:	gccmelt

%description modules
This packages contains Talpo's MELT modules files.

%files
%doc README

%files sources
%{_meltsources}/*.melt
%{_meltsources}/*.c

%files modules
%{_meltmodules}/*.so

%prep
%setup -q

%build
# disable make -j for now
# must have a new melt-module.mk which disables -j system wide before re-enabling here.
make -f Makefile-plugin CC=gcc

%install
%makeinstall_std -f Makefile-plugin PREFIX=%{_prefix}/

%clean
rm -fr %{buildroot}
