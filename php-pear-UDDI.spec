%include	/usr/lib/rpm/macros.php
%define		_class		UDDI
%define		_status		alpha
%define		_pearname	%{_class}

Summary:	%{_pearname} - API for PHP
Summary(pl):	%{_pearname} - API dla PHP
Name:		php-pear-%{_pearname}
Version:	0.2.0
%define	_rc	alpha4
%define	_rel 2
Release:	1.%{_rc}.%{_rel}
License:	GPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	a637ca53ff82e4335ed234a017f098eb
URL:		http://pear.php.net/package/UDDI/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of Universal Description, Discovery and Integration API
for locating and publishing Web Services in a UBR (UDDI Business
Registry).

In PEAR status of this package is: %{_status}.

%description -l pl
Implementacja Universal Description, Discovery and Integration API
s³u¿±cego wyszukiwaniu i umieszczaniu us³ug sieciowych w rejestrze UBR
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
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
