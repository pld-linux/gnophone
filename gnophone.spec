# TODO: zaptel (-lzap -ltonezone)
Summary:	Gnophone Open Source Communicator
Summary(pl):	Gnophone - komunikator Open Source
Name:		gnophone
Version:	0.2.4
Release:	1
License:	LGPL/GPL
Group:		Applications/Communications
Source0:	ftp://ftp.gnophone.com/pub/gnophone/%{name}-%{version}.tar.gz
#Source0-md5:	75cee76acbd930ccdf473352b1beab30
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-gcc33.patch
URL:		http://www.gnophone.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
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

%description -l pl
Gnophone jest Internetowym telefonem IP, pozwalaj±cym na telefonowanie
do innych GnoPhone'ów lub do bramek Asterisk PBX. Ma w pe³ni
funkcjonalny interfejs WWW, który pozwala uczestniczyæ w ró¿nych
grupach dyskusyjnych. Obs³uguje tak¿e ca³kowicie kodek GSM, który nie
potrzebuje do uzyskania dobrej jako¶ci du¿ego pasma.

%package esd
Summary:	EsounD audio module for Gnophone
Summary(pl):	Modu³ d¼wiêku EsounD dla Gnophone
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description esd
EsounD audio module for Gnophone.

%description esd -l pl
Modu³ d¼wiêku EsounD dla Gnophone.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}  -I m4
%{__autoconf}
%{__automake}
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
%attr(755,root,root) %{_bindir}/gnophone
%attr(755,root,root) %{_bindir}/gnophone.bin
%dir %{_libdir}/gnophone
%{_libdir}/gnophone/images
%dir %{_libdir}/gnophone/modules
%attr(755,root,root) %{_libdir}/gnophone/modules/audio-oss.so
%attr(755,root,root) %{_libdir}/gnophone/modules/audio-phone.so

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnophone/modules/audio-esd.so
