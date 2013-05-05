# $Id$
# Authority: dag

# Tag: test

Summary: HA-Proxy is a TCP/HTTP reverse proxy for high availability environments
Name: haproxy
Version: 1.4.23
Release: bas.1
License: GPL
Group: System Environment/Daemons
URL: http://haproxy.1wt.eu

Packager: Thomas Heil <heil@terminal-consulting.de>
Vendor: Zscho Repository, http://puppet.zscho.net/repo

#Source0: http://w.ods.org/tools/haproxy/haproxy-%{version}.tar.gz
Source0:  http://haproxy.1wt.eu/download/1.4/src/haproxy-%{version}.tar.gz
Source1: haproxy.cfg
Source2: haproxy.init
Source99: filter-haproxy-requires.sh

Patch0: 0001-BUG-MAJOR-backend-consistent-hash-can-loop-forever-i.patch
Patch1: 0002-BUG-MEDIUM-checks-disable-TCP-quickack-when-pure-TCP.patch
Patch2: 001-haproxy-1.4.x-sendproxy.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pcre-devel
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/chkconfig, /sbin/service
Requires(postun):   /sbin/service

%global __perl_requires %{SOURCE99}

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

It needs very little resource. Its event-driven architecture allows it to easily
handle thousands of simultaneous connections on hundreds of instances without
risking the system's stability.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%build
%{__make} TARGET=linux26 "COPTS.pcre=-DUSE_PCRE $(pcre-config --cflags)" USE_LINUX_TPROXY=1 USE_LINUX_SPLICE=1 SMALL_OPTS="-DBUFSIZE=16384 -DMAXREWRITE=8192 -DSYSTEM_MAXCONN=65530"


%install
%{__rm} -rf %{buildroot}
 
%{__install} -d -m0755 %{buildroot}%{_datadir}/haproxy/

%{__install} -D -m0755 haproxy %{buildroot}%{_sbindir}/haproxy
%{__install} -D -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/haproxy/haproxy.cfg
%{__install} -D -m0755 %{SOURCE2} %{buildroot}%{_initrddir}/haproxy
 
%clean
%{__rm} -rf %{buildroot}
 
%post
/sbin/chkconfig --add haproxy

%preun
if [ $1 -eq 0 ]; then
	/sbin/service haproxy stop &>/dev/null || :
	/sbin/chkconfig --del haproxy
fi

%postun
if [ $1 -ge 1 ]; then
	/sbin/service haproxy condrestart &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG README TODO doc/* examples/
%config(noreplace) %{_sysconfdir}/haproxy/
%config %{_initrddir}/haproxy
%{_sbindir}/haproxy
%dir %{_datadir}/haproxy/

%changelog
* Wed Nov 03 2010 Thomas Heil <heil@terminal-consulting.de>
- bump to Version 1.4.9 which is mainly bug fixing release
-* Wed Oct 06 2010 Thomas Heil <heil@terminal-consulting.de>
- add gracefull reload to init-script
-* Wed Jun 07 2010 Thomas Heil <heil@terminal-consulting.de>
- Upgrade to 1.4.8
- Add SMALL_OPTS so TPROXY Support may available in the near future

* Tue Oct 27 2009 Thomas Heil <heil@terminal-consulting.de>
- Upgrade to 1.2.22

* Tue Feb 07 2006 Dag Wieers <dag@wieers.com> - 1.1.34-1
- Initial package. (using DAR)
