Summary:	Luminance Panel is a small panel application based on the fbpanel
Summary(pl):	Luminance Panel to ma³y panel oparty o fbpanel
Name:		luminance-panel
Version:	0.0.6
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/luminance/%{name}-%{version}.tar.gz
# Source0-md5:	79cbf3c0180d323f433bfafb5dee13ef
URL:		http://luminance.sourceforge.net/
BuildRequires:	atk-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Luminance Panel is a small panel application based on the fbpanel.

%description -l pl
Luminence Panel to ma³y panel oparty o fbpanel.

%prep
%setup -q

%build
%{__aclocal}
%{__automake}
%{__autoconf}
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
%doc AUTHORS ChangeLog INSTALL README
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_datadir}/%{name}
