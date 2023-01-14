Name:		bastet
Version:	0.43.2
Release:	1
License:	GPLv3+
Summary:	Tetris clone giving you the worst bricks possible
Group:		Games/Other
Url:		http://fph.altervista.org/prog/bastet.html
#Source0:	http://fph.altervista.org/prog/files/%{name}-%{version}.tgz
Source0:	https://github.com/fph/bastet/archive/%{version}/%{name}-%{version}.tar.gz
# (fedora)
Patch0:		bastet-tr1.patch
# (fedora)
Patch1:		bastet-fmt-str.patch

BuildRequires:	imagemagick
BuildRequires:  ncurses-devel
BuildRequires:	boost-devel

%description
Bastet stands for "bastard tetris", and is a simple ncurses-based Tetris(R)
clone for Linux. Instead of choosing the next block randomly, this fiendish
program uses a special algorithm to give you the worst possible brick.
Playing Bastet can be a very frustrating experience!

%files
%license LICENSE
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/openmandriva-%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man6/*
%config(noreplace) %{_var}/%{_gamesdir}/%{name}.scores2

#--------------------------------------------------------------------

%prep
%autosetup -p1

# remove reference to Tetris
sed -e 's/Tetris(R)/any falling bricks game/g' -e 's/Tetris/falling bricks game/g' \
-e 's/tetris/falling bricks game/g' README > README.new
mv -f README.new README
# remove also any reference to Tetris in the bastet manpage
sed -e 's/Tetris(r)/any falling bricks game/g' -e 's/tetris/falling bricks game/g' \
bastet.6 > bastet.6.new
mv -f bastet.6.new bastet.6

%build
%set_build_flags
%make_build

%install
# binary
install -pm 0755 -d %{buildroot}%{_bindir}
install -pm 0755 bastet %{buildroot}%{_bindir}/bastet

# empty high score file
install -pm 0755 -d %{buildroot}%{_var}/%{_gamesdir}
touch %{buildroot}%{_var}/%{_gamesdir}/%{name}.scores2

# .desktop file
install -pm 0755 -d %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/openmandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=An evil falling bricks game
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;
X-Vendor=OpenMandriva
EOF

# icons
for d in 16 32 48 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
#	rsvg-convert -f png -h ${d} -w ${d} %{name}.svg \
#			-o %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
	convert -background none -size "${d}x${d}" %{name}.svg \
			%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -size 32x32 %{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# appdata
install -pm 0755 -d %{buildroot}%{_datadir}/appdata
install -pm 0644 bastet.appdata.xml %{buildroot}%{_datadir}/appdata/

# manpage
install -pm 0755 -d %{buildroot}%{_mandir}/man6
install -pm 0644 %{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6 

