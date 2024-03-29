Name:		kde4-macros
Version:	16.12.0
Release:	2
Group:		Development/KDE and Qt
Summary:	Base install macros for kde 4
License:	GPL
URL:		%{disturl}
Source0:	kde4.macros
BuildArch:	noarch
Requires:	cmake >= 2.6.2
Requires:	distro-release

%description
Base install macros for KDE 4.

%install
install -m644 %{SOURCE0} -D %{buildroot}%{_sysconfdir}/rpm/macros.d/kde4.macros

%files 
%{_sysconfdir}/rpm/macros.d/kde4.macros
