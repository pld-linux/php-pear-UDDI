%define		_status		alpha
%define		_pearname	UDDI
Summary:	%{_pearname} - API for PHP
Summary(pl.UTF-8):	%{_pearname} - API dla PHP
Name:		php-pear-%{_pearname}
Version:	0.2.4
Release:	3
License:	GPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e6774c0fa6bf1cd2c097260fbfe860ae
URL:		http://pear.php.net/package/UDDI/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of Universal Description, Discovery and Integration API
for locating and publishing Web Services in a UBR (UDDI Business
Registry).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Implementacja Universal Description, Discovery and Integration API
służącego wyszukiwaniu i umieszczaniu usług sieciowych w rejestrze UBR
(UDDI Business Registry).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%dir %{php_pear_dir}/UDDI
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/UDDI/*.php
