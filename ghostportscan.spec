Summary:	Ghost Port Scan Tool
Name:		ghostportscan
Version:	0.9.3
Release:	13
Group:		Networking/Other
Source:		http://gps.sourceforge.net/release/gps-%{version}-FRC.tar.bz2
URL:		http://gps.sourceforge.net
License:	GPL
BuildRequires:  pcap-devel
BuildRequires:	net1.0.2-devel = 1.0.2a-17

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
%setup -q -n gps-%{version}-FRC

%build
%configure
%make

%install
%makeinstall
mkdir  %{buildroot}/%{_sbindir}
mv %{buildroot}/%{_bindir}/gps %{buildroot}/%{_sbindir}/ghostportscan

%files 
%defattr(644,root,root)
%doc AUTHORS ChangeLog README docs/* NEWS
%attr(755,root,root) %{_sbindir}/ghostportscan



%changelog
* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-11mdv2009.1
+ Revision: 298255
- rebuilt against libpcap-1.0.0

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.3-10mdv2009.0
+ Revision: 246074
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.9.3-8mdv2008.1
+ Revision: 125690
- kill re-definition of %%buildroot on Pixel's request
- import ghostportscan


* Fri Mar 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-8mdk
- rebuilt against libnet1.0.2

* Thu Jul 28 2005 Michael Scherer <misc@mandriva.org> 0.9.3-7mdk
- add doc
- move to sbindir as it requires root privileges

* Thu Jul 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.3-6mdk
- Fix BuildRequires

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-5mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Thu Jun 03 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.9.3-4mdk
- rebuild

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9.3-3mdk
- rebuild

* Mon Apr 30 2002 Christian Belisle <cbelisle@mandrakesoft.com> 0.9.3-2mdk
- Fix spec errors (group & url).

* Mon Apr 29 2002 Christian Belisle <cbelisle@mandrakesoft.com> 0.9.3-1mdk
- First Mandrake release
