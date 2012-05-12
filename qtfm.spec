Summary:	Qt File Manager
Summary(pl.UTF-8):	Menedzer plików Qt
Name:		qtfm
Version:	5.4
Release:	1
License:	GPL
URL:		http://www.qtfm.org/
Source0:	http://www.qtfm.org/%{name}-%{version}.tar.gz
# Source0-md5:	f3ec357ec11b1dbc67b942580ae14dd3
Group:		X11/Applications
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	libstdc++-devel
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
%lang(da) %{_datadir}/qtfm/qtfm_da.qm
%lang(de) %{_datadir}/qtfm/qtfm_de.qm
%lang(es) %{_datadir}/qtfm/qtfm_es.qm
%lang(fr) %{_datadir}/qtfm/qtfm_fr.qm
%lang(it) %{_datadir}/qtfm/qtfm_it.qm
%lang(pl) %{_datadir}/qtfm/qtfm_pl.qm
%lang(ru) %{_datadir}/qtfm/qtfm_ru.qm
%lang(sr) %{_datadir}/qtfm/qtfm_sr.qm
%lang(zh) %{_datadir}/qtfm/qtfm_zh.qm
%lang(zh_TH) %{_datadir}/qtfm/qtfm_zh_TW.qm
