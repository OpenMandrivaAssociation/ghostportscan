%define name ghostportscan
%define version 0.9.3
%define release %mkrel 8

Summary:	Ghost Port Scan Tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Networking/Other
Source:		http://gps.sourceforge.net/release/gps-%{version}-FRC.tar.bz2
URL:		http://gps.sourceforge.net
License:	GPL
BuildRequires:  libpcap-devel
BuildRequires:	libnet1.0.2-devel

%description
The aim of Ghost Port Scan is to provide administrators
and pen-testers with a tool that allow them to easily
test firewalls and get information from a remote host.

PS is a port scanner and a firewall rules disclosure 
(FWRD) tool, which uses IP spoofing, ARP poisoning and
some other technics in order to perform a stealth and
untrackable information collect.

As far as GPS needs to sniff the responses from the
target host, it requires to be run using a loopback or
an ethernet interface (including cable modem).

%prep
rm -rf ${buildroot}
%setup -q -n gps-%{version}-FRC

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall
mkdir  %{buildroot}/%{_sbindir}
mv %{buildroot}/%{_bindir}/gps %{buildroot}/%{_sbindir}/ghostportscan

%clean
rm -rf %{buildroot}

%files 
%defattr(644,root,root)
%doc AUTHORS ChangeLog README docs/* NEWS
%attr(755,root,root) %{_sbindir}/ghostportscan

