Name:		kde4-macros
Version:	4.7.90
Release:	3
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



%changelog
* Tue Dec 20 2011 Zé <ze@mandriva.org> 4.7.90-3
+ Revision: 744015
- add back build type since the one set in cmake is now clean

* Mon Dec 19 2011 Zé <ze@mandriva.org> 4.7.90-2
+ Revision: 743658
- fix wrong paste

* Sun Dec 18 2011 Zé <ze@mandriva.org> 4.7.90-1
+ Revision: 743467
- bump version to match kde
- debug type is set in cmake and not to be set twice

* Fri Dec 02 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.7.80-6
+ Revision: 737243
- again, don't disable verbosity by default, by "definining locally", I meant ie.
  by adding '%%_cmake_verbose %%{nil}' to ~/.rpmmacros

* Thu Dec 01 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-5
+ Revision: 735958
- Disable verbose in kde

* Sun Nov 27 2011 Zé <ze@mandriva.org> 4.7.80-4
+ Revision: 733718
- clean end of the line

* Sat Nov 26 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.7.80-3
+ Revision: 733668
- don't override the default verbosity enabled by %%cmake macro, if you don't want
  build output, you can disable this privately with the %%_cmake_verbose macro

* Fri Nov 25 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-2
+ Revision: 733274
- Revert CMAKE_VERBOSE_MAKEFILE change to set it to OFF by default in kde builds

* Sun Nov 20 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 731984
- Update to kde version
- Revert mandir part

* Sun Nov 20 2011 Zé <ze@mandriva.org> 4.6.5-2
+ Revision: 731982
- clean BR, defattr and clean setion.
- fix kde man path
- fix dbus interfaces path
- remove cmake option to enable verbosity that should be handled in cmake and not repeat the same entry

* Thu Jul 07 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.6.5-1
+ Revision: 689133
- Make cmake quite in kde4 build

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 4.4.95-2
+ Revision: 666016
- mass rebuild

* Mon Aug 02 2010 Funda Wang <fwang@mandriva.org> 4.4.95-1mdv2011.0
+ Revision: 564932
- back to debug mode

* Mon May 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.4.3-1mdv2010.1
+ Revision: 545737
- Rebuild KDE in Release mode

* Wed Dec 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.3.85-1mdv2010.1
+ Revision: 481679
- Build in debug mode

  + Helio Chissini de Castro <helio@mandriva.com>
    - Not support older builds than 2009.0

* Thu Aug 27 2009 Helio Chissini de Castro <helio@mandriva.com> 4.3.1-1mdv2010.0
+ Revision: 421588
- Remember to add FAM support

* Tue Mar 31 2009 Helio Chissini de Castro <helio@mandriva.com> 4.2.2-1mdv2009.1
+ Revision: 363093
- Remove fatness to enable Release mode, since macros are now cascadeing %%cmake
  macros

* Sat Feb 28 2009 Helio Chissini de Castro <helio@mandriva.com> 4.2.1-1mdv2009.1
+ Revision: 345847
- Solved the TODO of Debug/Release

* Mon Dec 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.85-1mdv2009.1
+ Revision: 317716
- Use debug to help finding solution to bugs

* Fri Nov 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.73-1mdv2009.1
+ Revision: 302951
- Remove unneeded macro
- Add a TODO comment

* Mon Nov 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.71-3mdv2009.1
+ Revision: 301668
- It is cooker so enable debug to allow us to debug easily

* Sun Oct 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.71-2mdv2009.1
+ Revision: 297485
- Fix non release build

* Sun Oct 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.71-1mdv2009.1
+ Revision: 297441
- Build with debug output for now

* Mon Sep 29 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.2-1mdv2009.0
+ Revision: 289729
- Force cmake build type as release, as we don't want untranslated string coming with a nastry message

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-2mdv2009.0
+ Revision: 277381
- Enable final still broken

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1.1-1mdv2009.0
+ Revision: 277327
- Enable final
- Add _kde_applicationsdir

* Fri Jul 04 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1-12mdv2009.0
+ Revision: 231693
- Added kde plugindir, since last kde4 style Rodrigo package need it

* Fri Jun 20 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1-11mdv2009.0
+ Revision: 227357
- Data dir for kde4 is apps dir, not datadir

* Fri Jun 20 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1-10mdv2009.0
+ Revision: 227322
- Little brainstorm with nanar and anssi produced the solutions that i needed for at least for 2008.1
- Old and new distros now
- Datadir and Mandriva release

* Thu Jun 19 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1-8mdv2009.0
+ Revision: 226808
- Now we have a KDE_DEFAULT_HOME var for cmake

* Mon Jun 16 2008 Anssi Hannula <anssi@mandriva.org> 4.1-7mdv2009.0
+ Revision: 220360
- add -DCMAKE_SKIP_RPATH=ON to %%cmake_kde4 (kde4 has its own rpath
  handling that often adds bad rpath=/usr/lib:/lib even though cmake's
  own handling would not do that; this may also fix accelerated GL with
  non-mesa libGL.so.1, if such problems were present)

* Tue Jun 10 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1-6mdv2009.0
+ Revision: 217770
- Proper interfaces dir

* Fri Jun 06 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1-5mdv2009.0
+ Revision: 216543
- Finish implementation of new flags for bug https://qa.mandriva.com/show_bug.cgi?id=41284

* Mon Jun 02 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1-4mdv2009.0
+ Revision: 214393
- Proper man dir

* Mon Apr 28 2008 Helio Chissini de Castro <helio@mandriva.com> 4.1-3mdv2009.0
+ Revision: 198239
- Fixing bug https://qa.mandriva.com/show_bug.cgi?id=40434 ( Invalid CFLAGS export )
- Removed CXXFLAGS export, we need only CPPFLAGS
- Added -DPIC on defines
- Added services and servicetypes on macros
- Starting to push new infrastructure for devel KDE 4.1. KDE 4 will be on / now. KDE is dead. Long live KDE vi kdenetwork4/SPECS/kdenetwork4.spec ;-)

* Sat Feb 09 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.1-1mdv2008.1
+ Revision: 164600
- Update to kde 4.0.1

* Thu Feb 07 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.0-3mdv2008.1
+ Revision: 163717
- We're not ready for enable final...

* Wed Feb 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0.0-2mdv2008.1
+ Revision: 162941
- Build w/o debug now

* Wed Jan 09 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.0-1mdv2008.1
+ Revision: 147322
- cmake >= 2.5.0 is needed

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.94.1-1mdv2008.1
+ Revision: 101361
- let us have debug on cooker for now

* Wed Sep 05 2007 Helio Chissini de Castro <helio@mandriva.com> 3.93.0-1mdv2008.0
+ Revision: 80294
- 3.93.0. Not compiling packages as debug anymore unless stated

* Tue Jul 31 2007 Helio Chissini de Castro <helio@mandriva.com> 3.92-1mdv2008.0
+ Revision: 57192
- CFLAGS -> CPPFLAGS

* Mon Jul 23 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-7mdv2008.0
+ Revision: 54789
- DBUS install defines changed

* Fri Jul 20 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-6mdv2008.0
+ Revision: 53991
- Move debug, pie and final for macros. Now we just need add %%cmake_kde4 to compile. Debug is enabled by default and final is disabled by default until release candidates.

* Tue Jul 03 2007 Helio Chissini de Castro <helio@mandriva.com> 3.91-5mdv2008.0
+ Revision: 47553
- Not break mkdir in already existent dirs

* Mon Jul 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.91-4mdv2008.0
+ Revision: 47172
+ rebuild (emptylog)

* Sun Jul 01 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.91-3mdv2008.0
+ Revision: 46407
- Fix dbus install

* Thu Jun 28 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.91-2mdv2008.0
+ Revision: 45437
- Fix typo (thanks Anssi)

* Thu Jun 28 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.91-1mdv2008.0
+ Revision: 45423
- Update to Kde4 3.91
- Add macros for sbin and include dir

* Tue Jun 19 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-10mdv2008.0
+ Revision: 41594
- Added -fPIC on common flags for kde4 compilation

* Sat Jun 16 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-9mdv2008.0
+ Revision: 40313
+ rebuild (emptylog)

* Sat Jun 16 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-8mdv2008.0
+ Revision: 40271
- Move services dbus dir to system have proper detection
- Make icons back to opt/kde4 root dir

* Fri Jun 15 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-7mdv2008.0
+ Revision: 40113
- Add appsdir on macros

* Fri Jun 08 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-6mdv2008.0
+ Revision: 37492
- Nope, we can't move kde4 out of their jail yet. Even libs gone to kde prefix.

* Fri Jun 08 2007 Helio Chissini de Castro <helio@mandriva.com> 3.90.2-5mdv2008.0
+ Revision: 37309
- Sane macros. For while, only libraries and icons will sit under /. KDE 4 basedir is /opt/kde4
- Prope datadir
- Base macros for kde4. First release
- import kde4-macros-3.90.2-1mdv2008.0


