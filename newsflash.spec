%undefine __brp_mangle_shebangs

Name:           newsflash
Version:        5.1.0
Release:        1%{?dist}
Summary:        Follow your favorite blogs & news sites

License:        GPL-3.0-only
URL:            https://gitlab.com/news-flash/news_flash_gtk
Source0:        %{url}/-/archive/v.%{version}/news_flash_gtk-v.%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        vendor-config.toml

BuildRequires:  blueprint-compiler
BuildRequires:  cargo-rpm-macros >= 25
BuildRequires:  clang-devel
BuildRequires:  meson
BuildRequires:  openssl-devel

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  sqlite3

BuildRequires:  pkgconfig(clapper-0.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(webkitgtk-6.0)

%description
NewsFlash is a program designed to complement an already existing web-based
RSS reader account. It combines all the advantages of web based services like
syncing across all your devices with everything you expect from a modern
desktop program: Desktop notifications, fast search and filtering, tagging,
handy keyboard shortcutsand having access to all your articles as long as you
like.

%prep
%autosetup -n news_flash_gtk-v.%{version} -p1 -a1
%cargo_prep -N
if [ -f .cargo/config.toml ]; then
  cat %{SOURCE2} >> .cargo/config.toml
else
  cat %{SOURCE2} >> .cargo/config
fi

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.gitlab.news_flash.NewsFlash.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.gitlab.news_flash.NewsFlash.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/io.gitlab.news_flash.NewsFlash
%{_datadir}/applications/io.gitlab.news_flash.NewsFlash.desktop
%{_datadir}/dbus-1/services/io.gitlab.news_flash.NewsFlash.service
%{_datadir}/icons/hicolor/scalable/apps/io.gitlab.news_flash.NewsFlash.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.gitlab.news_flash.NewsFlash-symbolic.svg
%{_metainfodir}/io.gitlab.news_flash.NewsFlash.appdata.xml

%changelog
%autochangelog
