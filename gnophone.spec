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
URL:		http://www.gnophone.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	iax-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnophone is an Open Source Internet telephone and more that allows you
to make calls to other GnoPhone users or to an Asterisk PBX Gateway.
It supports a fully featured web interface allowing you to participate
in various discussion groups. It also supports the full rate GSM codec
for great quality that doesn't require very high bandwidth.

%description -l pl
Gnophone jest Internetowym telefonem IP, pozwalaj�cym na telefonowanie
do innych GnoPhone-�w lub do bramek Asterisk PBX. Wspiera pe�ny
interfejs web-owy, kt�ry pozwala uczestniczy� w r�nych grupach
dyskusyjnych. Wspiera tak�e w pe�ni kodek GSM, kt�ry nie potrzebuje do
uzyskania dobrej jako�ci du�ego pasma.

%prep
%setup -q
%patch0 -p1

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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnophone
%attr(755,root,root) %{_bindir}/gnophone.bin
%dir %{_libdir}/gnophone
%dir %{_libdir}/gnophone/images
%{_libdir}/gnophone/images/*
%dir %{_libdir}/gnophone/modules
%{_libdir}/gnophone/modules/*
