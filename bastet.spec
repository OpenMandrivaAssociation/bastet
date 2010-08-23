%define name bastet
%define version 0.43
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv3+
Summary:	Tetris clone giving you the worst bricks possible
Group:		Games/Other
Url:		http://fph.altervista.org/prog/bastet.html
Source0:	http://fph.altervista.org/prog/files/%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
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
%serverbuild
%make

%install
rm -rf %{buildroot}

# binary
mkdir -p %{buildroot}%{_bindir}
install -p bastet %{buildroot}%{_bindir}/bastet

# empty high score file
mkdir -p %{buildroot}%{_var}/%{_gamesdir}
touch %{buildroot}%{_var}/%{_gamesdir}/%{name}.scores2

# manpage
mkdir -p %{buildroot}%{_mandir}/man6
install -p %{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README
%attr(2755,root,games) %{_bindir}/%{name}
%attr(664,root,games) %{_var}/%{_gamesdir}/%{name}.scores2
%{_mandir}/man6/%{name}.*
