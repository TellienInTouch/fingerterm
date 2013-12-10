Name: fingerterm
Version: 1.2.0
Release: 1
Summary: A terminal emulator with a custom virtual keyboard
Group: System/Base
License: GPLv2
Source0: %{name}-%{version}.tar.gz
URL: https://github.com/nemomobile/fingerterm
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt0Feedback)
BuildRequires: pkgconfig(sailfishapp)
Requires: qt5-qtdeclarative-import-xmllistmodel
Requires: qt5-qtdeclarative-import-window2
Requires: sailfishsilica-qt5
Obsoletes: meego-terminal <= 0.2.2
Provides: meego-terminal > 0.2.2

%description
%{summary}.

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{_datadir}/%{name}


%prep
%setup -q -n %{name}-%{version}


%build
# Inject version number from RPM into source
sed -i -e 's/PROGRAM_VERSION="[^"]*"/PROGRAM_VERSION="%{version}"/g' version.h

%qmake5
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%qmake5_install
