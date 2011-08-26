%define name talpo
%define version 0.0.20110826git3ca28e0

%define _meltsources %(gcc -print-file-name=plugin/melt-sources)
%define _meltmodules %(gcc -print-file-name=plugin/melt-modules)

Name:		%{name}
Version:	%{version}
Release:	3
License:	GPLv3
Summary:	Talpo is GCC MELT user-programmable checker
Group:		Development/C
URL:		https://gitorious.org/%{name}/%{name}
Source0:	%{name}-%{version}.tar.bz2
Patch0:	0001-Install-modlis-files.patch
Patch1:	0002-Adding-usr-bin-talpo-wrapper.patch
Patch2:	0003-Fix-talpo-wrapper-arguments-handling.patch
Patch3:	0004-Backport-read_strv.patch
Patch4:	0005-Changes-for-MELT-0.9.patch

Requires:	%{name}-sources
Requires:	%{name}-modules
Requires:	gccmelt
BuildRequires:	gccmelt
## Needed because BuildRequires of gccmelt won't get installed
## inside the building chroot
BuildRequires:	gcc-plugin-devel
BuildRequires:	gmp-devel
BuildRequires:	ppl-devel
BuildRequires:	ppl_c-devel
BuildRequires:	mpfr-devel
BuildRequires:	libmpc-devel

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
This package contains Talpo's MELT sources files.

%package modules
Summary:	Talpo's MELT modules
Suggests:	gccmelt

%description modules
This package contains Talpo's MELT modules files.

%package doc
Summary:	Talpo's Documentation
Suggests:	gccmelt
BuildArch:	noarch

%description doc
This package provides Talpo's documentation

%files
%{_bindir}/talpo

%files sources
%{_meltsources}/*.melt
%{_meltsources}/*.c

%files modules
%{_meltmodules}/*.so
%{_meltmodules}/*.modlis

%files doc
%doc README AdvancedREADME
%{_docdir}/%{name}-doc/examples/

%prep
%setup -q

%apply_patches

%build
# disable make -j for now
# must have a new melt-module.mk which disables -j system wide before re-enabling here.
make -f Makefile-plugin CC=gcc

%install

pushd examples
for f in $(find . -type f); do
	%{__install} -m644 -D $f %{buildroot}%{_docdir}/%{name}-doc/examples/$f
done;
popd

%makeinstall_std -f Makefile-plugin PREFIX=%{_prefix}/

%clean
rm -fr %{buildroot}
