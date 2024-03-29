Summary: 	Yerase's TNEF Stream Reader
Name: 		ytnef
Epoch: 		1
Version: 	1.9.3
Release: 	3%{?dist}
License: 	GPLv2+
URL: 		https://github.com/Yeraze/ytnef
Source0: 	https://github.com/Yeraze/ytnef/archive/v%{version}/%{name}-%{version}.tar.gz
#Patch0:         ytnef-pkgconfig.patch
BuildRequires:  autoconf automake libtool
BuildRequires: 	perl-generators

%description
Yerase's TNEF Stream Reader.  Can take a TNEF Stream (winmail.dat) sent from
Microsoft Outlook (or similar products) and extract the attachments, including
construction of Contact Cards & Calendar entries.

%prep
%setup -q
./autogen.sh
#%patch0 -p1

%build
%configure --disable-static
V=1 %{__make} %{?_smp_mflags}

%install
%{__make}  install DESTDIR=$RPM_BUILD_ROOT includedir=%{_includedir}


%files
%license COPYING
%doc README.md ChangeLog ytnef/README.ytnefprocess
%{_bindir}/*
%doc lib/doc/recurrence.txt
%{_libdir}/*.so.*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/libytnef.la
%{_libdir}/pkgconfig/libytnef.pc

%changelog
* Fri Sep 17 2021 stephane de Labrusse <stephdl@de-labrusse.fr> - 1:1.9.3-3
- Rebuild to be compatible with the build of SOGo, the include dir path is 
- not expected by the sogo code. It expects to be at the root of /usr/include

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Kalev Lember <klember@redhat.com> - 1:1.9.3-1
- Update to 1.9.3 (#1683489)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Michael Schwendt <mschwendt@fedoraproject.org> - 1:1.9.2-5
- Spec fixes for modern guidelines:
  remove BuildRoot tag, remove Group tags, remove defattr, no clean section,
  automatic buildroot clean in install section, use license macro
- License is GPLv2+ / "GPL v2 (or later)".
- Verbose build.log with V=1
- Make base package deps arch-specific.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 28 2017 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 1:1.9.2-2
- include dir should be libytnef
- adjust pkgconfig

* Sat Mar 18 2017 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 1:1.9.2-1
- version upgrade
- fix cve rhbz#1431730
- merge ytnef/libytnef and add epoch

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.6-10
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 19 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.6-5
- fix location in ytnefprocess.pl

* Thu May 28 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.6-4
- fix perl requires

* Tue Mar 24 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.6-3
- Changed License to the same as libytnef-devel
- Macronify everything as possible.
- Included ChangeLog as part of the documentation.

* Fri Feb 13 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.6-2
- Rebuild for fedora 10

* Fri Mar 12 2004 Patrick <rpms@puzzled.xs4all.nl>
- Initial version
