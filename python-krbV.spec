%{!?python_sitearch: %global python_sitearch %([ -x %{__python} ] && %{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)" || :)}

Name: python-krbV
Version: 1.0.90
Release: 3%{?dist}
Summary: Python extension module for Kerberos 5

Group: Development/Languages
License: LGPLv2+

URL: http://fedorahosted.org/python-krbV/
Source: http://fedorahosted.org/python-krbV/attachment/wiki/Releases/python-krbV-%{version}.tar.bz2

BuildRequires: python-devel
BuildRequires: krb5-devel >= 1.2.2
BuildRequires: /bin/awk

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
python-krbV allows python programs to use Kerberos 5 authentication
and security.

%prep
%setup -q

%build
export LIBNAME="%{_lib}"
export CFLAGS="%{optflags} -Wextra"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}/%{python_sitearch}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING krbV-code-snippets.py
%{python_sitearch}/krbVmodule.so

%changelog
* Thu Jan  6 2011 John Dennis <jdennis@redhat.com> - 1.0.90-3
- Related: bug 642414
  Fix rpmlint complaint about description line too long

* Tue Jan  4 2011 John Dennis <jdennis@redhat.com> - 1.0.90-2
- Resolves: bug 642414
  Update to latest upstream release (includes the following)
  - return the contents of the AP_REP message from rd_rep()
  - improved memory handling
  - removed use of KRB_PRIVATE
  - better docstrings

* Tue Jun  1 2010 Dennis Gregorovic <dgregor@redhat.com> - 1.0.13-11
- Adjust for /usr/lib64
- Bump for rebuild
- Related: rhbz#566527

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.13-8
- Rebuild for Python 2.6

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.13-7
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Mike Bonnet <mikeb@redhat.com> - 1.0.13-6
- rebuild for F8

* Mon Dec 11 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-5
- rebuild for python 2.5
- remove obsolete python-abi Requires:

* Wed Sep 13 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-4
- support building against krb5-1.5, where the headers have been moved to /usr/include/krb5

* Mon Sep 11 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-3
- rebuild for FC6

* Sun May 21 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-2
- spec file cleanup

* Wed May 21 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.13-1
- AuthContext.addrs can now be set manually, rather than calling genaddrs()

* Sun May 21 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.12-3
- use macros consistently

* Thu Apr 27 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.12-2
- configure.in: parse version number out of spec file
- add URL tag
- add LGPL text
- remove Requires: krb5-libs, let rpm pick up library dependencies
- bump revision

* Mon Apr 24 2006 Mike Bonnet <mikeb@redhat.com> - 1.0.12-1
- bump version number due to API changes

* Fri Mar 24 2006 Mike Bonnet <mikeb@redhat.com>
- fix typo in error definition
- change the return value of recvauth() from ac to (ac, princ), where princ is the principal sent by sendauth()
- rename the package and reorganize the BuildRequires, to be more Extras-friendly

* Tue Sep 25 2001 Elliot Lee <sopwith@redhat.com>
- Initial version
