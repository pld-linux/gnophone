Summary:	Gnophone Internet Phone
Name:		gnophone
Version:	0.2.4
Release:	1
License:	LGPL/GPL
Group:		Applications/Communications
Source0:	ftp://ftp.gnophone.com/pub/gnophone/%{name}-%{version}.tar.gz
#Source0-md5:	75cee76acbd930ccdf473352b1beab30
Patch0:		%{name}-destdir.patch
URL:		http://www.gnophone.com
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	iax-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
empty


%prep
%setup -q
%patch0 -p1
%build
rm -f missing
%{__libtoolize}
%{__aclocal}  -I m4
%{__autoconf}
%{__automake}
%configure \

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
