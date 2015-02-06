%define upstream_name	 Class-DBI-Plugin-AbstractCount
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Get COUNT(*) results with abstract SQL
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(SQL::Abstract)
BuildRequires:	perl(Class::DBI::Plugin)
BuildRequires:	perl(Class::DBI)
BuildRequires:	perl(Class::Accessor::Grouped)
BuildArch:	noarch

%description
This Class::DBI plugin combines the functionality from
Class::DBI::Plugin::CountSearch (counting objects without
having to use an array or an iterator), and
Class::DBI::AbstractSearch, which allows complex
where-clauses a la SQL::Abstract.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 681088
- add br
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 401705
- rebuild using %%perl_convert_version
- fixed license field

* Fri Jul 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2010.0
+ Revision: 391940
- update to new version 0.08

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.07-4mdv2009.0
+ Revision: 241182
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-2mdv2008.0
+ Revision: 86101
- rebuild


* Thu Jun 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2007.0
- New version 0.07
- rpmbuildupdate aware
- spec cleanup

* Sat Apr 08 2006 Arnaud de Lorbeau <devel@mandriva.com> 0.06-1mdk
- Initial MDV RPM

