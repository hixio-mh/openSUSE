#
# spec file for package patterns-kde
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with betatest

Name:           patterns-kde
Version:        20181130
Release:        0
Summary:        Patterns for Installation (kde devel)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros
BuildArch:      noarch

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the KDE patterns.

################################################################################

%package devel_kde_frameworks
%pattern_development
Summary:        KDE Frameworks and Plasma Development
Group:          Metapackages
Provides:       patterns-kde-devel_kde = %{version}
Provides:       patterns-openSUSE-devel_kde = %{version}
Provides:       patterns-openSUSE-devel_kde_framework = %{version}
Provides:       pattern() = devel_kde_frameworks
Provides:       pattern-icon() = pattern%2Dkde%2Ddevel
Provides:       pattern-order() = 3180
Provides:       pattern-visible()
Obsoletes:      patterns-kde-devel_kde < %{version}
Obsoletes:      patterns-openSUSE-devel_kde < %{version}
Obsoletes:      patterns-openSUSE-devel_kde_framework < %{version}
Requires:       pattern() = devel_C_C++
Recommends:     pattern() = devel_qt5
Recommends:     cmake
Recommends:     extra-cmake-modules

# Generated by:
# osc api /build/KDE:Frameworks5/openSUSE_Factory/x86_64/_repository | xmllint --xpath "binarylist/binary/@filename" - | sed 's/.rpm" filename="/\n/g' | awk '/-devel$/ { printf "Recommends:     %s\n", $0 }'

Recommends:     AppStream-devel
Recommends:     attica-qt5-devel
Recommends:     baloo5-devel
Recommends:     bluez-qt-devel
Recommends:     frameworkintegration-devel
Recommends:     kactivities-stats-devel
Recommends:     kactivities5-devel
Recommends:     karchive-devel
Recommends:     kauth-devel
Recommends:     kbookmarks-devel
Recommends:     kcmutils-devel
Recommends:     kcodecs-devel
Recommends:     kcompletion-devel
Recommends:     kconfig-devel
Recommends:     kconfigwidgets-devel
Recommends:     kcoreaddons-devel
Recommends:     kcrash-devel
Recommends:     kdbusaddons-devel
Recommends:     kdeclarative-devel
Recommends:     kded-devel
Recommends:     kdelibs4support-devel
Recommends:     kdesignerplugin-devel
Recommends:     kdesu-devel
Recommends:     kdewebkit-devel
Recommends:     kdnssd-framework-devel
Recommends:     kdoctools-devel
Recommends:     kemoticons-devel
Recommends:     kfilemetadata5-devel
Recommends:     kglobalaccel-devel
Recommends:     kguiaddons-devel
Recommends:     kholidays-devel
Recommends:     khotkeys5-devel
Recommends:     khtml-devel
Recommends:     ki18n-devel
Recommends:     kiconthemes-devel
Recommends:     kidletime-devel
Recommends:     kinit-devel
Recommends:     kio-devel
Recommends:     kirigami-devel
Recommends:     kirigami2-devel
Recommends:     kitemmodels-devel
Recommends:     kitemviews-devel
Recommends:     kjobwidgets-devel
Recommends:     kjs-devel
Recommends:     kjsembed-devel
Recommends:     kmediaplayer-devel
Recommends:     knewstuff-core-devel
Recommends:     knewstuff-devel
Recommends:     knewstuff-quick-devel
Recommends:     knotifications-devel
Recommends:     knotifyconfig-devel
Recommends:     kpackage-devel
Recommends:     kparts-devel
Recommends:     kpeople5-devel
Recommends:     kplotting-devel
Recommends:     kpty-devel
Recommends:     kross-devel
Recommends:     krunner-devel
Recommends:     kscreenlocker-devel
Recommends:     kservice-devel
Recommends:     ktexteditor-devel
Recommends:     ktextwidgets-devel
Recommends:     kunitconversion-devel
Recommends:     kwallet-devel
Recommends:     kwayland-devel
Recommends:     kwidgetsaddons-devel
Recommends:     kwin5-devel
Recommends:     kwindowsystem-devel
Recommends:     kxmlgui-devel
Recommends:     kxmlrpcclient5-devel
Recommends:     libAppStreamQt-devel
Recommends:     libKF5ModemManagerQt-devel
Recommends:     libKF5NetworkManagerQt-devel
Recommends:     libkdecoration2-devel
Recommends:     libkscreen2-devel
Recommends:     libksysguard5-devel
Recommends:     libpolkit-qt5-1-devel
Recommends:     oxygen5-devel
Recommends:     phonon4qt5-devel
Recommends:     plasma-framework-devel
Recommends:     plasma5-addons-devel
Recommends:     plasma5-workspace-devel
Recommends:     prison-qt5-devel
Recommends:     purpose-devel
Recommends:     qqc2-desktop-style-devel
Recommends:     solid-devel
Recommends:     sonnet-devel
Recommends:     syntax-highlighting-devel
Recommends:     systemsettings5-devel
Recommends:     threadweaver-devel

%description devel_kde_frameworks
KDE Frameworks development packages.

%files devel_kde_frameworks
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/devel_kde_frameworks.txt

################################################################################

%package devel_qt5
%pattern_development
Summary:        Qt 5 Development
Group:          Metapackages
Provides:       patterns-openSUSE-devel_qt5 = %{version}
Provides:       pattern() = devel_qt5
Provides:       pattern-icon() = pattern%2Dqt%2Ddevel
Provides:       pattern-order() = 3381
Provides:       pattern-visible()
Obsoletes:      patterns-openSUSE-devel_qt5 < %{version}
Requires:       libqt5-qtbase-common-devel
Requires:       pattern() = devel_C_C++
Recommends:     libqt5-creator

# Generated by:
# osc api /build/KDE:Qt5/openSUSE_Factory/x86_64/_repository | xmllint --xpath "binarylist/binary/@filename" - | sed 's/.rpm" filename="/\n/g' | awk '/libqt5-qt/ && /-devel$/ && !/private-headers/ { printf "Recommends:     %s\n", $0 }'

Recommends:     libqt5-qt3d-devel
Recommends:     libqt5-qtbase-common-devel
Recommends:     libqt5-qtbase-devel
Recommends:     libqt5-qtconnectivity-devel
Recommends:     libqt5-qtdeclarative-devel
Recommends:     libqt5-qtdoc-devel
Recommends:     libqt5-qtgamepad-devel
Recommends:     libqt5-qtimageformats-devel
Recommends:     libqt5-qtlocation-devel
Recommends:     libqt5-qtmultimedia-devel
Recommends:     libqt5-qtnetworkauth-devel
Recommends:     libqt5-qtremoteobjects-devel
Recommends:     libqt5-qtscript-devel
Recommends:     libqt5-qtscxml-devel
Recommends:     libqt5-qtsensors-devel
Recommends:     libqt5-qtserialbus-devel
Recommends:     libqt5-qtserialport-devel
Recommends:     libqt5-qtspeech-devel
Recommends:     libqt5-qtstyleplugins-devel
Recommends:     libqt5-qtsvg-devel
Recommends:     libqt5-qttools-devel
Recommends:     libqt5-qtvirtualkeyboard-devel
Recommends:     libqt5-qtwayland-devel
Recommends:     libqt5-qtwebchannel-devel
Recommends:     libqt5-qtwebengine-devel
Recommends:     libqt5-qtwebsockets-devel
Recommends:     libqt5-qtwebview-devel
Recommends:     libqt5-qtx11extras-devel
Recommends:     libqt5-qtxmlpatterns-devel

%description devel_qt5
Tools and libraries for software development using Qt 5.

%files devel_qt5
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/devel_qt5.txt

################################################################################

%package kde
%pattern_graphicalenvironments
Summary:        KDE Applications and Plasma 5 Desktop
Group:          Metapackages
Provides:       patterns-openSUSE-kde = %{version}
Provides:       patterns-openSUSE-kde4 = %{version}
Provides:       pattern() = kde
Provides:       pattern-icon() = pattern%2Dkde
Provides:       pattern-order() = 1110
Provides:       pattern-visible()
Obsoletes:      patterns-openSUSE-kde < %{version}
Obsoletes:      patterns-openSUSE-kde4 < %{version}
Requires:       pattern() = kde_plasma
Recommends:     pattern() = kde_internet
Recommends:     pattern() = kde_utilities
Recommends:     pattern() = kde_pim
Recommends:     pattern() = kde_yast
Recommends:     pattern() = multimedia
Recommends:     pattern() = office
Recommends:     pattern() = games
Recommends:     ark
Recommends:     discover
Recommends:     dolphin
Recommends:     kate
Recommends:     kcalc
Recommends:     konsole
Recommends:     spectacle
Recommends:     gwenview5
Recommends:     kipi-plugins
Recommends:     okular
# bnc#605509
Recommends:     skanlite
# bnc#521177
Suggests:       yakuake
Suggests:       kcron
Suggests:       ksystemlog
# from data/COMMON-DESKTOP
Recommends:     MozillaFirefox
Recommends:     avahi
Recommends:     yast2-control-center-qt
Suggests:       marble
Suggests:       kiosktool
Suggests:       krename
Suggests:       vym

%description kde
Packages providing the Plasma desktop environment and applications from KDE.

%files kde
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde.txt

################################################################################

%package kde_plasma
%pattern_graphicalenvironments
Summary:        KDE Plasma 5 Desktop Base
Group:          Metapackages
Provides:       patterns-openSUSE-kde4_basis = %{version}
Provides:       patterns-openSUSE-kde_plasma = %{version}
Provides:       pattern() = kde_plasma
Provides:       pattern-icon() = pattern%2Dkde
Provides:       pattern-order() = 1100
Provides:       pattern-visible()
Obsoletes:      patterns-openSUSE-kde4_admin < %{version}
Obsoletes:      patterns-openSUSE-kde4_basis < %{version}
Obsoletes:      patterns-openSUSE-kde4_laptop < %{version}
Obsoletes:      patterns-openSUSE-kde4_pure < %{version}
Obsoletes:      patterns-openSUSE-kde_plasma < %{version}
Obsoletes:      patterns-openSUSE-plasma5_basis < %{version}
Provides:       patterns-openSUSE-plasma5_basis = %{version}
# Obsolete the kdebase4-workspace-devel package specifically to prevent upgrade issues
Obsoletes:      kdebase4-workspace-devel
Requires:       pattern() = x11
# Obsolete the KDE bindings which have not been ported yet
Obsoletes:      mono-kde4
Obsoletes:      perl-kde4
Obsoletes:      python3-kde4
Obsoletes:      ruby-kde4

# Minimum to get a usable desktop
Requires:       breeze5-cursors
Requires:       breeze5-decoration
Requires:       breeze5-icons
Requires:       breeze5-style
Requires:       plasma5-session
# bnc#508120
Requires:       xdg-user-dirs
# bnc#430161
Requires:       desktop-data
Requires:       polkit-default-privs

# We have a theme for this, so prefer it
Recommends:     sddm

# To open folders on the desktop
Recommends:     dolphin

# Additional packages for the desktop
Recommends:     bluedevil5
Recommends:     breeze5-wallpapers
Recommends:     plasma-nm5
Recommends:     plasma5-pa
Recommends:     plasma5-pk-updates
Recommends:     plasma5-addons
Recommends:     plasma5-thunderbolt
Recommends:     kgamma5
Recommends:     kdeconnect-kde
Recommends:     kde-print-manager
Recommends:     kwrited5
# Wayland is optional
Recommends:     plasma5-session-wayland

# Make sure that at least a phonon backend is being installed
Recommends:     phonon4qt5-backend-gstreamer
# bnc#541820
Recommends:     khelpcenter5
Recommends:     kwalletmanager5
Recommends:     baloo5-file
Recommends:     baloo5-kioslaves
Recommends:     baloo5-tools
Recommends:     kdenetwork4-filesharing
Recommends:     pinentry-qt5
Recommends:     kio-extras5

# pulseaudio
Recommends:     pulseaudio
Recommends:     pulseaudio-module-x11
Recommends:     pulseaudio-module-zeroconf
Recommends:     pulseaudio-utils
Recommends:     alsa-plugins-pulse

# Thumbnailers
Recommends:     ffmpegthumbs
Recommends:     kdegraphics-thumbnailers

%description kde_plasma
Base packages for the KDE Plasma 5 desktop environment.

%files kde_plasma
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_plasma.txt

################################################################################

%package kde_pim
%pattern_kdedesktop
Summary:        KDE PIM Suite
Group:          Metapackages
Provides:       pattern() = kde_pim
Provides:       pattern-icon() = pattern%2Dkde%2Dpim
Provides:       pattern-order() = 2360
Provides:       pattern-visible()
Recommends:     akregator
Recommends:     kaddressbook
Recommends:     kmail
Recommends:     kontact
Recommends:     korganizer
Recommends:     knotes
Recommends:     kleopatra

%description kde_pim
The KDE PIM Suite (Kontact, KMail, KOrganizer, ...).

%files kde_pim
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_pim.txt

################################################################################

%package kde_edutainment
%pattern_kdedesktop
Summary:        KDE Education
Group:          Metapackages
Provides:       patterns-openSUSE-kde4_edutainment = %{version}
Provides:       patterns-openSUSE-kde_edutainment = %{version}
Provides:       pattern() = kde_edutainment
Provides:       pattern-icon() = package_edutainment
Provides:       pattern-order() = 2360
Obsoletes:      patterns-openSUSE-kde4_edutainment < %{version}
Obsoletes:      patterns-openSUSE-kde_edutainment < %{version}
Recommends:     blinken
Recommends:     marble
Recommends:     kalzium
Recommends:     kanagram
Recommends:     kbruch
Recommends:     kalgebra
Recommends:     kgeography
Recommends:     khangman
Recommends:     kig
Recommends:     kiten
Recommends:     klettres
Recommends:     kmplot
Recommends:     ktouch
Recommends:     parley
Recommends:     kwordquiz
Recommends:     step
Suggests:       kturtle

%description kde_edutainment
KDE Applications - Tools to teach kids with computers

%files kde_edutainment
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_edutainment.txt

################################################################################

%package kde_games
%pattern_kdedesktop
Summary:        KDE Games
Group:          Metapackages
Provides:       patterns-openSUSE-kde4_games = %{version}
Provides:       patterns-openSUSE-kde_games = %{version}
Provides:       pattern() = kde_games
Provides:       pattern-extends() = games
Provides:       pattern-icon() = package_games
Provides:       pattern-order() = 2400
Obsoletes:      patterns-openSUSE-kde4_games < %{version}
Obsoletes:      patterns-openSUSE-kde_games < %{version}
Supplements:    packageand(patterns-kde-kde:patterns-games-games)
# from data/KDE4-Games
Recommends:     kpat
Recommends:     kmahjongg
Recommends:     kmines
Recommends:     kreversi
Recommends:     ksudoku
Suggests:       kblocks
Suggests:       katomic
Suggests:       bovo
Suggests:       knavalbattle
Suggests:       kblackbox
Suggests:       kbounce
Suggests:       kbreakout
Suggests:       kdiamond
Suggests:       kgoldrunner
Suggests:       kiriki
Suggests:       kjumpingcube
Suggests:       kollision
Suggests:       klines
Suggests:       knetwalk
Suggests:       kolf
Suggests:       konquest
Suggests:       kshisen
Suggests:       ksirk
Suggests:       kspaceduel
Suggests:       ksquares
Suggests:       ktuberling
Suggests:       kubrick
Suggests:       lskat

%description kde_games
KDE Applications - Games

%files kde_games
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_games.txt

################################################################################

%package kde_ide
%pattern_kdedesktop
Summary:        KDE Integrated Development Environment
Group:          Metapackages
Provides:       patterns-openSUSE-kde4_ide = %{version}
Provides:       patterns-openSUSE-kde_ide = %{version}
Provides:       pattern() = kde_ide
Provides:       pattern-icon() = package_utilities
Provides:       pattern-order() = 2820
Obsoletes:      patterns-openSUSE-kde4_ide < %{version}
Obsoletes:      patterns-openSUSE-kde_ide < %{version}
Recommends:     kate
Recommends:     kdbg
Recommends:     kdevelop5
Recommends:     kapptemplate
Recommends:     lokalize
Recommends:     kcachegrind
Recommends:     kio_svn
Recommends:     kompare
Recommends:     umbrello
Suggests:       cervisia

%description kde_ide
KDE software for development (editors, integrated development environments, and associated tools).

%files kde_ide
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_ide.txt

################################################################################

%package kde_imaging
%pattern_kdedesktop
Summary:        KDE Graphics
Group:          Metapackages
Provides:       patterns-openSUSE-kde4_imaging = %{version}
Provides:       patterns-openSUSE-kde_imaging = %{version}
Provides:       pattern() = kde_imaging
Provides:       pattern-extends() = imaging
Provides:       pattern-icon() = package_graphics
Provides:       pattern-order() = 2540
Obsoletes:      patterns-openSUSE-kde4_imaging < %{version}
Obsoletes:      patterns-openSUSE-kde_imaging < %{version}
Supplements:    packageand(patterns-kde-kde:patterns-desktop-imaging)
Requires:       pattern() = kde_plasma
# from data/KDE4-IMAGE
Recommends:     gwenview5
Recommends:     digikam
Recommends:     kipi-plugins
Recommends:     okular
Recommends:     kio_kamera
Recommends:     kcolorchooser
# Should probably be Recommends here, but that would install krita on
# many current user's machines :-/
Suggests:       krita
Suggests:       libjpeg-turbo
Suggests:       kruler
Suggests:       kolourpaint

%description kde_imaging
KDE Applicatons - Handling of digital photos and graphics

%files kde_imaging
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_imaging.txt

################################################################################

%package kde_internet
%pattern_kdedesktop
Summary:        KDE Internet
Group:          Metapackages
Provides:       patterns-openSUSE-kde4_internet = %{version}
Provides:       patterns-openSUSE-kde_internet = %{version}
Provides:       pattern() = kde_internet
Provides:       pattern-extends() = kde4
Provides:       pattern-icon() = package_network
Provides:       pattern-order() = 2560
Obsoletes:      patterns-openSUSE-kde4_internet < %{version}
Obsoletes:      patterns-openSUSE-kde_internet < %{version}
# from data/KDE4-Internet
# 297684 for these 2
Recommends:     konversation
# bnc#533580
Recommends:     plasma-nm5-openvpn
Recommends:     plasma-nm5-openconnect
Recommends:     plasma-nm5-pptp
Suggests:       kget
Suggests:       kopete

%description kde_internet
KDE Internet Applications

%files kde_internet
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_internet.txt

################################################################################

%package kde_multimedia
%pattern_kdedesktop
Summary:        KDE Multimedia
Group:          Metapackages
Provides:       patterns-openSUSE-kde4_multimedia = %{version}
Provides:       patterns-openSUSE-kde_multimedia = %{version}
Provides:       pattern() = kde_multimedia
Provides:       pattern-extends() = multimedia
Provides:       pattern-icon() = package_multimedia
Provides:       pattern-order() = 2620
Obsoletes:      patterns-openSUSE-kde4_multimedia < %{version}
Obsoletes:      patterns-openSUSE-kde_multimedia < %{version}
Supplements:    packageand(patterns-kde-kde:patterns-desktop-multimedia)
# from data/KDE4-Multimedia
Recommends:     plasma5-pa
Recommends:     kio_audiocd
Recommends:     PackageKit-gstreamer-plugin
Recommends:     phonon4qt5-backend-gstreamer
Recommends:     gstreamer-plugins-good
# we want a video player
Recommends:     vlc
Suggests:       amarok
Suggests:       dragonplayer
Suggests:       juk
Suggests:       k3b
Suggests:       kscd

%description kde_multimedia
KDE Applications - Multimedia

%files kde_multimedia
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_multimedia.txt

################################################################################

%package kde_office
%pattern_kdedesktop
Summary:        KDE Office
Group:          Metapackages
Provides:       patterns-openSUSE-kde4_office = %{version}
Provides:       patterns-openSUSE-kde_office = %{version}
Provides:       pattern() = kde_office
Provides:       pattern-extends() = office
Provides:       pattern-icon() = package_wordprocessing
Provides:       pattern-order() = 2700
Obsoletes:      patterns-openSUSE-kde4_office < %{version}
Obsoletes:      patterns-openSUSE-kde_office < %{version}
Supplements:    packageand(patterns-kde-kde:patterns-office-office)
# from data/KDE4-Office
Recommends:     libreoffice-qt5
Recommends:     libreoffice-icon-theme-breeze
Suggests:       scribus

%description kde_office
KDE Office

%files kde_office
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_office.txt

################################################################################

%package kde_telepathy
%pattern_kdedesktop
Summary:        KDE Telepathy
Group:          Metapackages
Provides:       patterns-openSUSE-kde_telephony = %{version}
Provides:       pattern() = kde_telepathy
Provides:       pattern-extends() = kde4
Provides:       pattern-icon() = package_network
Provides:       pattern-order() = 2560
Obsoletes:      patterns-openSUSE-kde_telephony < %{version}
Requires:       ktp-accounts-kcm
Requires:       ktp-auth-handler
Requires:       ktp-common-internals
Requires:       ktp-icons
Requires:       ktp-kded-module
Requires:       signon-kwallet-extension
Requires:       signon-plugin-oauth2
Requires:       signon-plugins
Requires:       signon-ui
Requires:       signond
Recommends:     ktp-approver
Recommends:     ktp-contact-list
Recommends:     ktp-desktop-applets
Recommends:     ktp-text-ui
Suggests:       ktp-call-ui
Suggests:       ktp-contact-runner
Suggests:       ktp-filetransfer-handler
Suggests:       ktp-send-file

%description kde_telepathy
KDE Applications - Telepathy

%files kde_telepathy
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_telepathy.txt

################################################################################

%package kde_utilities
%pattern_kdedesktop
Summary:        KDE Utilities
Group:          Metapackages
Provides:       patterns-openSUSE-kde4_utilities = %{version}
Provides:       patterns-openSUSE-kde_utilities = %{version}
Provides:       pattern() = kde_utilities
Provides:       pattern-extends() = kde
Provides:       pattern-icon() = package_utilities
Provides:       pattern-order() = 2860
Obsoletes:      patterns-openSUSE-kde4_utilities < %{version}
Obsoletes:      patterns-openSUSE-kde_utilities < %{version}
Recommends:     pattern() = kde_utilities_opt
# from data/KDE4-Utilities
Recommends:     kmag
Recommends:     kcharselect
Recommends:     kmousetool
Recommends:     kompare
Suggests:       okteta
Suggests:       kteatime
Suggests:       ktux
Suggests:       amor
Suggests:       k4dirstat
Suggests:       sweeper

%description kde_utilities
KDE Applications - Utilities

%files kde_utilities
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_utilities.txt

################################################################################

%package kde_utilities_opt
%pattern_kdedesktop
Summary:        KDE Utilities
Group:          Metapackages
Provides:       patterns-openSUSE-kde4_utilities_opt = %{version}
Provides:       patterns-openSUSE-kde_utilities_opt = %{version}
Provides:       pattern() = kde_utilities_opt
Provides:       pattern-extends() = kde
Provides:       pattern-icon() = package_utilities
Provides:       pattern-order() = 2840
Obsoletes:      patterns-openSUSE-kde4_utilities_opt < %{version}
Obsoletes:      patterns-openSUSE-kde_utilities_opt < %{version}
# from data/KDE4-UTILITIES-OPT
Suggests:       rsibreak
Suggests:       speedcrunch
Suggests:       kchmviewer
Suggests:       kmouth
Suggests:       kremotecontrol
Suggests:       kdf
Suggests:       ktimer
Suggests:       kwikdisk
Suggests:       krusader

# from data/COMMON-DESKTOP-OPT
# packages a GTK application
Recommends:     gutenprint
# MAYBE later lsb-graphics
# give net shares
Recommends:     samba
# needs python-qt4, see#649280#14
Suggests:       hplip

%description kde_utilities_opt
KDE Application - Additional Utilities

%files kde_utilities_opt
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_utilities_opt.txt

################################################################################

%package kde_yast
%pattern_basetechnologies
Summary:        YaST KDE User Interfaces
Group:          Metapackages
Provides:       patterns-openSUSE-kde4_yast = %{version}
Provides:       patterns-openSUSE-kde_yast = %{version}
Provides:       pattern() = kde_yast
Provides:       pattern-extends() = yast2_basis
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1300
Obsoletes:      patterns-openSUSE-kde4_yast < %{version}
Obsoletes:      patterns-openSUSE-kde_yast < %{version}
Provides:       patterns-kde-sw_management_kde = %{version}
Obsoletes:      patterns-kde-sw_management_kde < %{version}
Provides:       patterns-openSUSE-sw_management_kde = %{version}
Obsoletes:      patterns-openSUSE-sw_management_kde < %{version}
Provides:       patterns-openSUSE-sw_management_kde4 = %{version}
Obsoletes:      patterns-openSUSE-sw_management_kde4 < %{version}
Supplements:    packageand(patterns-kde-kde_plasma:patterns-yast-yast2_basis)
# from data/KDE4-YaST
Requires:       libyui-qt-pkg
# SLE/Leap 15.1 or Tumbleweed
%if 0%{?sle_version} > 150000 || 0%{?suse_version} >= 1550
Requires:       yast2-theme-oxygen
%else
Requires:       yast2-branding-openSUSE-Oxygen
%endif
Requires:       yast2-control-center-qt

%description kde_yast
Graphical YaST user interfaces for the KDE desktop.

%files kde_yast
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/kde_yast.txt

%prep

%build

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
for i in devel_kde_frameworks devel_qt5 kde kde_plasma kde_pim \
    kde_edutainment kde_games kde_ide kde_imaging kde_internet kde_multimedia \
    kde_office kde_telepathy kde_utilities kde_utilities_opt kde_yast; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}/%{_defaultdocdir}/patterns/$i.txt"
done

%changelog
