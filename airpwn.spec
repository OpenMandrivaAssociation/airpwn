Summary:	Generic packet injection tool for wireless networks
Name:		airpwn
Epoch:		1
Version:	1.4
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/Other
URL:		http://sf.net/projects/airpwn
Source0:	%{name}-%{version}.tgz
BuildRequires:	libiw-devel
BuildRequires:	libpcap-devel
BuildRequires:	lorcon-devel
BuildRequires:  python2.4-devel
BuildRequires:	net-devel >= 1.1.3
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Airpwn is a generic packet injection tool for wireless networks.

%prep
%setup -q

%build
export LIBS="-lcrypto"
%configure
%make

%install
rm -rf %{buildroot}

%makeinstall_std

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}

install -m 755 madwifing_prep.sh %{buildroot}%{_bindir}
install -m 755 mac80211_prep.sh %{buildroot}%{_bindir}
rm -rf conf/CVS 
install -m 644 conf/* %{buildroot}%{_datadir}/%{name}
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README INSTALL
%{_bindir}/*
%{_mandir}/man1/*
%{_sbindir}/*
%{_datadir}/airpwn
