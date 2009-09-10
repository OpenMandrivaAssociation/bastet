%define name bastet
%define version 0.41
%define release %mkrel 6

Name:		%name
Version:	%version
Release:	%release
License:	GPL
Summary:	Tetris clone giving you the worst bricks possible
Group:		Games/Other
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires: ncurses-devel
Source0:	http://fph.altervista.org/prog/%{name}-%{version}.tgz
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-%{version}-cheat.patch
%description
Have you ever thought Tetris(R) was evil because it wouldn't send you
that straight "I" brick you needed in order to clear four rows at the
same time? Well Tetris(R) probably isn't evil, but Bastet certainly is. >:-)
Bastet stands for "bastard tetris", and is a simple ncurses-based Tetris(R)
clone for Linux. Unlike normal Tetris(R), however, Bastet does not choose
your next brick at random. Instead, Bastet uses a special algorithm
designed to choose the worst brick possible. As you can imagine, playing
Bastet can be a very frustrating experience!

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%make

%install
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_var}/%{_gamesdir}
make BIN_PREFIX=$RPM_BUILD_ROOT%{_bindir}/ DATA_PREFIX=$RPM_BUILD_ROOT%{_var}/%{_gamesdir}/ install

%clean
%{__rm} -Rf %{buildroot}

%files
%attr(2755,root,games) %{_bindir}/%{name}
%attr(664,root,games) %{_var}/%{_gamesdir}/%{name}.scores

