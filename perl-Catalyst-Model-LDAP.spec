%define realname Catalyst-Model-LDAP
%define name	perl-%{realname}
%define	modprefix Catalyst

%define version	0.15
%define release	%mkrel 1

Summary:	Catalyst LDAP Model Class
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Carp)
BuildRequires:	perl(Catalyst) >= 5.5
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Net::LDAP)
BuildRequires:	perl(Net::LDAP::Constant)
BuildRequires:	perl(NEXT)
BuildRequires:	perl(Test::More)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is the Net::LDAP model class for Catalyst. It is nothing more than a
simple wrapper for Net::LDAP.

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
##%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%clean
rm -rf %{buildroot}



