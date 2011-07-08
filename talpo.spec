%define name talpo
%define version 0.0.20110708git6a72e12

Name:		%{name}
Version:	%{version}
Release:	1
License:	GPLv3
Summary:	Talpo is GCC MELT user-programmable checker
Group:		Development/C
URL:		https://gitorious.org/%{name}/%{name}
Source0:	%{name}-%{version}.tar.bz2
# [alex@portable-alex talpo (Mandriva)]$ git tag 0.0.$(date "+%Y%m%d")
# [alex@portable-alex talpo (Mandriva)]$ git tag -l
# 0.0.20110701
# [alex@portable-alex talpo (Mandriva)]$ git archive --format=tar --prefix=talpo-$(git describe --tags)git$(git describe --always)/ master | bzip2 > /home/alex/BuildSystem/talpo/SOURCES/talpo-$(git describe --tags)git$(git describe --always).tar.bz2
Requires:	gccmelt
BuildArch:	noarch

%description
GCC MELT is a GCC plugin providing a lispy domain specific
language to easily code GCC extensions in.

Talpo is such of one of theses extensions, aiming at providing
compile-time complex and easy-to-use checking.

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/gcc-melt/%{name}/*.melt

%prep
%setup -q

%build
# Nothing to do here

%install
%makeinstall_std PREFIX=%{_prefix}/

%clean
rm -fr %{buildroot}
