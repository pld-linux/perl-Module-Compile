#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Compile
%include	/usr/lib/rpm/macros.perl
Summary:	Module::Compile - Perl Module Compilation
#Summary(pl.UTF-8):	
Name:		perl-Module-Compile
Version:	0.35
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7b9cf30692ab350d2ac013db55d9bc34
URL:		http://search.cpan.org/dist/Module-Compile/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-SHA1 >= 2.13
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a system for writing modules that compile other
Perl modules.

Modules that use these compilation modules get compiled into some
altered form the first time they are run. The result is cached into
.pmc files.

Perl has native support for .pmc files. It always checks for them, before
loading a .pm file.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Module/*.pm
%{perl_vendorlib}/Module/Compile
%{_mandir}/man3/*
