#
# spec file for package translation-update
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


Name:           translation-update
BuildRequires:  fdupes
BuildRequires:  gettext
Version:        15.1
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Translation updates. Files here should not conflict with
# translation-update-from-translation-update-upstream.
# In case of conflict, the particular translation file is lost.
Source:         translation-update.tar.bz2
Source1:        README
Source2:        COPYING
Source3:        AUTHORS
# WARNING: Before submitting new version, always review "osc diff", fix bad
# language description and update Obsoletes for removed locales.
# Auto-generated by translation-update-upstream supplementary scripts
# upstream-collect.sh + translation-update-upstream-to-translation-update.sh
# (Includes packages that don't correctly update with
# translation-update-upstream and packages that are not rebuilt in
# target project.)
Source4:        translation-update-from-translation-update-upstream-20181128.tar.bz2
# Last minute additions that take precedence over
# translation-update-from-translation-update-upstream. Strings are
# merged in a smart way and existing strings are not lost.
Source5:        translation-update2.tar.bz2
Source6:        translation-update.rpmlintrc
# Supplementary scripts:
# Reset ranslation-update.tar.bz2.
Source100:      reset-translation-update.sh
# Strip all sub-packages from the spec file.
Source101:      translation-update-spec-reset-lang-list.sh
# Generate spec file with needed sub-packages from .build.log from "osc build".
Source102:      translation-update-spec-generate-lang-list.sh
BuildArch:      noarch
Summary:        Translation Updates
# These packages existed only during SLE 15 / Leap 15 development
License:        GPL-2.0-or-later
Group:          System/Base
Obsoletes:      translation-update-ia
# All these packages are not needed in Tumbleweed
Obsoletes:      translation-update-ar
Obsoletes:      translation-update-as
Obsoletes:      translation-update-ast
Obsoletes:      translation-update-be
Obsoletes:      translation-update-be-latin
Obsoletes:      translation-update-bn
Obsoletes:      translation-update-bn_IN
Obsoletes:      translation-update-ca-valencia
Obsoletes:      translation-update-en
Obsoletes:      translation-update-en-shaw
Obsoletes:      translation-update-en_US
Obsoletes:      translation-update-eo
Obsoletes:      translation-update-es_AR
Obsoletes:      translation-update-es_CL
Obsoletes:      translation-update-es_CO
Obsoletes:      translation-update-es_CR
Obsoletes:      translation-update-es_DO
Obsoletes:      translation-update-es_EC
Obsoletes:      translation-update-es_ES
Obsoletes:      translation-update-es_GT
Obsoletes:      translation-update-es_HN
Obsoletes:      translation-update-es_MX
Obsoletes:      translation-update-es_NI
Obsoletes:      translation-update-es_PA
Obsoletes:      translation-update-es_PE
Obsoletes:      translation-update-es_PR
Obsoletes:      translation-update-es_SV
Obsoletes:      translation-update-es_UY
Obsoletes:      translation-update-es_VE
Obsoletes:      translation-update-fa
Obsoletes:      translation-update-fr_CA
Obsoletes:      translation-update-gu
Obsoletes:      translation-update-he
Obsoletes:      translation-update-hi
Obsoletes:      translation-update-id
Obsoletes:      translation-update-is
Obsoletes:      translation-update-it_IT
Obsoletes:      translation-update-kk
Obsoletes:      translation-update-km
Obsoletes:      translation-update-kn
Obsoletes:      translation-update-mai
Obsoletes:      translation-update-mk
Obsoletes:      translation-update-mr
Obsoletes:      translation-update-nb_NO
Obsoletes:      translation-update-nds
Obsoletes:      translation-update-nn
Obsoletes:      translation-update-or
Obsoletes:      translation-update-pt_PT
Obsoletes:      translation-update-sq
Obsoletes:      translation-update-sr-ije
Obsoletes:      translation-update-sr-latin
Obsoletes:      translation-update-ta
Obsoletes:      translation-update-te
Obsoletes:      translation-update-th
Obsoletes:      translation-update-tr_TR
Obsoletes:      translation-update-ug
Obsoletes:      translation-update-wa
Obsoletes:      translation-update-zh_HK

%description
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-bg
Summary:        Translation Updates for Bulgarian
Group:          System/Localization
Provides:       locale(translation-update:bg)
Requires:       translation-update

%description -n translation-update-bg
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-ca
Summary:        Translation Updates for Catalan
Group:          System/Localization
Provides:       locale(translation-update:ca)
Requires:       translation-update

%description -n translation-update-ca
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-cs
Summary:        Translation Updates for Czech
Group:          System/Localization
Provides:       locale(translation-update:cs)
Requires:       translation-update

%description -n translation-update-cs
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-da
Summary:        Translation Updates for 
Group:          System/Localization
Provides:       locale(translation-update:da)
Requires:       translation-update

%description -n translation-update-da
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-de
Summary:        Translation Updates for German
Group:          System/Localization
Provides:       locale(translation-update:de)
Requires:       translation-update

%description -n translation-update-de
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-dz
Summary:        Translation Updates for Dzongkha
Group:          System/Localization
Provides:       locale(translation-update:dz)
Requires:       translation-update

%description -n translation-update-dz
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-el
Summary:        Translation Updates for Greek
Group:          System/Localization
Provides:       locale(translation-update:el)
Requires:       translation-update

%description -n translation-update-el
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-en_CA
Summary:        Translation Updates for Canadian English
Group:          System/Localization
Provides:       locale(translation-update:en_CA)
Requires:       translation-update

%description -n translation-update-en_CA
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-en_GB
Summary:        Translation Updates for 
Group:          System/Localization
Provides:       locale(translation-update:en_GB)
Requires:       translation-update

%description -n translation-update-en_GB
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-es
Summary:        Translation Updates for Spanish
Group:          System/Localization
Provides:       locale(translation-update:es)
Requires:       translation-update

%description -n translation-update-es
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-et
Summary:        Translation Updates for Estonian
Group:          System/Localization
Provides:       locale(translation-update:et)
Requires:       translation-update

%description -n translation-update-et
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-eu
Summary:        Translation Updates for Basque
Group:          System/Localization
Provides:       locale(translation-update:eu)
Requires:       translation-update

%description -n translation-update-eu
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-fi
Summary:        Translation Updates for Finnish
Group:          System/Localization
Provides:       locale(translation-update:fi)
Requires:       translation-update

%description -n translation-update-fi
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-fr
Summary:        Translation Updates for French
Group:          System/Localization
Provides:       locale(translation-update:fr)
Requires:       translation-update

%description -n translation-update-fr
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-ga
Summary:        Translation Updates for Irish
Group:          System/Localization
Provides:       locale(translation-update:ga)
Requires:       translation-update

%description -n translation-update-ga
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-gl
Summary:        Translation Updates for Galician
Group:          System/Localization
Provides:       locale(translation-update:gl)
Requires:       translation-update

%description -n translation-update-gl
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-hr
Summary:        Translation Updates for Croatian
Group:          System/Localization
Provides:       locale(translation-update:hr)
Requires:       translation-update

%description -n translation-update-hr
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-hu
Summary:        Translation Updates for Hungarian
Group:          System/Localization
Provides:       locale(translation-update:hu)
Requires:       translation-update

%description -n translation-update-hu
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-it
Summary:        Translation Updates for italiano
Group:          System/Localization
Provides:       locale(translation-update:it)
Requires:       translation-update

%description -n translation-update-it
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-ja
Summary:        Translation Updates for Japanese
Group:          System/Localization
Provides:       locale(translation-update:ja)
Requires:       translation-update

%description -n translation-update-ja
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-ko
Summary:        Translation Updates for Korean
Group:          System/Localization
Provides:       locale(translation-update:ko)
Requires:       translation-update

%description -n translation-update-ko
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-lt
Summary:        Translation Updates for Lithuanian
Group:          System/Localization
Provides:       locale(translation-update:lt)
Requires:       translation-update

%description -n translation-update-lt
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-lv
Summary:        Translation Updates for Latvian
Group:          System/Localization
Provides:       locale(translation-update:lv)
Requires:       translation-update

%description -n translation-update-lv
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-ml
Summary:        Translation Updates for Malayalam
Group:          System/Localization
Provides:       locale(translation-update:ml)
Requires:       translation-update

%description -n translation-update-ml
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-nb
Summary:        Translation Updates for Norwegian bokmål
Group:          System/Localization
Provides:       locale(translation-update:nb)
Requires:       translation-update

%description -n translation-update-nb
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-ne
Summary:        Translation Updates for Nepali
Group:          System/Localization
Provides:       locale(translation-update:ne)
Requires:       translation-update

%description -n translation-update-ne
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-nl
Summary:        Translation Updates for Dutch
Group:          System/Localization
Provides:       locale(translation-update:nl)
Requires:       translation-update

%description -n translation-update-nl
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-pa
Summary:        Translation Updates for Punjabi
Group:          System/Localization
Provides:       locale(translation-update:pa)
Requires:       translation-update

%description -n translation-update-pa
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-pl
Summary:        Translation Updates for Polish
Group:          System/Localization
Provides:       locale(translation-update:pl)
Requires:       translation-update

%description -n translation-update-pl
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-pt
Summary:        Translation Updates for Portuguese
Group:          System/Localization
Provides:       locale(translation-update:pt)
Requires:       translation-update

%description -n translation-update-pt
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-pt_BR
Summary:        Translation Updates for Brazilian Portuguese
Group:          System/Localization
Provides:       locale(translation-update:pt_BR)
Requires:       translation-update

%description -n translation-update-pt_BR
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-ro
Summary:        Translation Updates for Romanian
Group:          System/Localization
Provides:       locale(translation-update:ro)
Requires:       translation-update

%description -n translation-update-ro
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-ru
Summary:        Translation Updates for Russian
Group:          System/Localization
Provides:       locale(translation-update:ru)
Requires:       translation-update

%description -n translation-update-ru
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-sk
Summary:        Translation Updates for Slovak
Group:          System/Localization
Provides:       locale(translation-update:sk)
Requires:       translation-update

%description -n translation-update-sk
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-sl
Summary:        Translation Updates for Slovenian
Group:          System/Localization
Provides:       locale(translation-update:sl)
Requires:       translation-update

%description -n translation-update-sl
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-sr
Summary:        Translation Updates for Serbian (sr)
Group:          System/Localization
Provides:       locale(translation-update:sr)
Requires:       translation-update

%description -n translation-update-sr
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-sv
Summary:        Translation Updates for Swedish
Group:          System/Localization
Provides:       locale(translation-update:sv)
Requires:       translation-update

%description -n translation-update-sv
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-tr
Summary:        Translation Updates for Turkish
Group:          System/Localization
Provides:       locale(translation-update:tr)
Requires:       translation-update

%description -n translation-update-tr
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-uk
Summary:        Translation Updates for Ukrainian
Group:          System/Localization
Provides:       locale(translation-update:uk)
Requires:       translation-update

%description -n translation-update-uk
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-vi
Summary:        Translation Updates for Vietnamese
Group:          System/Localization
Provides:       locale(translation-update:vi)
Requires:       translation-update

%description -n translation-update-vi
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-zh_CN
Summary:        Translation Updates for Simplified Chinese
Group:          System/Localization
Provides:       locale(translation-update:zh_CN)
Requires:       translation-update

%description -n translation-update-zh_CN
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%package -n translation-update-zh_TW
Summary:        Translation Updates for Traditional Chinese
Group:          System/Localization
Provides:       locale(translation-update:zh_TW)
Requires:       translation-update

%description -n translation-update-zh_TW
This is a set of translation updates that are installed into the
preferred directory, /usr/share/locale-langpack/<locale>/LC_MESSAGES/.

Applications that use gettext correctly can then pick up overridden or
updated translations from this location.

%prep
%setup -n translation-update -a 4
# # These were updated on SLE10 SP1 resp. separately as yast2-trans-{??,??_??}
# rm -fr yast-trans/{ar,bn,ca,cs,de,es,fi,fr,hi,hu,it,ja,ko,nb,nl,pl,pt_BR,ru,sk,ta,zh_CN,zh_TW}
cd ..
mkdir tu2
cd tu2
tar xvf %{S:5}
cd ..

%build
%if ! 0%{?is_opensuse}
echo "This is a openSUSE only package! Please use SLE version."
exit 1
%endif
# Merge last minute updates in upstream collected files
shopt -s nullglob
up_dir=../../../translation-update/translation-update
cd ../tu2/translation-update
for PACKAGE in * ; do
  cd $PACKAGE
  for LL in * ; do
    msgfmt --check -o /dev/null $LL/$LL.po || continue
    # ls $up_dir
    up_ll_dir=$up_dir/$PACKAGE/$LL
    up_ll_file=$up_ll_dir/$LL.po
    if [ -f $up_ll_file ]; then
      msgcat --use-first -o tmp.po $LL/$LL.po $up_ll_file \
        && mv tmp.po $up_ll_file \
        || :
    else
      mkdir -p $up_ll_dir
      cp $LL/$LL.po $up_ll_dir
    fi
  done
  cd ..
done

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale-langpack
# First process translation-update tarball.
shopt -s nullglob
for PACKAGE in * ; do
    if test "$PACKAGE" = translation-update ; then
	continue
    fi
    cd $PACKAGE
    for LNG in * ; do
	cd $LNG
	for PO in *.po ; do
	    if [ ${PO%.po} == $LNG ] ; then
		msgfmt -c -o $PACKAGE.mo $PO
	    else
		msgfmt -c -o ${PO%.$LNG.po}.mo $PO
	    fi
	    if [ -d ${RPM_BUILD_ROOT}%{_datadir}/locale-langpack/$LNG ] ; then
		install -m 644 *.mo ${RPM_BUILD_ROOT}%{_datadir}/locale-langpack/$LNG/LC_MESSAGES
	    else
		install -d ${RPM_BUILD_ROOT}%{_datadir}/locale-langpack/$LNG/LC_MESSAGES
		install -m 644 *.mo ${RPM_BUILD_ROOT}%{_datadir}/locale-langpack/$LNG/LC_MESSAGES
	    fi
	done
	cd ..
    done
    cd ..
done
cd translation-update
# Second process translation-update-from-translation-update-upstream tarball.
# In case of conflict, it will overwrite the previous. (It should contain LCN + upstream fixes together.
for PACKAGE in * ; do
    cd $PACKAGE
    for LNG in * ; do
	cd $LNG
	for PO in *.po ; do

	    # Supplementary scripts make several checks. But if the
	    # downstream po file was already invalid, then update may
	    # still be invalid. Don't fail and ignore such updates.

	    if [ ${PO%.po} == $LNG ] ; then
		if ! msgfmt -c -o $PACKAGE.mo $PO ; then
		    echo "ERROR: $PACKAGE/$LNG/$PO is invalid. Ignoring update."
		    continue
		fi
	    else
		if ! msgfmt -c -o ${PO%.$LNG.po}.mo $PO ; then
		    echo "ERROR: $PACKAGE/$LNG/$PO is invalid. Ignoring update."
		    continue
		fi
	    fi
	    if [ -d ${RPM_BUILD_ROOT}%{_datadir}/locale-langpack/$LNG ] ; then
		install -m 644 *.mo ${RPM_BUILD_ROOT}%{_datadir}/locale-langpack/$LNG/LC_MESSAGES
	    else
		install -d ${RPM_BUILD_ROOT}%{_datadir}/locale-langpack/$LNG/LC_MESSAGES
		install -m 644 *.mo ${RPM_BUILD_ROOT}%{_datadir}/locale-langpack/$LNG/LC_MESSAGES
	    fi
	done
	cd ..
    done
    cd ..
done
cd ..
install -d ${RPM_BUILD_ROOT}%{_defaultdocdir}/%{name}
install -m 644 %{S:1} ${RPM_BUILD_ROOT}%{_defaultdocdir}/%{name}
install -m 644 %{S:2} ${RPM_BUILD_ROOT}%{_defaultdocdir}/%{name}
install -m 644 %{S:3} ${RPM_BUILD_ROOT}%{_defaultdocdir}/%{name}
# For empty subpackages
install -m 644 %{S:2} .

#
# go through valid locales and fail in invalid ones
#
set +x
cd $RPM_BUILD_ROOT%{_datadir}/locale-langpack
for LOCALE in * ; do
	if ! test -d /usr/share/locale/$LOCALE ; then
               echo -n "removing unsupported translation $LOCALE"
               rm -rfv $LOCALE
        fi
done

# FIXME: There are duplicates! Some packages changed its domain and translation-update.tar.bz2 still uses the old one.
%fdupes ${RPM_BUILD_ROOT}

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_defaultdocdir}/%{name}

%files -n translation-update-bg
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(bg) %{_datadir}/locale-langpack/bg
%doc COPYING

%files -n translation-update-ca
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(ca) %{_datadir}/locale-langpack/ca
%doc COPYING

%files -n translation-update-cs
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(cs) %{_datadir}/locale-langpack/cs
%doc COPYING

%files -n translation-update-da
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(da) %{_datadir}/locale-langpack/da
%doc COPYING

%files -n translation-update-de
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(de) %{_datadir}/locale-langpack/de
%doc COPYING

%files -n translation-update-dz
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(dz) %{_datadir}/locale-langpack/dz
%doc COPYING

%files -n translation-update-el
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(el) %{_datadir}/locale-langpack/el
%doc COPYING

%files -n translation-update-en_CA
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(en_CA) %{_datadir}/locale-langpack/en_CA
%doc COPYING

%files -n translation-update-en_GB
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(en_GB) %{_datadir}/locale-langpack/en_GB
%doc COPYING

%files -n translation-update-es
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(es) %{_datadir}/locale-langpack/es
%doc COPYING

%files -n translation-update-et
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(et) %{_datadir}/locale-langpack/et
%doc COPYING

%files -n translation-update-eu
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(eu) %{_datadir}/locale-langpack/eu
%doc COPYING

%files -n translation-update-fi
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(fi) %{_datadir}/locale-langpack/fi
%doc COPYING

%files -n translation-update-fr
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(fr) %{_datadir}/locale-langpack/fr
%doc COPYING

%files -n translation-update-ga
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(ga) %{_datadir}/locale-langpack/ga
%doc COPYING

%files -n translation-update-gl
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(gl) %{_datadir}/locale-langpack/gl
%doc COPYING

%files -n translation-update-hr
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(hr) %{_datadir}/locale-langpack/hr
%doc COPYING

%files -n translation-update-hu
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(hu) %{_datadir}/locale-langpack/hu
%doc COPYING

%files -n translation-update-it
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(it) %{_datadir}/locale-langpack/it
%doc COPYING

%files -n translation-update-ja
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(ja) %{_datadir}/locale-langpack/ja
%doc COPYING

%files -n translation-update-ko
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(ko) %{_datadir}/locale-langpack/ko
%doc COPYING

%files -n translation-update-lt
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(lt) %{_datadir}/locale-langpack/lt
%doc COPYING

%files -n translation-update-lv
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(lv) %{_datadir}/locale-langpack/lv
%doc COPYING

%files -n translation-update-ml
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(ml) %{_datadir}/locale-langpack/ml
%doc COPYING

%files -n translation-update-nb
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(nb) %{_datadir}/locale-langpack/nb
%doc COPYING

%files -n translation-update-ne
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(ne) %{_datadir}/locale-langpack/ne
%doc COPYING

%files -n translation-update-nl
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(nl) %{_datadir}/locale-langpack/nl
%doc COPYING

%files -n translation-update-pa
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(pa) %{_datadir}/locale-langpack/pa
%doc COPYING

%files -n translation-update-pl
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(pl) %{_datadir}/locale-langpack/pl
%doc COPYING

%files -n translation-update-pt
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(pt) %{_datadir}/locale-langpack/pt
%doc COPYING

%files -n translation-update-pt_BR
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(pt_BR) %{_datadir}/locale-langpack/pt_BR
%doc COPYING

%files -n translation-update-ro
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(ro) %{_datadir}/locale-langpack/ro
%doc COPYING

%files -n translation-update-ru
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(ru) %{_datadir}/locale-langpack/ru
%doc COPYING

%files -n translation-update-sk
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(sk) %{_datadir}/locale-langpack/sk
%doc COPYING

%files -n translation-update-sl
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(sl) %{_datadir}/locale-langpack/sl
%doc COPYING

%files -n translation-update-sr
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(sr) %{_datadir}/locale-langpack/sr
%doc COPYING

%files -n translation-update-sv
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(sv) %{_datadir}/locale-langpack/sv
%doc COPYING

%files -n translation-update-tr
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(tr) %{_datadir}/locale-langpack/tr
%doc COPYING

%files -n translation-update-uk
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(uk) %{_datadir}/locale-langpack/uk
%doc COPYING

%files -n translation-update-vi
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(vi) %{_datadir}/locale-langpack/vi
%doc COPYING

%files -n translation-update-zh_CN
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(zh_CN) %{_datadir}/locale-langpack/zh_CN
%doc COPYING

%files -n translation-update-zh_TW
%defattr(-,root,root)
%dir %{_datadir}/locale-langpack
%lang(zh_TW) %{_datadir}/locale-langpack/zh_TW
%doc COPYING

%changelog
