%define upstream_name	 Class-DBI-Plugin-AbstractCount
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Get COUNT(*) results with abstract SQL
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-SQL-Abstract >= 1.1
BuildRequires:  perl-Class-DBI-Plugin >= 0.02
BuildRequires:	perl-Class-DBI >= 0.95
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This Class::DBI plugin combines the functionality from
Class::DBI::Plugin::CountSearch (counting objects without
having to use an array or an iterator), and
Class::DBI::AbstractSearch, which allows complex
where-clauses a la SQL::Abstract.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Class
%{_mandir}/*/*
