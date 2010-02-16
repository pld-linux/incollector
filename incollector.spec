Summary:	Information collector
Summary(pl.UTF-8):	Program do zbierania informacji
Name:		incollector
Version:	1.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.incollector.devnull.pl/download/sources/%{name}-%{version}.tar.gz
# Source0-md5:	6701ac13da29119cd6719be3edcf30aa
#Source1:	%{name}.desktop
URL:		http://www.incollector.devnull.pl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	gettext-devel
BuildRequires:	mono-csharp
BuildRequires:	perl-base
BuildRequires:	pkgconfig
Requires:	dotnet-gtk-sharp2 >= 2.8
Requires:	mono >= 1.2
Requires:	mono-csharp >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application to collect various kind of Information (like notes,
conversation logs, quotes, serial numbers, source code, webaddresses,
words). All entries can be tagged. Application can also search and
browse entries easly.

%description -l pl.UTF-8
Aplikacja do zbierania różnego rodzaju informacji (jak notatki, logi
rozmów, cytaty, numery seryjne, kody źródłowe, adresy w sieci, słowa).
Wszystkie wpisy mogą być znakowane. Program może wyszukiwać i łatwo
przeglądać wpisy.

%prep
%setup -q
%{__perl} -pi -e 's#> Engine/Defines.cs \\#> Engine/Defines.cs#' src/Makefile.am
%{__perl} -pi -e "s/lib/%{_lib}/" script.in

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

# ukrainian is uk
mv $RPM_BUILD_ROOT/%{_datadir}/locale/u{a,k}

%find_lang incollector

%clean
rm -rf $RPM_BUILD_ROOT

%files -f incollector.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/incollector
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
