%define haproxy_user    haproxy
%define haproxy_group   %{haproxy_user}
%define haproxy_home    %{_localstatedir}/lib/haproxy
%define haproxy_confdir %{_sysconfdir}/haproxy
%define haproxy_datadir %{_datadir}/haproxy
%define patch_count	37
%define altrelease	dev18
%define altname	haproxy

Name:           haproxy-devel
Version:        1.5
Release:        dev18.%{patch_count}
Summary:        HA-Proxy is a TCP/HTTP reverse proxy for high availability environments

Group:          System Environment/Daemons
License:        GPLv2+

URL:            http://haproxy.1wt.eu/
Source0:        http://haproxy.1wt.eu/download/1.5/src/devel/haproxy-%{version}-%{altrelease}.tar.gz
Source1:        %{altname}.init
Source2:        %{altname}.cfg
Source3:        %{altname}.logrotate

Patch0: 0001-BUG-MINOR-http-add-header-set-header-did-not-accept-.patch
Patch1: 0002-MINOR-show-PCRE-version-and-JIT-status-in-vv.patch
Patch2: 0003-BUILD-mention-in-the-Makefile-that-USE_PCRE_JIT-is-f.patch
Patch3: 0004-BUG-MEDIUM-splicing-is-broken-since-1.5-dev12.patch
Patch4: 0005-BUG-MAJOR-acl-add-implicit-arguments-to-the-resolve-.patch
Patch5: 0006-BUG-regex-fix-pcre-compile-error-when-using-JIT.patch
Patch6: 0007-BUG-MINOR-tcp-fix-error-reporting-for-TCP-rules.patch
Patch7: 0008-CLEANUP-peers-remove-a-bit-of-spaghetti-to-prepare-f.patch
Patch8: 0009-MINOR-stick-table-allow-to-allocate-an-entry-without.patch
Patch9: 0010-BUG-MAJOR-peers-fix-an-overflow-when-syncing-strings.patch
Patch10: 0011-MINOR-session-only-call-http_send_name_header-when-c.patch
Patch11: 0012-MINOR-tcp-report-the-erroneous-word-in-tcp-request-t.patch
Patch12: 0013-BUG-MAJOR-backend-consistent-hash-can-loop-forever-i.patch
Patch13: 0014-BUG-MEDIUM-log-fix-regression-on-log-format-handling.patch
Patch14: 0015-MEDIUM-log-report-file-name-line-number-and-directiv.patch
Patch15: 0016-BUG-MINOR-cli-clear-table-did-not-work-anymore-witho.patch
Patch16: 0017-BUG-MINOR-cli-clear-table-xx-data.xx-does-not-work-a.patch
Patch17: 0018-BUG-MAJOR-http-compression-still-has-defects-on-chun.patch
Patch18: 0019-BUG-MINOR-jit-don-t-rely-on-USE-flag-to-detect-suppo.patch
Patch19: 0020-MEDIUM-stats-add-proxy-name-filtering-on-the-statist.patch
Patch20: 0021-MINOR-stats-remove-the-autofocus-on-the-scope-input-.patch
Patch21: 0022-BUG-MINOR-stats-fix-confirmation-links-on-the-stats-.patch
Patch22: 0023-BUG-MINOR-stats-the-status-bar-does-not-appear-anymo.patch
Patch23: 0024-MINOR-stats-show-soft-stopped-servers-in-different-c.patch
Patch24: 0025-BUG-MEDIUM-stats-allocate-the-stats-frontend-also-on.patch
Patch25: 0026-MINOR-compression-acl-res.comp-and-fetch-res.comp_al.patch
Patch26: 0027-BUG-MEDIUM-stats-fix-a-regression-when-dealing-with-.patch
Patch27: 0028-BUG-MEDIUM-Fix-crt-list-file-parsing-error-filtered-.patch
Patch28: 0029-BUG-MINOR-fix-unterminated-ACL-array-in-compression.patch
Patch29: 0030-BUG-MINOR-config-source-does-not-work-in-defaults-se.patch
Patch30: 0031-BUILD-last-fix-broke-non-linux-platforms.patch
Patch31: 0032-BUG-MEDIUM-ssl-EDH-ciphers-are-not-usable-if-no-DH-p.patch
Patch32: 0033-MINOR-init-indicate-the-SSL-runtime-version-on-vv.patch
Patch33: 0034-BUG-MEDIUM-shctx-makes-the-code-independent-on-SSL-r.patch
Patch34: 0035-BUG-MEDIUM-compression-the-deflate-algorithm-must-us.patch
Patch35: 0036-BUILD-stdbool-is-not-portable-again.patch
Patch36: 0037-DOC-readme-add-a-small-reminder-about-restrictions-t.patch


BuildRoot:      %{_tmppath}/%{altname}-%{version}-%{altrelease}-root-%(%{__id_u} -n)
BuildRequires:  pcre-devel openssl-devel zlib-devel

Requires:           pcre
Requires(pre):      %{_sbindir}/useradd
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/chkconfig, /sbin/service
Requires(postun):   /sbin/service

%description
HA-Proxy is a TCP/HTTP reverse proxy which is particularly suited for high
availability environments. Indeed, it can:
- route HTTP requests depending on statically assigned cookies
- spread the load among several servers while assuring server persistence
  through the use of HTTP cookies
- switch to backup servers in the event a main one fails
- accept connections to special ports dedicated to service monitoring
- stop accepting connections without breaking existing ones
- add/modify/delete HTTP headers both ways
- block requests matching a particular pattern

%package log
Summary: halog for %{name}
Group: System Environment/Daemons

%description log
halog binary for %{name}
HA-Proxy is a TCP/HTTP reverse proxy which is particularly suited for high
availability environments.


%prep
%setup -q -n %{altname}-%{version}-%{altrelease}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1

%build
# No configure script is present, it is all done via make flags
# EL-5 is linux 2.6 so using linux26 as target.

# Recommended optimization option for x86 builds
regparm_opts=
%ifarch %ix86 x86_64
regparm_opts="USE_REGPARM=1"
%endif
make USE_OPENSSL=1 %{?_smp_mflags} CPU="generic" TARGET="linux26" USE_PCRE=1 ${regparm_opts} ADDINC="%{optflags} -I/usr/include/pcre" \
	SMALL_OPTS="-DBUFSIZE=16384 -DMAXREWRITE=1030 -DSYSTEM_MAXCONN=165530 " \
	USE_LINUX_TPROXY=1 USE_LINUX_SPLICE=1 USE_REGPARM=1 USE_OPENSSL=1 \
	USE_ZLIB=yes \
	VERSION="%{altrelease}-patch-%{patch_count}" 

make -C contrib/halog \
	USE_OPENSSL=1 %{?_smp_mflags} CPU="generic" TARGET="linux26" USE_PCRE=1 ${regparm_opts} ADDINC="%{optflags} -I/usr/include/pcre" \
	SMALL_OPTS="-DBUFSIZE=16384 -DMAXREWRITE=1030 -DSYSTEM_MAXCONN=165530 " \
	USE_LINUX_TPROXY=1 USE_LINUX_SPLICE=1 USE_REGPARM=1 USE_OPENSSL=1 \
	USE_ZLIB=yes \
	VERSION="%{altrelease}-patch-%{patch_count}" \
	halog

%install
rm -rf %{buildroot}
# there is no install make target, only one file is created during build
%{__install} -p -D -m 0755 %{altname} %{buildroot}%{_sbindir}/%{altname}
%{__install} -p -D -m 0755 ./contrib/halog/halog %{buildroot}%{_sbindir}/halog
%{__install} -p -D -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/%{altname}
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{haproxy_confdir}/%{altname}.cfg
%{__install} -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{altname}
%{__install} -d -m 0755 %{buildroot}%{haproxy_home}
%{__install} -d -m 0755 %{buildroot}%{haproxy_datadir}
%{__install} -p -D -m 0644 ./doc/%{altname}.1 %{buildroot}%{_mandir}/man1/%{altname}.1
for httpfile in $(find ./examples/errorfiles/ -type f) 
do
    %{__install} -p -m 0644 $httpfile %{buildroot}%{haproxy_datadir}
done

# convert all text files to utf8
for textfile in $(find ./ -type f -name '*.txt')
do
    mv $textfile $textfile.old
    iconv --from-code ISO8859-1 --to-code UTF-8 --output $textfile $textfile.old
    rm -f $textfile.old
done 


%clean
rm -rf %{buildroot}


%pre
%{_sbindir}/useradd -c "HAProxy user" -s /bin/false -r -d %{haproxy_home} %{haproxy_user} 2>/dev/null || :


%post
/sbin/chkconfig --add %{altname}
    

%preun
if [ $1 = 0 ]; then
    /sbin/service %{altname} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{altname}
fi  
    

%postun
if [ $1 -ge 1 ]; then
/sbin/service %{name} condrestart > /dev/null 2>&1 || :
fi  
 

%files
%defattr(-,root,root,-)
%doc doc/*
%doc examples/url-switching.cfg
%doc examples/acl-content-sw.cfg
%doc examples/content-sw-sample.cfg
%doc examples/cttproxy-src.cfg
%doc examples/haproxy.cfg
%doc examples/tarpit.cfg
#%doc examples/tcp-splicing-sample.cfg
%doc CHANGELOG LICENSE README
%dir %{haproxy_datadir}
%dir %{haproxy_datadir}/*
%dir %{haproxy_confdir}
%config(noreplace) %{haproxy_confdir}/%{altname}.cfg
%config(noreplace) %{_sysconfdir}/logrotate.d/%{altname}
%{_initrddir}/%{altname}
%{_sbindir}/%{altname}
%{_mandir}/man1/%{altname}.1.gz
%attr(-,%{haproxy_user},%{haproxy_group}) %dir %{haproxy_home}

%files log
%defattr(-,root,root,-)
%{_sbindir}/halog


%changelog
* Thu Feb 24 2011 Ben Timby <btimby@gmail.com> 1.3.25-2
- added USE_LINUX_TPROXY

* Sun Jun 20 2010 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.25-1
- update to 1.3.25

* Thu Feb 18 2010 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.23-1
- update to 1.3.23

* Sat Oct 17 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.22-2
- update to 1.3.22
- add logrotate configuration

* Mon Oct 12 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.21-1
- update to 1.3.21

* Sun Oct 11 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.20-1
- update to 1.3.20

* Sun Aug 02 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.19-1
- update to 1.3.19

* Sun May 17 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> 1.3.18-1
-  update to 1.3.18

* Sat Apr 11 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> 1.3.17-1
-  update to 1.3.17

* Tue Dec 30 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.14.11-1
- update to 1.3.14.11
- remove upstream patches, they are now part of source distribution

* Sat Nov 22 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.14.10-3
- apply upstream error reporting patch

* Sat Nov 15 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.14.10-2
- rebuilt

* Sat Nov 15 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.14.10-1
- update to 1.3.14.10
- add in recommended regparm build option for x86

* Sat Jun 28 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.14.6-2
- update to 1.3.14.6
- remove MIT license portion, that code was removed from upstream

* Mon Apr 14 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.14.4-1
- update to 1.3.14.4
- fix reload command on init script

* Mon Jan 21 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.14.2-1
- update to 1.3.14.2
- update make flags that changed with this upstream release
- added man page installation

* Sun Dec 16 2007 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3.14
- update to 1.3.14

* Sun Nov 11 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.3.12.4-1
- update to 1.3.12.4

* Fri Sep 21 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.3.12.2-3
- added pcre as Requires dependency

* Thu Sep 20 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.3.12.2-2
- update License field

* Thu Sep 20 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.3.12.2-1
- update to 1.3.12.2
- remove the upstream patch

* Tue Sep 18 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.3.12.1-1
- switch to 1.3.12.1 branch
- add patch from upstream with O'Reilly licensing updates.
- convert ISO-8859-1 doc files to UTF-8

* Sat Mar 24 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.2.17-2
- addition of haproxy user
- add license information

* Fri Mar 23 2007 Jeremy Hinegardner <jeremy@hinegardner.org> - 1.2.17-1
- initial packaging
