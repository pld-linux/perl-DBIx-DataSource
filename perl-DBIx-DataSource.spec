%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	DataSource
Summary:	DBIx::DataSource -- Database-independant create and drop functions
Summary(pl):	DBIx::DataSource -- niezale�ne od bazy danych funkcje do tworzenia i usuwania
Name:		perl-%{pdir}-%{pnam}
Version:	0.02
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements create_database and drop_database functions for
databases.  It aims to provide a common interface to database creation
and deletion regardless of the actual database being used.

%description -l pl
Ten modu� jest implementacj� funkcji create_database i drop_database
dla baz danych. Celem jego jest dostarczenie wsp�lnego interfejsu do
tworzenia i usuwania baz danych, niezale�nego od u�ywanej bazy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*