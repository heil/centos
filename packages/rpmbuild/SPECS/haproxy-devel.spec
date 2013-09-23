%define haproxy_user    haproxy
%define haproxy_group   %{haproxy_user}
%define haproxy_home    %{_localstatedir}/lib/haproxy
%define haproxy_confdir %{_sysconfdir}/haproxy
%define haproxy_datadir %{_datadir}/haproxy
%define patch_count	57
%define altrelease	dev19
%define altname	haproxy

Name:           haproxy-devel
Version:        1.5
Release:        dev19.%{patch_count}
Summary:        HA-Proxy is a TCP/HTTP reverse proxy for high availability environments

Group:          System Environment/Daemons
License:        GPLv2+

URL:            http://haproxy.1wt.eu/
Source0:        http://haproxy.1wt.eu/download/1.5/src/devel/haproxy-%{version}-%{altrelease}.tar.gz
Source1:        %{altname}.init
Source2:        %{altname}.cfg
Source3:        %{altname}.logrotate

Ptch0 0001-CLEANUP-session-remove-event_accept-which-was-not-us.patch
Patch1 0002-MEDIUM-session-disable-lingering-on-the-server-when-.patch
Patch2 0003-BUG-MEDIUM-prevent-gcc-from-moving-empty-keywords-li.patch
Patch3 0004-BUG-MINOR-http-fix-set-tos-not-working-in-certain-co.patch
Patch4 0005-MEDIUM-http-add-IPv6-support-for-set-tos.patch
Patch5 0006-DOC-remove-the-comment-saying-that-SSL-certs-are-not.patch
Patch6 0007-BUG-MINOR-deinit-free-fdinfo-while-doing-cleanup.patch
Patch7 0008-BUG-counters-third-counter-was-not-stored-if-others-.patch
Patch8 0009-DOC-minor-typo-fix-in-documentation.patch
Patch9 0010-BUG-MAJOR-http-don-t-emit-the-send-name-header-when-.patch
Patch10 0011-BUG-MEDIUM-http-option-checkcache-fails-with-the-no-.patch
Patch11 0012-BUG-MAJOR-http-sample-prefetch-code-was-not-properly.patch
Patch12 0013-BUG-MEDIUM-server-set-the-macro-for-server-s-max-wei.patch
Patch13 0014-BUG-MEDIUM-splicing-fix-abnormal-CPU-usage-with-spli.patch
Patch14 0015-BUG-MINOR-stream_interface-don-t-call-chk_snd-on-pol.patch
Patch15 0016-OPTIM-splicing-use-splice-for-the-last-block-when-re.patch
Patch16 0017-MEDIUM-sample-handle-comma-delimited-converter-list.patch
Patch17 0018-MINOR-sample-fix-sample_process-handling-of-unstable.patch
Patch18 0019-CLEANUP-acl-move-the-3-remaining-sample-fetches-to-s.patch
Patch19 0020-MINOR-sample-add-a-new-date-fetch-to-return-the-curr.patch
Patch20 0021-MINOR-samples-add-the-http_date-offset-sample-conver.patch
Patch21 0022-DOC-minor-improvements-to-the-part-on-the-stats-sock.patch
Patch22 0023-MEDIUM-sample-systematically-pass-the-keyword-pointe.patch
Patch23 0024-MINOR-payload-split-smp_fetch_rdp_cookie.patch
Patch24 0025-MINOR-counters-factor-out-smp_fetch_sc-_tracked.patch
Patch25 0026-MINOR-counters-provide-a-generic-function-to-retriev.patch
Patch26 0027-MEDIUM-counters-factor-out-smp_fetch_sc-_get_gpc0.patch
Patch27 0028-MEDIUM-counters-factor-out-smp_fetch_sc-_gpc0_rate.patch
Patch28 0029-MEDIUM-counters-factor-out-smp_fetch_sc-_inc_gpc0.patch
Patch29 0030-MEDIUM-counters-factor-out-smp_fetch_sc-_clr_gpc0.patch
Patch30 0031-MEDIUM-counters-factor-out-smp_fetch_sc-_conn_cnt.patch
Patch31 0032-MEDIUM-counters-factor-out-smp_fetch_sc-_conn_rate.patch
Patch32 0033-MEDIUM-counters-factor-out-smp_fetch_sc-_conn_cur.patch
Patch33 0034-MEDIUM-counters-factor-out-smp_fetch_sc-_sess_cnt.patch
Patch34 0035-MEDIUM-counters-factor-out-smp_fetch_sc-_sess_rate.patch
Patch35 0036-MEDIUM-counters-factor-out-smp_fetch_sc-_http_req_cn.patch
Patch36 0037-MEDIUM-counters-factor-out-smp_fetch_sc-_http_req_ra.patch
Patch37 0038-MEDIUM-counters-factor-out-smp_fetch_sc-_http_err_cn.patch
Patch38 0039-MEDIUM-counters-factor-out-smp_fetch_sc-_http_err_ra.patch
Patch39 0040-MEDIUM-counters-factor-out-smp_fetch_sc-_kbytes_in.patch
Patch40 0041-MEDIUM-counters-factor-out-smp_fetch_sc-_bytes_in_ra.patch
Patch41 0042-MEDIUM-counters-factor-out-smp_fetch_sc-_kbytes_out.patch
Patch42 0043-MEDIUM-counters-factor-out-smp_fetch_sc-_bytes_out_r.patch
Patch43 0044-MEDIUM-counters-factor-out-smp_fetch_sc-_trackers.patch
Patch44 0045-MINOR-session-make-the-number-of-stick-counter-entri.patch
Patch45 0046-MEDIUM-counters-support-passing-the-counter-number-a.patch
Patch46 0047-MEDIUM-counters-support-looking-up-a-key-in-an-alter.patch
Patch47 0048-MEDIUM-cli-adjust-the-method-for-feeding-frequency-c.patch
Patch48 0049-MINOR-cli-make-it-possible-to-enter-multiple-values-.patch
Patch49 0050-MINOR-payload-allow-the-payload-sample-fetches-to-re.patch
Patch50 0051-BUG-MINOR-use-the-same-check-condition-for-server-as.patch
Patch51 0052-BUG-MINOR-cli-clear-table-must-not-kill-entries-that.patch
Patch52 0053-MINOR-ssl-use-MAXPATHLEN-instead-of-PATH_MAX.patch
Patch53 0054-MINOR-config-warn-when-a-server-with-no-specific-por.patch
Patch54 0055-BUG-MEDIUM-unique_id-HTTP-request-counter-must-be-un.patch
Patch55 0056-BUG-MEDIUM-unique_id-junk-in-log-on-empty-unique_id.patch
Patch56 0057-BUG-MINOR-log-junk-at-the-end-of-syslog-packet.patch
Patch57 0058-DOC-add-a-mention-about-the-limited-chunk-size.patch
Patch58 0059-MINOR-ssl-Add-statement-verifyhost-to-server-stateme.patch
Patch59 0060-BUG-MEDIUM-fix-broken-send_proxy-on-FreeBSD.patch
Patch60 0061-MEDIUM-stick-tables-flush-old-entries-upon-soft-stop.patch
Patch61 0062-MINOR-tcp-add-new-close-action-for-tcp-response.patch
Patch62 0063-MINOR-payload-provide-the-res.len-fetch-method.patch
Patch63 0064-BUILD-add-SSL_INC-SSL_LIB-variables-to-force-the-pat.patch
Patch64 0065-BUG-MEDIUM-ssl-potential-memory-leak-using-verifyhos.patch
Patch65 0066-BUILD-ssl-compilation-issue-with-openssl-v0.9.6.patch
Patch66 0067-BUG-MINOR-fix-forcing-fastinter-in-on-error.patch
heil@sun ~/work/git/centos/packages/rpmbuild/SPECS $ i=0; ls /tmp/patches/ | while read line; do  echo "Patch$i: $line"; i=$((i=$i+1)); done
Patch0: 0001-CLEANUP-session-remove-event_accept-which-was-not-us.patch
Patch1: 0002-MEDIUM-session-disable-lingering-on-the-server-when-.patch
Patch2: 0003-BUG-MEDIUM-prevent-gcc-from-moving-empty-keywords-li.patch
Patch3: 0004-BUG-MINOR-http-fix-set-tos-not-working-in-certain-co.patch
Patch4: 0005-MEDIUM-http-add-IPv6-support-for-set-tos.patch
Patch5: 0006-DOC-remove-the-comment-saying-that-SSL-certs-are-not.patch
Patch6: 0007-BUG-MINOR-deinit-free-fdinfo-while-doing-cleanup.patch
Patch7: 0008-BUG-counters-third-counter-was-not-stored-if-others-.patch
Patch8: 0009-DOC-minor-typo-fix-in-documentation.patch
Patch9: 0010-BUG-MAJOR-http-don-t-emit-the-send-name-header-when-.patch
Patch10: 0011-BUG-MEDIUM-http-option-checkcache-fails-with-the-no-.patch
Patch11: 0012-BUG-MAJOR-http-sample-prefetch-code-was-not-properly.patch
Patch12: 0013-BUG-MEDIUM-server-set-the-macro-for-server-s-max-wei.patch
Patch13: 0014-BUG-MEDIUM-splicing-fix-abnormal-CPU-usage-with-spli.patch
Patch14: 0015-BUG-MINOR-stream_interface-don-t-call-chk_snd-on-pol.patch
Patch15: 0016-OPTIM-splicing-use-splice-for-the-last-block-when-re.patch
Patch16: 0017-MEDIUM-sample-handle-comma-delimited-converter-list.patch
Patch17: 0018-MINOR-sample-fix-sample_process-handling-of-unstable.patch
Patch18: 0019-CLEANUP-acl-move-the-3-remaining-sample-fetches-to-s.patch
Patch19: 0020-MINOR-sample-add-a-new-date-fetch-to-return-the-curr.patch
Patch20: 0021-MINOR-samples-add-the-http_date-offset-sample-conver.patch
Patch21: 0022-DOC-minor-improvements-to-the-part-on-the-stats-sock.patch
Patch22: 0023-MEDIUM-sample-systematically-pass-the-keyword-pointe.patch
Patch23: 0024-MINOR-payload-split-smp_fetch_rdp_cookie.patch
Patch24: 0025-MINOR-counters-factor-out-smp_fetch_sc-_tracked.patch
Patch25: 0026-MINOR-counters-provide-a-generic-function-to-retriev.patch
Patch26: 0027-MEDIUM-counters-factor-out-smp_fetch_sc-_get_gpc0.patch
Patch27: 0028-MEDIUM-counters-factor-out-smp_fetch_sc-_gpc0_rate.patch
Patch28: 0029-MEDIUM-counters-factor-out-smp_fetch_sc-_inc_gpc0.patch
Patch29: 0030-MEDIUM-counters-factor-out-smp_fetch_sc-_clr_gpc0.patch
Patch30: 0031-MEDIUM-counters-factor-out-smp_fetch_sc-_conn_cnt.patch
Patch31: 0032-MEDIUM-counters-factor-out-smp_fetch_sc-_conn_rate.patch
Patch32: 0033-MEDIUM-counters-factor-out-smp_fetch_sc-_conn_cur.patch
Patch33: 0034-MEDIUM-counters-factor-out-smp_fetch_sc-_sess_cnt.patch
Patch34: 0035-MEDIUM-counters-factor-out-smp_fetch_sc-_sess_rate.patch
Patch35: 0036-MEDIUM-counters-factor-out-smp_fetch_sc-_http_req_cn.patch
Patch36: 0037-MEDIUM-counters-factor-out-smp_fetch_sc-_http_req_ra.patch
Patch37: 0038-MEDIUM-counters-factor-out-smp_fetch_sc-_http_err_cn.patch
Patch38: 0039-MEDIUM-counters-factor-out-smp_fetch_sc-_http_err_ra.patch
Patch39: 0040-MEDIUM-counters-factor-out-smp_fetch_sc-_kbytes_in.patch
Patch40: 0041-MEDIUM-counters-factor-out-smp_fetch_sc-_bytes_in_ra.patch
Patch41: 0042-MEDIUM-counters-factor-out-smp_fetch_sc-_kbytes_out.patch
Patch42: 0043-MEDIUM-counters-factor-out-smp_fetch_sc-_bytes_out_r.patch
Patch43: 0044-MEDIUM-counters-factor-out-smp_fetch_sc-_trackers.patch
Patch44: 0045-MINOR-session-make-the-number-of-stick-counter-entri.patch
Patch45: 0046-MEDIUM-counters-support-passing-the-counter-number-a.patch
Patch46: 0047-MEDIUM-counters-support-looking-up-a-key-in-an-alter.patch
Patch47: 0048-MEDIUM-cli-adjust-the-method-for-feeding-frequency-c.patch
Patch48: 0049-MINOR-cli-make-it-possible-to-enter-multiple-values-.patch
Patch49: 0050-MINOR-payload-allow-the-payload-sample-fetches-to-re.patch
Patch50: 0051-BUG-MINOR-use-the-same-check-condition-for-server-as.patch
Patch51: 0052-BUG-MINOR-cli-clear-table-must-not-kill-entries-that.patch
Patch52: 0053-MINOR-ssl-use-MAXPATHLEN-instead-of-PATH_MAX.patch
Patch53: 0054-MINOR-config-warn-when-a-server-with-no-specific-por.patch
Patch54: 0055-BUG-MEDIUM-unique_id-HTTP-request-counter-must-be-un.patch
Patch55: 0056-BUG-MEDIUM-unique_id-junk-in-log-on-empty-unique_id.patch
Patch56: 0057-BUG-MINOR-log-junk-at-the-end-of-syslog-packet.patch
Patch57: 0058-DOC-add-a-mention-about-the-limited-chunk-size.patch
Patch58: 0059-MINOR-ssl-Add-statement-verifyhost-to-server-stateme.patch
Patch59: 0060-BUG-MEDIUM-fix-broken-send_proxy-on-FreeBSD.patch
Patch60: 0061-MEDIUM-stick-tables-flush-old-entries-upon-soft-stop.patch
Patch61: 0062-MINOR-tcp-add-new-close-action-for-tcp-response.patch
Patch62: 0063-MINOR-payload-provide-the-res.len-fetch-method.patch
Patch63: 0064-BUILD-add-SSL_INC-SSL_LIB-variables-to-force-the-pat.patch
Patch64: 0065-BUG-MEDIUM-ssl-potential-memory-leak-using-verifyhos.patch
Patch65: 0066-BUILD-ssl-compilation-issue-with-openssl-v0.9.6.patch
Patch66: 0067-BUG-MINOR-fix-forcing-fastinter-in-on-error.patch

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
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1

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
