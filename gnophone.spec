# TODO:
# - zaptel (-lzap -ltonezone)
#
# Conditional build:
%bcond_without	esd	# without esound
#
Summary:	Gnophone Open Source Communicator
Summary(pl.UTF-8):	Gnophone - komunikator Open Source
Name:		gnophone
Version:	0.2.4
Release:	1
License:	LGPL/GPL
Group:		Applications/Communications
Source0:	ftp://ftp.gnophone.com/pub/gnophone/%{name}-%{version}.tar.gz
#Source0-md5:	75cee76acbd930ccdf473352b1beab30
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-gcc33.patch
Patch2:		%{name}-switch.patch
URL:		http://www.gnophone.com/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_esd:BuildRequires:   esound-devel}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	iax-devel
BuildRequires:	imlib-devel
BuildRequires:	libgsm-devel
BuildRequires:	libtool
BuildRequires:	nspr-devel
BuildRequires:	sox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnophone is an Open Source Internet telephone and more that allows you
to make calls to other GnoPhone users or to an Asterisk PBX Gateway.
It supports a fully featured web interface allowing you to participate
in various discussion groups. It also supports the full rate GSM codec
for great quality that doesn't require very high bandwidth.

%description -l pl.UTF-8
Gnophone jest Internetowym telefonem IP, pozwalającym na telefonowanie
do innych GnoPhone'ów lub do bramek Asterisk PBX. Ma w pełni
funkcjonalny interfejs WWW, który pozwala uczestniczyć w różnych
grupach dyskusyjnych. Obsługuje także całkowicie kodek GSM, który nie
potrzebuje do uzyskania dobrej jakości dużego pasma.

%package esd
Summary:	EsounD audio module for Gnophone
Summary(pl.UTF-8):	Moduł dźwięku EsounD dla Gnophone
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description esd
EsounD audio module for Gnophone.

%description esd -l pl.UTF-8
Moduł dźwięku EsounD dla Gnophone.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}  -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_esd:--disable-esd}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnophone
%attr(755,root,root) %{_bindir}/gnophone.bin
%dir %{_libdir}/gnophone
%{_libdir}/gnophone/images
%dir %{_libdir}/gnophone/modules
%attr(755,root,root) %{_libdir}/gnophone/modules/audio-oss.so
%attr(755,root,root) %{_libdir}/gnophone/modules/audio-phone.so

%if %{with esd}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnophone/modules/audio-esd.so
%endif
