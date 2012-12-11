%define upstream_name    Catalyst-Model-LDAP
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Catalyst LDAP Model Class
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Catalyst) >= 5.5
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Net::LDAP)
BuildRequires:	perl(Net::LDAP::Constant)
BuildRequires:	perl(NEXT)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This is the Net::LDAP model class for Catalyst. It is nothing more than a
simple wrapper for Net::LDAP.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
##%__make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.170.0-2mdv2011.0
+ Revision: 680722
- mass rebuild

* Sat Dec 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 473716
- update to 0.17

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 401761
- rebuild using %%perl_convert_version
- fixed license field

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.16-3mdv2009.0
+ Revision: 255521
- rebuild

* Fri Feb 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2008.1
+ Revision: 173879
- update to new version 0.16

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.15-1mdv2008.0
+ Revision: 19286
- Fix Spec file
-New version


* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 01:46:05 (54286)
- Rebuild, spec file cleanup

* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 01:42:38 (54284)
- import perl-Catalyst-Model-LDAP-0.14-2mdk

* Thu May 04 2006 Scott Karns <scottk@mandriva.org> 0.14-2mdk
- Adjusted BuildRequies
- Adjusted to comply with Mandriva perl packaging policies

* Wed Mar 08 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.14-1mdk
- 0.14

* Mon Mar 06 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.12-1mdk
- 0.12

* Mon Feb 27 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.10-1mdk
- 0.10

* Thu Feb 02 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.09-1mdk
- Initial MDV RPM

