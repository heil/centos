#
# spec file for quilt - patch management scripts
#
%{!?dist: %define dist .fc3}
%{!?fedora: %define fedora 3}

Name:		quilt
Summary:	Scripts for working with series of patches
License:	GPL
Group:		Development/Tools
Version:	0.40
Release:	2%{?dist}
Source:		http://savannah.nongnu.org/download/quilt/quilt-%{version}.tar.gz
URL:		http://savannah.nongnu.org/projects/quilt
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gettext
Requires: coreutils
Requires: diffutils
Requires: gzip
Requires: bzip2
Requires: sed
Requires: gawk
Requires: diffstat
Requires: %{_sbindir}/sendmail
Requires: util-linux
Requires: tar
Requires: rpm-build

%description
These scripts allow one to manage a series of patches by keeping track of the
changes each patch makes. Patches can be applied, un-applied, refreshed, etc.

The scripts are heavily based on Andrew Morton's patch scripts found at
http://www.zip.com.au/~akpm/linux/patches/

%prep
%setup

%build
%configure --with-mta=%{_sbindir}/sendmail --with-diffstat=%{_bindir}/diffstat
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install BUILD_ROOT=$RPM_BUILD_ROOT
%{find_lang} %{name}
mv $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}/* .
rm -rf $RPM_BUILD_ROOT/%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc README README.MAIL quilt.pdf
%doc AUTHORS BUGS COPYING TODO
%{_bindir}/guards
%{_bindir}/quilt
%{_datadir}/quilt/
%{_libdir}/quilt/
%{_sysconfdir}/bash_completion.d
%config %{_sysconfdir}/quilt.quiltrc
%{_mandir}/man1/*

%changelog
* Wed May 4 2005 - jwboyer@jdub.homelinux.org 0.40-2
- Bump release to fix dist tag usage

* Tue May 3 2005 - jwboyer@jdub.homelinux.org 0.40-1
- Update to 0.40
- Remove fix-man-page.patch as it's now upstream
- Fix release numbering for multiple distro version

* Fri Apr 22 2005 - jwboyer@jdub.homelinux.org 0.39-7
- Bump release to be higher than FC-3 branch

* Thu Apr 21 2005 - jwboyer@jdub.homelinux.org 0.39-5
- Add rpm-build requires back for setup function.  rpm-build needs patch and
  perl, so remove explict requires.

* Tue Apr 5 2005 - jwboyer@jdub.homelinux.org 0.39-4
- Remove some Requires.  coreutils needs grep and findutils. rpm-build isn't
  really needed.  gzip needs mktemp.
- Remove the Authors from the description to make it more Fedora like.
- Get rid of old character set warning in man page

* Sun Apr 3 2005 - jwboyer@jdub.homelinux.org 0.39-3
- Add dependency on perl for the graph, mail, and setup functions

* Fri Apr 1 2005 Toshio Kuratomi <toshio-tiki-lounge.com> 0.39-2
- Full URL for Source.
- Changed some of the entries in the %%files section to own more directories,
  add more docs, and mark config files as config.
- Add some BuildRequires, configure switches and Requires so various quilt
  commandline options work.

* Thu Mar 31 2005 - jwboyer@jdub.homelinux.org
- Adapt quilt spec file to Fedora Extras conventions
