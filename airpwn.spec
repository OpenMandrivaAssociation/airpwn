%define	name	airpwn
%define version	1.3
%define	release	%mkrel 2

Summary:	Generic packet injection tool for wireless networks
Name:		%{name}
Epoch:		1
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
URL:		http://sf.net/projects/%{name}
Source:		%{name}-%{version}.tgz
Patch:		airpwn-1.3-wireless.h-build-fix.patch
BuildRequires:	libiw-devel
BuildRequires:	libpcap-devel
BuildRequires:	lorcon-devel
BuildRequires:	net-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Airpwn is a generic packet injection tool for wireless networks.

%prep
%setup -q
%patch -p1 -b .wireless.h-build-fix

%build
%configure
%make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 755 atheros_prep.sh %{buildroot}%{_bindir}
install -m 644 conf/* %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%{_bindir}/*
%{_mandir}/man1/*
%{_sbindir}/*
%{_datadir}/airpwn

