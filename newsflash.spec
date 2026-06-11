%undefine __brp_mangle_shebangs

Name:           newsflash
Version:        4.2.1
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
* Tue Nov 18 2025 Umut Demir <mail@umutdemir.me> - 4.2.1-1
- Update to 4.2.1

* Thu Aug 28 2025 Umut Demir <mail@umutdemir.me> - 4.1.4-1
- Update to 4.1.4

* Mon Aug 4 2025 Umut Demir <mail@umutdemir.me> - 4.1.3-1
- Update to 4.1.3

* Wed Jul 30 2025 Umut Demir <mail@umutdemir.me> - 4.1.2-1
- Update to 4.1.2

* Sun Jul 6 2025 Umut Demir <mail@umutdemir.me> - 4.0.3-1
- Update to 4.0.3

* Fri Jun 20 2025 Umut Demir <mail@umutdemir.me> - 4.0.0~beta2-1
- Update to 4.0.0~beta2

* Fri May 9 2025 Umut Demir <mail@umutdemir.me> - 4.0.0~beta1-1
- Update to 4.0.0~beta1

* Sun Mar 23 2025 Umut Demir <mail@umutdemir.me> - 3.3.5-2
- Add check
- Disable brp mangle
- Use vendored dependencies

* Tue Sep 24 2024 Umut Demir <mail@umutdemir.me> - 3.3.5-1
- Update to 3.3.5
- Fix license

