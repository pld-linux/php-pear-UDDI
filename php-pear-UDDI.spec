%include	/usr/lib/rpm/macros.php
%define         _class          UDDI
%define		_status		alpha
%define		_pearname	%{_class}

Summary:	%{_pearname} - API for PHP
Summary(pl):	%{_pearname} - API dla PHP
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	1
License:	GPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	81845ff73ae834ced032f1fb32f4e3da
URL:		http://pear.php.net/package/UDDI/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of Universal Description, Discovery and Integration API
for locating and publishing Web Services in a UBR (UDDI Business
Registry).

This class has in PEAR status: %{_status}.

%description -l pl
Implementacja Universal Description, Discovery and Integration API
s³u¿±cego wyszukiwaniu i umieszczaniu us³ug sieciowych w rejestrze UBR
(UDDI Business Registry).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
