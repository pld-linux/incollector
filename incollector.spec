Summary:	Information collector
Summary(pl):	Program do zbierania informacji
Name:		incollector
Version:	0.5
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.incollector.devnull.pl/download/sources/%{name}-%{version}.tar.gz
# Source0-md5:	ab7fa9bf12aecf2e10d50ccba96940ca
Source1:	%{name}.desktop
URL:		http://www.incollector.devnull.pl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	mono-csharp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application to collect various kind of Information (like notes,
conversation logs, quotes, serial numbers, source code, webaddresses,
words). All entries can be tagged. Application can also search and
browse entries easly.

%description -l pl
Aplikacja do zbierania ró¿nego rodzaju informacji (jak notatki, logi
rozmów, cytaty, numery seryjne, kody ¼ród³owe, adresy w sieci, s³owa).
Wszystkie wpisy mog± byæ znakowane. Program mo¿e wyszukiwaæ i ³atwo
przegl±daæ wpisy.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang incollector

%clean
rm -rf $RPM_BUILD_ROOT

%files -f incollector.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
