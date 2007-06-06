%define __libtoolize /bin/true

Name: kde4-macros
Summary: Base install macros for kde 4
Version: 3.90.2
Release: %mkrel 1
Source: kde4.macros
URL: http://www.mandriva.com
License: GPL
Group: Development/KDE and Qt
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Base install macros for kde 4

%files 
%defattr(-,root,root)
%_sysconfdir/rpm/macros.d/kde4.macros

%install
rm -rf %buildroot
install -d -m 755 %buildroot%_sysconfdir/rpm/macros.d
install -m 644 %SOURCE0 %buildroot%_sysconfdir/rpm/macros.d/

%clean
rm -rf %buildroot


