Summary:	Virtual Private Ethernet
Summary(pl.UTF-8):	Wirtualna sieć prywatna
Name:		gvpe
Version:	2.2
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnu.org/gnu/gvpe/%{name}-%{version}.tar.gz
# Source0-md5:	72d4dfdf87d5e4a5487aecc28e459b9f
URL:		http://savannah.gnu.org/projects/gvpe
BuildRequires:	libev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GVPE creates a virtual ethernet (broadcasts supported, any protocol
that works with a normal ethernet should work with GVPE) by creating
encrypted host-to-host tunnels between multiple endpoints.

Unlike other virtual private "network" solutions which merely create a
single tunnel, GVPE creates a real network with multiple endpoints.

It is designed to be very simple and robust (cipher selection done at
compiletime etc.), and easy to setup (only a single config file shared
unmodified between all hosts).

Vpn hosts can neither sniff nor fake packets, that is, you can use
MAC-based filtering to ensure authenticity of packets even from member
nodes.

GVPE can also be used to tunnel into some vpn network using a variety
of protocols (raw IP, UDP, TCP, HTTPS-proxy-connect, ICMP and DNS). It
is, however, primarily designed to sit on the gateway machines of
company branches to connect them together.

%description -l pl.UTF-8
GVPE tworzy wirtualną sieć ethernet (ze wsparciem dla broadcastów,
każdy protokół działający w obrębie sieci ethernet powinien działać z
GVPE) za pomocą szyfrowanych tuneli host-do-hosta pomiędzy wieloma
punktami.

W odróżnieniu od innych rozwiązań tego typu tworzących jedynie
pojedynczy tunel, GVPE umożliwia stworzenie sieci pomiędzy wieloma
punktami.

Zaprojektowany został w sposób prosty, ale jednocześnie wydajny (wybór
szyfru na poziomie kompilacji, itp.), jak również prosty do wdrożenia
(pojedynczy plik konfiguracyjny współdzielony pomiędzy końcówkami).

Końcówki VPN nie mogą podsłuchać ani sfałszować pakietów, dzięki czemu
możliwe jest zastosowanie filtrowania na podstawie MAC-adresów aby
zapewnić autentyczność pakietów pochodzących od hostów klienckich.

GVPE może byc także wykorzystane w celu tunelowania sieci VPN za
pomocą wielu protokołów (czyste IP, UDP, TCP, HTTPS poprzez PROXY,
ICMP czy DNS). Podstawowym jego zastosowaniem jest jednak
wykorzystanie na maszynach będących bramkami sieci (n.p. oddziałów
firmy).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_sbindir}/gvpe
%attr(755,root,root) %{_bindir}/gvpectrl
%{_infodir}/gvpe.info*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*
%{_mandir}/man8/*.8*
