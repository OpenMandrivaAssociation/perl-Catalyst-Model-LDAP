%define upstream_name    Catalyst-Model-LDAP
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Catalyst LDAP Model Class
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is the Net::LDAP model class for Catalyst. It is nothing more than a
simple wrapper for Net::LDAP.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
##%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*
