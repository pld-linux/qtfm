Summary:	Qt File Manager
Summary(pl.UTF-8):	Menedzer plików Qt
Name:		qtfm
Version:	5.0
Release:	1
License:	GPL
URL:		http://www.qtfm.org/
Source0:	http://www.qtfm.org/%{name}-%{version}.tar.gz
# Source0-md5:	ad8e6d2d1533b2b1327cda557251a35d
Group:		X11/Applications
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qtFM - Small, fast, light Qt filemanager.

%description -l pl.UTF-8
qtFM - Mały, szybki i lekki menedżer plików oparty o Qt.

%prep
%setup -q

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}*.desktop
%{_pixmapsdir}/%{name}.png
