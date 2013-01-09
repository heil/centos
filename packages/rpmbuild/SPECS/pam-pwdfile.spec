%define nam pam_pwdfile
%define ver 0.99
%define prefix /usr
%define debug_package %{nil}
%define docdir %{prefix}/doc/%{nam}-%{ver}

%define installer /usr/bin/install

Summary: A PAM module that allows users to authenticate on htpasswd-type files separate from /etc/passwd.
Name: pam_pwdfile
Version: %{ver}
Release: 9004.bas
License: LGPL
Group: System Environment/Base
Source0: %{nam}-%{ver}.tar.gz
Source1: Makefile.standalone
URL: http://cpbotha.net/pam_pwdfile.html
Distribution: Xeran Internal Packages
Vendor: Xeran Technologies
Packager: Jason F. McBrayer <jason@xeran.com>
BuildRoot:	/var/tmp/%{nam}-%{ver}-root
BuildPrereq: pam pam-devel
Requires: pam 

%description
This pam module can be used for the authentication service only, in cases
where one wants to use a different set of passwords than those in the main
system password database.  E.g. in our case we have an imap server running,
and prefer to keep the imap passwords different from the system passwords
for security reasons.

%prep
%setup
cp $RPM_SOURCE_DIR/Makefile.standalone $RPM_BUILD_DIR/%{nam}-%{ver}/Makefile.standalone

%build
make -f Makefile.standalone

%install
make -f Makefile.standalone PAM_LIB_DIR="$RPM_BUILD_ROOT/lib64/security" install

%files
%attr(0755, root, root) /lib64/security/pam_pwdfile.so
%attr(-, root, root) %doc README
%attr(-, root, root) %doc changelog
