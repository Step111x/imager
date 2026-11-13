%define _unpackaged_files_terminate_build 1

Name: imager
Version: 1.0
Release: alt1
Summary: Simple SDL2 image viewer with curl
License: GPLv3
Group: Graphics
Url: https://github.com/vasthecat/imager

Source: %name-%version.tar

PreReq: rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: libcurl-devel
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_image-devel

%description
A simple C application that downloads and displays an image using
libcurl and SDL2.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/imager
%_datadir/applications/imager.desktop

%changelog
* Tue Nov 10 2026 mr step <stepmr4@gmail.com> 1.0-alt1
- Initial build.
