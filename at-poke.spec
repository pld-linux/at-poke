Summary:	Tool for poking around with accessibility support
Summary(pl):	Narzêdzie do gmerania ze wsparciem dla u³atwieñ dostêpu
Name:		at-poke
Version:	0.2.2
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	e8e1c2907b96ded42f81ab045728a8d7
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	at-spi-devel >= 1.3.12
BuildRequires:	gail-devel
BuildRequires:	gcc-c++
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libgail-gnome-devel
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	popt-devel >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a tool for poking around with accessibility support.

%description -l pl
Narzêdzie do gmerania ze wsparciem dla u³atwieñ dostêpu.

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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
