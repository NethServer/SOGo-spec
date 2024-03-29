%define sogo_version 5.10.0
%define sogo_release 1
%define sope_major_version 4
%define sope_minor_version 9

# We disable OpenChange builds since it's not maintained
%define enable_openchange 0

%{!?sogo_major_version: %global sogo_major_version %(/bin/echo %{sogo_version} | /bin/cut -f 1 -d .)}
%if %enable_openchange
%global oc_build_depends samba4 openchange
%endif

%{!?python_sys_pyver: %global python_sys_pyver %(/usr/bin/python -c "import sys; print (sys.hexversion)")}

# Systemd for fedora >= 17 or el 7
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
  %global _with_systemd 1
%else
  %global _with_systemd 0
%endif

%define sogo_user sogo

Summary:      SOGo
Name:         sogo
Version:      %{sogo_version}
Release:      %{sogo_release}%{?dist}
Vendor:       http://www.inverse.ca/
Packager:     Inverse inc. <info@inverse.ca>
License:      GPL
URL:          http://www.inverse.ca/contributions/sogo.html
Group:        Productivity/Groupware
Source:       https://github.com/inverse-inc/sogo/archive/SOGo-%{sogo_version}.tar.gz
Prefix:       /usr
AutoReqProv:  no
Requires:     gnustep-base >= 1.23, sope%{sope_major_version}%{sope_minor_version}-core, httpd, sope%{sope_major_version}%{sope_minor_version}-core, sope%{sope_major_version}%{sope_minor_version}-appserver, sope%{sope_major_version}%{sope_minor_version}-ldap, sope%{sope_major_version}%{sope_minor_version}-cards >= %{sogo_version}, sope%{sope_major_version}%{sope_minor_version}-gdl1-contentstore >= %{sogo_version}, sope%{sope_major_version}%{sope_minor_version}-sbjson, libmemcached, memcached, tmpwatch, libzip, ytnef = 1:1.9.3
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  gcc-objc gnustep-base gnustep-make gnustep-base-devel sope%{sope_major_version}%{sope_minor_version}-appserver-devel sope%{sope_major_version}%{sope_minor_version}-core-devel sope%{sope_major_version}%{sope_minor_version}-ldap-devel sope%{sope_major_version}%{sope_minor_version}-mime-devel sope%{sope_major_version}%{sope_minor_version}-xml-devel sope%{sope_major_version}%{sope_minor_version}-gdl1-devel sope%{sope_major_version}%{sope_minor_version}-sbjson-devel libmemcached-devel sed libcurl-devel openldap-devel %{?oc_build_depends} libzip-devel ytnef = 1:1.9.3


# Required by MS Exchange freebusy lookups
%{?el5:Requires: curl}
%{?el5:BuildRequires: curl-devel}
%{?el6:Requires: libcurl}
%{?el6:BuildRequires: libcurl-devel}

# saml is enabled everywhere except on el5 since its glib2 is prehistoric
%define saml2_cfg_opts "--enable-saml2"
%define mfa_cfg_opts "--enable-mfa"
%{?el5:%define saml2_cfg_opts ""}
%{?el5:%define mfa_cfg_opts ""}
%{?el6:%define mfa_cfg_opts ""}
%{?el6:Requires: lasso}
%{?el6:BuildRequires: lasso-devel}
%{?el7:Requires: lasso}
%{?el7:BuildRequires: lasso-devel}
%{?el7:Requires: liboath}
%{?el7:BuildRequires: liboath-devel}
%{?el8:Requires: lasso}
%{?el8:BuildRequires: lasso-devel}
%{?el8:Requires: liboath}
%{?el8:BuildRequires: liboath-devel}

%if 0%{?rhel} >= 7
Requires: libsodium
BuildRequires: libsodium-devel
%define sodium_cfg_opts "--enable-sodium"
%else
%define sodium_cfg_opts "--disable-sodium"
%endif

%description
SOGo is a groupware server built around OpenGroupware.org (OGo) and
the SOPE application server.  It focuses on scalability.

The Inverse edition of this project has many feature enhancements:
- CalDAV and GroupDAV compliance
- full handling of vCard as well as vCalendar/iCalendar formats
- support for folder sharing and ACLs

The Web interface has been rewritten in an AJAX fashion to provided a faster
UI for the users, consistency in look and feel with the Mozilla applications,
and to reduce the load of the transactions on the server.

%package -n sogo-tool
Summary:      Command-line toolsuite for SOGo
Group:        Productivity/Groupware
Requires:     sogo = %{sogo_version}
AutoReqProv:  no

%description -n sogo-tool
Administrative tool for SOGo that provides the following internal commands:
  backup          -- backup user folders
  restore         -- restore user folders
  remove-doubles  -- remove duplicate contacts from the user addressbooks
  check-doubles   -- list user addressbooks with duplicate contacts

%package -n sogo-slapd-sockd
Summary:      SOGo backend for slapd and back-sock
Group:        Productivity/Groupware
AutoReqProv:  no

%description -n sogo-slapd-sockd
SOGo backend for slapd and back-sock, enabling access to private addressbooks
via LDAP.

%package -n sogo-ealarms-notify
Summary:      SOGo utility for executing email alarms
Group:        Productivity/Groupware
AutoReqProv:  no

%description -n sogo-ealarms-notify
SOGo utility executed each minute via a cronjob for executing email alarms.

%package -n sogo-activesync
Summary:      SOGo module to handle ActiveSync requests
Group:        Productivity/Groupware
Requires:     libwbxml, sogo = %{sogo_version}
BuildRequires: libwbxml-devel
AutoReqProv:  no

%description -n sogo-activesync
SOGo module to handle ActiveSync requests

%package -n sogo-devel
Summary:      Development headers and libraries for SOGo
Group:        Development/Libraries/Objective C
AutoReqProv:  no

%description -n sogo-devel
Development headers and libraries for SOGo. Needed to create modules.

%package -n sope%{sope_major_version}%{sope_minor_version}-gdl1-contentstore
Summary:      Storage backend for folder abstraction.
Group:        Development/Libraries/Objective C
Requires:     sope%{sope_major_version}%{sope_minor_version}-gdl1
AutoReqProv:  no

%description -n sope%{sope_major_version}%{sope_minor_version}-gdl1-contentstore
The storage backend implements the "low level" folder abstraction, which is
basically an arbitary "BLOB" containing some document.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package -n sope%{sope_major_version}%{sope_minor_version}-gdl1-contentstore-devel
Summary:      Development files for the GNUstep database libraries
Group:        Development/Libraries/Objective C
Requires:     sope%{sope_major_version}%{sope_minor_version}-gdl1
AutoReqProv:  no

%description -n sope%{sope_major_version}%{sope_minor_version}-gdl1-contentstore-devel
This package contains the header files for SOPE's GDLContentStore library.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package -n sope%{sope_major_version}%{sope_minor_version}-cards
Summary:      SOPE versit parsing library for iCal and VCard formats
Group:        Development/Libraries/Objective C
AutoReqProv:  no

%description -n sope%{sope_major_version}%{sope_minor_version}-cards
SOPE versit parsing library for iCal and VCard formats

%package -n sope%{sope_major_version}%{sope_minor_version}-cards-devel
Summary:      SOPE versit parsing library for iCal and VCard formats
Group:        Development/Libraries/Objective C
Requires:     sope%{sope_major_version}%{sope_minor_version}-cards
AutoReqProv:  no

%description -n sope%{sope_major_version}%{sope_minor_version}-cards-devel
SOPE versit parsing library for iCal and VCard formats

%if %enable_openchange
%package openchange-backend
Summary:      SOGo backend for OpenChange
Group:        Productivity/Groupware
AutoReqProv:  no

%description openchange-backend
SOGo backend for OpenChange
%endif

########################################
%prep
rm -fr ${RPM_BUILD_ROOT}
%setup -q -n sogo-SOGo-%{sogo_version}


# ****************************** build ********************************
%build
%if 0%{?el7}
. %{_libdir}/GNUstep/Makefiles/GNUstep.sh
%else
. /usr/share/GNUstep/Makefiles/GNUstep.sh
%endif
./configure %saml2_cfg_opts %mfa_cfg_opts %sodium_cfg_opts

case %{_target_platform} in
ppc64-*) 
  cc="gcc -m64";
  ldflags="-m64";; 
*)
  cc="gcc";
  ldflags="";; 
esac

make CC="$cc" LDFLAGS="$ldflags" messages=yes

# OpenChange
%if %enable_openchange
(cd OpenChange; \
 LD_LIBRARY_PATH=../SOPE/NGCards/obj:../SOPE/GDLContentStore/obj \
 make GNUSTEP_INSTALLATION_DOMAIN=SYSTEM )
%endif

# ****************************** install ******************************
%install
QA_SKIP_BUILD_ROOT=1
export QA_SKIP_BUILD_ROOT

case %{_target_platform} in
ppc64-*)
  cc="gcc -m64";
  ldflags="-m64";;
*)
  cc="gcc";
  ldflags="";;
esac

make DESTDIR=${RPM_BUILD_ROOT} \
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
     CC="$cc" LDFLAGS="$ldflags" \
     install

%if 0%{?_with_systemd}
  install -d  ${RPM_BUILD_ROOT}%{_unitdir}
%else
  install -d  ${RPM_BUILD_ROOT}/etc/init.d
%endif

install -d  ${RPM_BUILD_ROOT}/etc/cron.d
install -d ${RPM_BUILD_ROOT}/etc/cron.daily
install -d ${RPM_BUILD_ROOT}/etc/logrotate.d
install -d ${RPM_BUILD_ROOT}/etc/sysconfig
install -d ${RPM_BUILD_ROOT}/etc/httpd/conf.d
install -d ${RPM_BUILD_ROOT}/usr/sbin
install -d ${RPM_BUILD_ROOT}/var/lib/sogo
install -d ${RPM_BUILD_ROOT}/var/log/sogo
install -d ${RPM_BUILD_ROOT}/var/run/sogo
install -d ${RPM_BUILD_ROOT}/var/spool/sogo
install -d -m 750 ${RPM_BUILD_ROOT}/etc/sogo
install -m 640 Scripts/sogo.conf ${RPM_BUILD_ROOT}/etc/sogo/
#install -m 755 Scripts/openchange_user_cleanup ${RPM_BUILD_ROOT}/%{_sbindir}
cat Apache/SOGo.conf | sed -e "s@/lib/@/%{_lib}/@g" > ${RPM_BUILD_ROOT}/etc/httpd/conf.d/SOGo.conf
install -m 600 Scripts/sogo.cron ${RPM_BUILD_ROOT}/etc/cron.d/sogo
cp Scripts/tmpwatch ${RPM_BUILD_ROOT}/etc/cron.daily/sogo-tmpwatch
chmod 755 ${RPM_BUILD_ROOT}/etc/cron.daily/sogo-tmpwatch
cp Scripts/logrotate ${RPM_BUILD_ROOT}/etc/logrotate.d/sogo

%if 0%{?_with_systemd}
  cp Scripts/sogo-systemd-redhat ${RPM_BUILD_ROOT}%{_unitdir}/sogod.service
  chmod 644 ${RPM_BUILD_ROOT}%{_unitdir}/sogod.service
  mkdir ${RPM_BUILD_ROOT}/etc/tmpfiles.d
  cp Scripts/sogo-systemd.conf ${RPM_BUILD_ROOT}/etc/tmpfiles.d/sogo.conf
  chmod 644 ${RPM_BUILD_ROOT}/etc/tmpfiles.d/sogo.conf
%else
  cp Scripts/sogo-init.d-redhat ${RPM_BUILD_ROOT}/etc/init.d/sogod
  chmod 755 ${RPM_BUILD_ROOT}/etc/init.d/sogod
%endif

cp Scripts/sogo-default ${RPM_BUILD_ROOT}/etc/sysconfig/sogo
rm -rf ${RPM_BUILD_ROOT}%{_bindir}/test_quick_extract

# OpenChange
%if %enable_openchange
(cd OpenChange; \
 LD_LIBRARY_PATH=${RPM_BUILD_ROOT}%{_libdir} \
 make DESTDIR=${RPM_BUILD_ROOT} \
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
      CC="$cc" LDFLAGS="$ldflags" \
   install)
%endif

# ActiveSync
(cd ActiveSync; \
 LD_LIBRARY_PATH=${RPM_BUILD_ROOT}%{_libdir} \
 make DESTDIR=${RPM_BUILD_ROOT} \
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
      CC="$cc" LDFLAGS="$ldflags" \
   install)

# ****************************** clean ********************************
%clean
rm -fr ${RPM_BUILD_ROOT}

# ****************************** files ********************************
%files -n sogo
%defattr(-,root,root,-)

%if 0%{?_with_systemd}
%{_unitdir}/sogod.service
%{_sysconfdir}/tmpfiles.d/sogo.conf
%else
%{_sysconfdir}/init.d/sogod
%endif
%{_sysconfdir}/cron.daily/sogo-tmpwatch
%dir %attr(0700, %sogo_user, %sogo_user) %{_var}/lib/sogo
%dir %attr(0700, %sogo_user, %sogo_user) %{_var}/log/sogo
%dir %attr(0755, %sogo_user, %sogo_user) %{_var}/run/sogo
%dir %attr(0700, %sogo_user, %sogo_user) %{_var}/spool/sogo
%dir %attr(0750, root, %sogo_user) %{_sysconfdir}/sogo
%{_sbindir}/sogod
#%{_sbindir}/openchange_user_cleanup
%{_libdir}/sogo/libSOGo.so*
%{_libdir}/sogo/libSOGoUI.so*
%{_libdir}/GNUstep/SOGo/AdministrationUI.SOGo
%{_libdir}/GNUstep/SOGo/Appointments.SOGo
%{_libdir}/GNUstep/SOGo/CommonUI.SOGo
%{_libdir}/GNUstep/SOGo/Contacts.SOGo
%{_libdir}/GNUstep/SOGo/ContactsUI.SOGo
%{_libdir}/GNUstep/SOGo/MailPartViewers.SOGo
%{_libdir}/GNUstep/SOGo/Mailer.SOGo
%{_libdir}/GNUstep/SOGo/MailerUI.SOGo
%{_libdir}/GNUstep/SOGo/MainUI.SOGo
%{_libdir}/GNUstep/SOGo/PreferencesUI.SOGo
%{_libdir}/GNUstep/SOGo/SchedulerUI.SOGo

%{_libdir}/GNUstep/Frameworks/SOGo.framework/Resources
%{_libdir}/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/sogo/libSOGo.so*
%{_libdir}/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/Resources
%{_libdir}/GNUstep/Frameworks/SOGo.framework/Versions/Current
%{_libdir}/GNUstep/SOGo/Templates
%{_libdir}/GNUstep/SOGo/WebServerResources
%{_libdir}/GNUstep/OCSTypeModels
%{_libdir}/GNUstep/WOxElemBuilders-*

%config(noreplace) %attr(0640, root, %sogo_user) %{_sysconfdir}/sogo/sogo.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/sogo
%config(noreplace) %{_sysconfdir}/cron.d/sogo
%config(noreplace) %{_sysconfdir}/httpd/conf.d/SOGo.conf
%config(noreplace) %{_sysconfdir}/sysconfig/sogo
%doc ChangeLog Scripts/*sh Scripts/updates.php Apache/SOGo-apple-ab.conf

%files -n sogo-tool
%{_sbindir}/sogo-tool

%files -n sogo-ealarms-notify
%{_sbindir}/sogo-ealarms-notify

%files -n sogo-slapd-sockd
%{_sbindir}/sogo-slapd-sockd

%files -n sogo-activesync
%{_libdir}/GNUstep/SOGo/ActiveSync.SOGo
%doc ActiveSync/LICENSE ActiveSync/README

%files -n sogo-devel
%{_includedir}/SOGo
%{_includedir}/SOGoUI
%{_libdir}/sogo/libSOGo.so*
%{_libdir}/sogo/libSOGoUI.so*
%{_libdir}/GNUstep/Frameworks/SOGo.framework/Headers
%{_libdir}/GNUstep/Frameworks/SOGo.framework/sogo/libSOGo.so
%{_libdir}/GNUstep/Frameworks/SOGo.framework/sogo/SOGo
%{_libdir}/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/Headers
%{_libdir}/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/sogo/libSOGo.so*
%{_libdir}/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/sogo/SOGo

%files -n sope%{sope_major_version}%{sope_minor_version}-gdl1-contentstore
%defattr(-,root,root,-)
%{_libdir}/sogo/libGDLContentStore*.so*

%files -n sope%{sope_major_version}%{sope_minor_version}-gdl1-contentstore-devel
%{_includedir}/GDLContentStore
%{_libdir}/sogo/libGDLContentStore*.so*

%files -n sope%{sope_major_version}%{sope_minor_version}-cards
%{_libdir}/sogo/libNGCards.so*
%{_libdir}/GNUstep/SaxDrivers-*
%{_libdir}/GNUstep/SaxMappings
%{_libdir}/GNUstep/Libraries/Resources/NGCards

%files -n sope%{sope_major_version}%{sope_minor_version}-cards-devel
%{_includedir}/NGCards
%{_libdir}/sogo/libNGCards.so*

%if %enable_openchange
%files openchange-backend
%defattr(-,root,root,-)
%{_libdir}/GNUstep/SOGo/*.MAPIStore
%{_libdir}/mapistore_backends/*
%endif

# **************************** pkgscripts *****************************
%pre
if ! getent group %sogo_user >& /dev/null; then
  groupadd -f -r %sogo_user
fi
if ! id %sogo_user >& /dev/null; then
  /usr/sbin/useradd -d %{_var}/lib/sogo -c "SOGo daemon" -s /sbin/nologin -M -r -g %sogo_user %sogo_user
fi

%post
# update timestamp on imgs,css,js to let apache know the files changed
find %{_libdir}/GNUstep/SOGo/WebServerResources  -exec touch {} \;
# make shells scripts in documentation directory executable
find %{_docdir}/ -name '*.sh' -exec chmod a+x {} \;

%if 0%{?_with_systemd}
  systemctl daemon-reload
  systemctl enable sogod
  systemctl try-restart sogod > /dev/null 2>&1
%else
  /sbin/chkconfig --add sogod
  /etc/init.d/sogod condrestart  >&/dev/null
%endif

%preun
if [ "$1" == "0" ]
then
  %if 0%{?_with_systemd}
    systemctl disable sogod
    systemctl stop sogod > /dev/null 2>&1
  %else
    /sbin/chkconfig --del sogod
    /sbin/service sogod stop > /dev/null 2>&1
  %endif
fi

%postun
if test "$1" = "0"
then
  /usr/sbin/userdel %sogo_user
  /usr/sbin/groupdel %sogo_user > /dev/null 2>&1
  /bin/rm -rf %{_var}/run/sogo
  /bin/rm -rf %{_var}/spool/sogo
  # not removing /var/lib/sogo to keep .GNUstepDefaults
fi

# ********************************* changelog *************************
%changelog
* Thu Mar 21 2024 stephane de Labrusse <stephdl@de-labrusse.fr> - 5.10.0
- Bump to 5.10.0
* Wed Oct 18 2023 stephane de Labrusse <stephdl@de-labrusse.fr> - 5.9.0
- Bump to 5.9.0
* Thu Jun 22 2023 stephane de Labrusse <stephdl@de-labrusse.fr> - 5.8.4
- Bump to 5.8.4

* Tue Jun 20 2023 stephane de Labrusse <stephdl@de-labrusse.fr> - 5.8.3
- Bump to 5.8.3
* Wed Apr 05 2023 stephane de Labrusse <stephdl@de-labrusse.fr> - 5.8.2
- Bump to 5.8.2

* Tue Aug 09 2022 stephane de Labrusse <stephdl@de-labrusse.fr> - 5.7.0
- Bump to 5.7.0

* Mon May 16 2022 stephane de Labrusse <stephdl@de-labrusse.fr> - 5.6.0
- Bump to 5.6.0

* Wed Feb 09 2022 stephane de Labrusse <stephdl@de-labrusse.fr> - 5.5.1
- Bump to 5.5.1

* Wed Jan 26 2022 stephane de Labrusse <stephdl@de-labrusse.fr> - 5.5.0
- Bump to 5.5.0

* Fri Dec 24 2021 stephane de Labrusse <stephdl@de-labrusse.fr> - 5.4.0
- Bump to 5.4.0

* Fri Sep 17 2021 stephane de Labrusse <stephdl@de-labrusse.fr> - 5.2.0
- Bump to 5.2.0

* Wed Jul 7 2021 Stephane de Labrusse <stephdl@de-labrusse.fr>
- Bump to 5.1.1

* Tue Apr 6 2021 Stephane de Labrusse <stephdl@de-labrusse.fr>
- Bump to 5.1.0

* Tue Oct 27 2020 Stephane de Labrusse <stephdl@de-labrusse.fr>
- Bump to 5.0.1

* Tue Aug 11 2020 Stephane de Labrusse <stephdl@de-labrusse.fr>
- Bump to 5.0.0

* Fri May 22 2020  Stephane de Labrusse <stephdl@de-labrusse.fr>
- Bump to 4.3.2

* Thu Dec 19 2019 Stephane de Labrusse <stephdl@de-labrusse.fr>
- Bump to 4.2.0

* Mon Nov 09 2019 Stephane de Labrusse <stephdl@de-labrusse.fr>
- Upgrade to 4.1.1

* Mon Oct 28 2019 Stephane de Labrusse <stephdl@de-labrusse.fr>
- Upgrade to 4.1.0

* Tue Aug 27 2019 Stephane de Labrusse <stephdl@de-labrusse.fr>
- Upgrade to 4.08

* Mon Mar 11 2019 Stephane de Labrusse <stephdl@de-labrusse.fr>
- Upgrade to 4.07

* Fri Aug 24 2018 Stephane de Labrusse <stephdl@de-labrusse.fr>
- Upgrade to 4.02

* Wed Jul 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr>
- upgrade to 3.2.10

* Tue May 09 2017 Stephane de Labrusse <stephdl@de-labrusse.fr>
- upgrade to 3.2.9

* Tue Feb 02 2017 Stephane de Labrusse <stephdl@de-labrusse.fr>
- upgrade to 3.2.6a

* Wed Oct 12 2016 Mark Verlinde <mark.verlinde@gmail.com>
- refactor for maock build

* Thu Mar 31 2015 Inverse inc. <support@inverse.ca>
- Change script start sogod for systemd

* Wed Oct 8 2014 Inverse inc. <support@inverse.ca>
- fixed the library move to "sogo" app dir

* Wed Jan 15 2014 Inverse inc. <support@inverse.ca>
- New package: sogo-activesync
- explicitly list all *.SOGo modules in sogo package
- added dependency on sogo = %version for sogo-tool

* Thu Apr 17 2013 Inverse inc. <support@inverse.ca>
- Install openchange_user_cleanup in sbindir instead of doc

* Wed Apr 10 2013 Inverse inc. <support@inverse.ca>
- use %sogo_user instead of 'sogo'
- install a sample sogo.conf in /etc/sogo

* Tue Jan 22 2013 Inverse inc. <support@inverse.ca>
- Create the sogo user as a system user
- Use %attr() to set directory permissions instead of chown/chmod

* Mon Nov 12 2012 Inverse inc. <support@inverse.ca>
- Add missing dependency on lasso and lasso-devel

* Mon Nov 05 2012 Inverse inc. <support@inverse.ca>
- Disable saml2 on rhel5 - glib2 too old

* Fri Nov 02 2012 Inverse inc. <support@inverse.ca>
- Enable saml2

* Tue Aug 28 2012 Inverse inc. <support@inverse.ca>
- Add openchange_cleanup.py and tweak it to work on RHEL5

* Tue Jul 31 2012 Inverse inc. <support@inverse.ca>
- treat logrotate file as a config file

* Fri May 24 2012 Inverse inc. <support@inverse.ca>
- %post: restart sogo if it was running before rpm install

* Fri Mar 16 2012 Inverse inc. <support@inverse.ca>
- %post: update timestamp on imgs,css,js to let apache know the files changed

* Fri Feb 16 2012 Inverse inc. <support@inverse.ca>
- Use globbing to include all sql upgrade scripts instead of listing them all

* Tue Jan 10 2012 Inverse inc. <support@inverse.ca>
- /etc/cron.d/sogo

* Thu Oct 27 2011 Inverse inc. <support@inverse.ca>
- make build of sogo-openchange-backend conditional to sogo_version >= 2

* Fri Oct 14 2011 Inverse inc. <support@inverse.ca>
- adapted to gnustep-make 2.6
- added sogo-openchange-backend

* Tue Sep 28 2010 Inverse inc. <support@inverse.ca>
- removed "README" from documentation

* Fri Aug 20 2010 Inverse inc. <support@inverse.ca>
- added sogo-ealarms-notify package

* Tue Apr 06 2010 Inverse inc. <support@inverse.ca>
- added sogo-slapd-sockd package

* Thu Jul 31 2008 Inverse inc. <support@inverse.ca>
- added dependencies on sopeXY-appserver, -core, -gdl1-contentstore and -ldap

* Wed May 21 2008 Inverse inc. <support@inverse.ca>
- removed installation of template and resource files, since it is now done by the upstream package

* Tue Oct 4 2007 Inverse inc. <support@inverse.ca>
- added package sope-gdl1-contentstore

* Wed Jul 18 2007 Inverse inc. <support@inverse.ca>
- initial build
