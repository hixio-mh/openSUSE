#
# spec file for package gaupol
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define long_name io.otsaloma.gaupol
%bcond_without test
Name:           gaupol
Version:        1.8
Release:        0
Summary:        GTK Subtitle editor
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://otsaloma.io/gaupol/
Source0:        https://github.com/otsaloma/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE gaupol-1.7-desktop.patch prusnak@suse.cz -- add desktop category
Patch0:         gaupol-1.7-desktop.patch
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-devel
BuildRequires:  python3-gobject >= 3.12
Requires:       python3
Requires:       python3-aeidon
Requires:       python3-gobject >= 3.12
Recommends:     iso-codes >= 3.67
Recommends:     python3-chardet
BuildArch:      noarch
%if %{with test}
BuildRequires:  myspell-en_US
BuildRequires:  python3-chardet
BuildRequires:  python3-pytest
BuildRequires:  typelib(Gspell) >= 1
%endif

%description
Gaupol is an editor for text-based subtitle files. It supports multiple subtitle
file formats and provides means of correcting texts and timing subtitles to match
video. The user interface is designed with attention to batch processing of
multiple documents and convenience of translating.

Gaupol should run on all Unix-like (GNU/Linux, *BSD, etc.) operating systems and
on Windows. Technically it should be able to run on Mac as well, but that has
not been tested nor made convenient. Gaupol's user interface is based on the GTK+
toolkit and has been designed to best fit the GNOME desktop environment.

%package -n python3-aeidon
Summary:        Package for reading, writing and manipulating text-based subtitle files
Group:          Development/Libraries/Python
Provides:       python-aeidon = %{version}
Obsoletes:      python-aeidon < %{version}

%description -n python3-aeidon
This is a Python package for reading, writing and manipulating
text-based subtitle files. It is separate from the gaupol package,
which provides a subtitle editor application with a GTK+ user
interface.

%prep
%setup -q
%patch0

%build
export CFLAGS="%{optflags}"
python3 setup.py build

%install
python3 setup.py clean install --prefix=%{_prefix} --root=%{buildroot}
rm -f %{buildroot}%{_datadir}/gaupol/extensions/side-pane/__pycache__/*.pyc
rm -f %{buildroot}%{_datadir}/gaupol/extensions/custom-framerates/__pycache__/*.pyc
rm -f %{buildroot}%{_datadir}/gaupol/extensions/bookmarks/__pycache__/*.pyc

#remove zero length files
find %{buildroot} -type f -size 0 -delete

%find_lang %{name}
%fdupes %{buildroot}

%if %{with test}
%check
# No idea why "en" language can't be found
sed -i 's/"en"/"en_US"/' aeidon/test/test_spell.py
sed -i 's/language="en"/language="en_US"/' aeidon/agents/test/test_text.py
LANG=en py.test aeidon
%endif

%files -f %{name}.lang
%doc AUTHORS.md README.md NEWS.md
%license COPYING
%{_bindir}/gaupol
%{python3_sitelib}/gaupol*
%{_datadir}/%{name}
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{long_name}.appdata.xml
%{_datadir}/applications/%{long_name}.desktop
%{_datadir}/icons/*/*/apps/%{long_name}*
%{_mandir}/man1/gaupol.1%{?ext_man}

%files -n python3-aeidon
%doc AUTHORS.md README.aeidon.md NEWS.md
%license COPYING
%{python3_sitelib}/aeidon

%changelog
