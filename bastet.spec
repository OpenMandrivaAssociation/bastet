Name:		bastet
Version:	0.43.2
Release:	1
License:	GPLv3+
Summary:	Tetris clone giving you the worst bricks possible
Group:		Games/Other
Url:		http://fph.altervista.org/prog/bastet.html
Source0:	http://fph.altervista.org/prog/files/%{name}-%{version}.tar.gz
Patch0: bastet-tr1.patch

BuildRequires:  ncurses-devel
BuildRequires:	boost-devel

%description
Bastet stands for "bastard tetris", and is a simple ncurses-based Tetris(R)
clone for Linux. Instead of choosing the next block randomly, this fiendish
program uses a special algorithm to give you the worst possible brick.
Playing Bastet can be a very frustrating experience!

%prep
%setup -q

%build
%autopatch -p1
%serverbuild
%make

%install
# binary
mkdir -p %{buildroot}%{_bindir}
install -p bastet %{buildroot}%{_bindir}/bastet

# empty high score file
mkdir -p %{buildroot}%{_var}/%{_gamesdir}
touch %{buildroot}%{_var}/%{_gamesdir}/%{name}.scores2

# manpage
mkdir -p %{buildroot}%{_mandir}/man6
install -p %{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6 

%files
%doc AUTHORS NEWS README
%attr(2755,root,games) %{_bindir}/%{name}
%attr(664,root,games) %{_var}/%{_gamesdir}/%{name}.scores2
%{_mandir}/man6/%{name}.*



%changelog
* Fri Jun 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.43-4
+ Revision: 803550
- rebuild for boost libs
- cleaned up spec

* Mon Mar 14 2011 Funda Wang <fwang@mandriva.org> 0.43-3
+ Revision: 644475
- rebuild for new boost

* Mon Aug 23 2010 Funda Wang <fwang@mandriva.org> 0.43-2mdv2011.0
+ Revision: 572152
- rebuild for new boost

* Fri Mar 05 2010 Jani Välimaa <wally@mandriva.org> 0.43-1mdv2011.0
+ Revision: 514788
- new version 0.43
- drop unneeded patches
- add missing BR
- change description
- fix license
- add url

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.41-6mdv2010.0
+ Revision: 436806
- rebuild

* Wed Apr 01 2009 Nicolas Vigier <nvigier@mandriva.com> 0.41-5mdv2009.1
+ Revision: 363329
- fix Summary

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.41-4mdv2009.0
+ Revision: 243166
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.41-2mdv2008.1
+ Revision: 171453
- BuildRequires: curses-devel
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Nicolas Vigier <nvigier@mandriva.com>
    - Import bastet

