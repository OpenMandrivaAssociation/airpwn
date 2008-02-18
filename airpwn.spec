%define	name	airpwn
%define version	1.3
%define	release	%mkrel 1

Summary:	Generic packet injection tool for wireless networks
Name:		%{name}
Epoch:		1
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
URL:		http://sf.net/projects/%{name}
Source:		%{name}-%{version}.tgz
Patch:		airpwn-1.3-use-wireless-tools-header.patch
BuildRequires:	libpcap-devel
BuildRequires:	lorcon-devel
BuildRequires:	net-devel
BuildRequires:	pcre-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Airpwn is a generic packet injection tool for wireless networks.

%prep
%setup -q
%patch -p1 -b .use-wireless-tools-header

%build
%configure
%make

%install
rm -rf %{buildroot}
mkdir -p \
	%{buildroot}%{_bindir} \
	%{buildroot}%{_mandir}/man1 \
	%{buildroot}%{_sbindir} \
	%{buildroot}%{_datadir}/%{name}

install -m 644 airpwn.1 %{buildroot}%{_mandir}/man1/
install -s airpwn %{buildroot}%{_sbindir}
install -s atheros_prep.sh %{buildroot}%{_bindir}
install -s conf/* %{buildroot}%{_datadir}/%{name}

rm %{buildroot}%{_datadir}/%{name}/README

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%{_bindir}/*
%{_mandir}/man1/*
%{_sbindir}/*
%{_datadir}/airpwn

