#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	DBIx
%define		pnam	DataSource
%include	/usr/lib/rpm/macros.perl
Summary:	DBIx::DataSource - database-independent create and drop functions
Summary(pl.UTF-8):	DBIx::DataSource - niezależne od bazy danych funkcje do tworzenia i usuwania
Name:		perl-DBIx-DataSource
Version:	0.02
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	12d60ad75ceced40286d18fcdcb5a40b
URL:		http://search.cpan.org/dist/DBIx-DataSource/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements create_database and drop_database functions for
databases. It aims to provide a common interface to database creation
and deletion regardless of the actual database being used.

%description -l pl.UTF-8
Ten moduł jest implementacją funkcji create_database i drop_database
dla baz danych. Celem jego jest dostarczenie wspólnego interfejsu do
tworzenia i usuwania baz danych, niezależnego od używanej bazy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
