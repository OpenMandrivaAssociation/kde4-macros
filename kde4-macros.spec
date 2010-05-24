Name: kde4-macros
Version: 4.4.3
Release: %mkrel 1
Group: Development/KDE and Qt
Summary: Base install macros for kde 4
Source: kde4.macros
URL: http://www.mandriva.com
Requires: cmake >= 2.6.2
Requires: mandriva-release
License: GPL
BuildArch: noarch
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


