Name: tw_cli
Version: 10
%define pkgversion 1
Release: 9000%{?dist}
Summary: 3ware Command Line Interface Tool
Group: System Environment/Base
License: 3ware
URL: http://www.3ware.com/
#Source0: http://www.3ware.com/download/Escalade9550SX-Series/%{pkgversion}/tw_cli-linux-x86-%{pkgversion}.tgz
#Source1: http://www.3ware.com/download/Escalade9550SX-Series/%{pkgversion}/tw_cli-linux-x86_64-%{pkgversion}.tgz
#Source0: http://www.3ware.com/download/Escalade9750SX-Series/%{pkgversion}/cli_linux_10.1.zip
Source1: http://www.3ware.com/download/Escalade9750SX-Series/%{pkgversion}/cli_linux_10.1.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
tw_cli is a Command Line Interface Storage Management Software for
AMCC/3ware ATA RAID Controller(s). It provides controller, logical
unit and drive management. tw_cli can be used in both interactive and
batch mode, providing higher-level API (Application Programming
Interface) functionalities.


%prep
%setup -q -c -T -a1
perl -pi -e's,^ *use v5.6.0.*,,' tw_sched

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/sbin
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sysconfdir}
install -p -m 0755 x86_64/tw_cli %{buildroot}/sbin/
#install -p -m 0755 tw_sched %{buildroot}/sbin/
install -p -m 0644 tw_cli.8.nroff %{buildroot}%{_mandir}/man8/tw_cli.8
#install -p -m 0644 tw_sched.8.nroff %{buildroot}%{_mandir}/man8/tw_sched.8
#install -p -m 0644 tw_sched.cfg %{buildroot}%{_sysconfdir}/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc *.html
/sbin/*
%{_mandir}/man8/*.8*
#%config(noreplace) %{_sysconfdir}/tw_sched.cfg


%changelog
* Thu Feb  9 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.

