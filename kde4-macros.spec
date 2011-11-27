Name:		kde4-macros
Version:	4.7.80
Release:	4
Group:		Development/KDE and Qt
Summary:	Base install macros for kde 4
License:	GPL
URL:		http://www.mandriva.com
Source0:	kde4.macros
BuildArch:	noarch
Requires:	cmake >= 2.6.2
Requires:	mandriva-release

%description
Base install macros for kde 4

%files 
%_sysconfdir/rpm/macros.d/kde4.macros

%install
rm -rf %buildroot
install -d -m 755 %buildroot%_sysconfdir/rpm/macros.d
install -m 644 %SOURCE0 %buildroot%_sysconfdir/rpm/macros.d/

