%define haproxy_user    haproxy
%define haproxy_group   %{haproxy_user}
%define haproxy_home    %{_localstatedir}/lib/haproxy
%define haproxy_confdir %{_sysconfdir}/haproxy
%define haproxy_datadir %{_datadir}/haproxy
%define patch_count	12
%define altrelease	dev17
%define altname	haproxy

Name:           haproxy-devel
Version:        1.5
Release:        dev17.%{patch_count}
Summary:        HA-Proxy is a TCP/HTTP reverse proxy for high availability environments

Group:          System Environment/Daemons
License:        GPLv2+

URL:            http://haproxy.1wt.eu/
Source0:        http://haproxy.1wt.eu/download/1.5/src/devel/haproxy-%{version}-%{altrelease}.tar.gz
Source1:        %{altname}.init
Source2:        %{altname}.cfg
Source3:        %{altname}.logrotate
Patch0:		0001-BUG-MINOR-time-frequency-counters-are-not-t-1.5-dev17.diff
Patch1:		0002-BUG-MINOR-http-don-t-process-abortonclose-w-1.5-dev17.diff
Patch2:		0003-BUG-MEDIUM-stream_interface-don-t-close-out-1.5-dev17.diff
Patch3:		0004-BUG-MEDIUM-checks-ignore-late-resets-after--1.5-dev17.diff
Patch4:		0005-DOC-fix-bogus-recommendation-on-usage-of-gp-1.5-dev17.diff
Patch5:		0006-BUG-MINOR-http-compression-lookup-Cache-Con-1.5-dev17.diff
Patch6:		0007-DOC-typo-and-minor-fixes-in-compression-par-1.5-dev17.diff
Patch7:		0008-MINOR-config-http-request-configuration-err-1.5-dev17.diff
Patch8:		0009-MINOR-signal-don-t-block-SIGPROF-by-default-1.5-dev17.diff
Patch9:		0010-OPTIM-epoll-make-use-of-EPOLLRDHUP-1.5-dev17.diff
Patch10:	0011-OPTIM-splice-detect-shutdowns-and-avoid-spl-1.5-dev17.diff
Patch11:	0012-OPTIM-splice-assume-by-default-that-splice--1.5-dev17.diff

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
