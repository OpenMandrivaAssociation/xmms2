%define codename DrO_o

%define	major	0
%define	libname %mklibname xmms2_ %{major}
%define	devname	%mklibname -d xmms2

# too lazy to fix...
%define	_disable_ld_no_undefined 1

%define	client_major 6
%define libclient %mklibname xmmsclient %{client_major}
%define c_glib_major 1
%define libclientglib %mklibname xmmsclient-glib %{c_glib_major}
%define	c_ecore_major 1
%define libclientecore %mklibname xmmsclient-ecore %{c_ecore_major}
%define	c_pp_major 4
%define libclientpp %mklibname xmmsclient++ %{c_pp_major}
%define	c_pp_glib_major 1
%define libclientppglib %mklibname xmmsclient++-glib %{c_pp_glib_major}

Summary:	Redesign of the XMMS music player
Name:		xmms2
Version:	0.8
Release:	5
Group:		Sound
License:	GPLv2+
URL:		http://xmms2.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/xmms2/%{name}-%{version}%{codename}.tar.bz2
Source1:	https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-client-launcher.sh
# Use libdir properly for Fedora multilib
Patch1:		https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-0.8DrO_o-use-libdir.patch
# Set default output to pulse
Patch2:		https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-0.8DrO_o-pulse-output-default.patch
# Don't add extra CFLAGS, we're smart enough, thanks.
Patch4:		https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-0.8DrO_o-no-O0.patch
# More sane versioning
Patch5:		https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-0.8DrO_o-moresaneversioning.patch
Patch6:		https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-0.8DrO_o-xsubpp-fix.patch
Patch7:		https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-0.8DrO_o-libmodplug-pkgconfig-change.patch
Patch8:		https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-0.8DrO_o-vorbis-pkgconfig-libs.patch
Patch9:		https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-0.8DrO_o-ruby22-remove-deprecated-usage.patch
Patch10:	https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-0.8DrO_o-openssl-1.1.patch
Patch15:	xmms2-0.8DrO_o-remove-dead-libavcodec-function.patch

Patch20:	bp-fix-avcodec-init.patch
Patch21:	bp-fix-alloc-context.patch
Patch22:	bp-fix-missing-include.patch
Patch23:	bp-Get-rid-of-superfluous-argument-self.patch
Patch24:	spelling-error.patch
Patch25:	linker-flags.patch
Patch26:	plugin-tta-segment-with-startms.patch
Patch27:	nycli-man-page-symlink.patch
Patch28:	rpath.patch
Patch29:	fix-manpage-errors.patch
Patch30:	fix-typos.patch
#Patch31:	hardening-flags.patch
Patch33:	samba-with-pkg-cfg.patch
#Patch34:	ruby2-multiarch.patch
Patch35:	libav10.patch
Patch36:	xmms2-buildfixes.patch

BuildRequires:	pkgconfig(alsa)
BuildRequires:	avahi-compat-libdns_sd-devel
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(ao)
BuildRequires:	avahi-common-devel
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(gamin)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	libmpcdec-devel
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libofa)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(shout)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libvisual-0.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	perl-devel
BuildRequires:	perl(Pod::Parser)
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(ruby)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(libsidplay2)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	faad2-devel
BuildRequires:	swig >= 1.3.25
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(flac)
BuildRequires:	libgme-devel
# do actually require 2.3.0 from cvs, but sometime later, whenever.. :p
BuildRequires:	pkgconfig(sc68)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(samba-util)

%description
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

%package -n	%{libclient}
Summary:	Library associated with xmms2, needed for xmms2 and its plugins
Group:		System/Libraries
Obsoletes:	%{libname}

%description -n	%{libclient}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This library is mandatory for xmms2 and for all its plugins to run.

%package -n	%{libclientglib}
Summary:	Library associated with xmms2, needed for xmms2 and its plugins
Group:		System/Libraries
Obsoletes:	%{libname}

%description -n	%{libclientglib}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This library is mandatory for xmms2 and for all its plugins to run.

%package -n	%{libclientecore}
Summary:	Library associated with xmms2, needed for xmms2 and its plugins
Group:		System/Libraries
Obsoletes:	%{libname}

%description -n	%{libclientecore}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This library is mandatory for xmms2 and for all its plugins to run.

%package -n	%{libclientpp}
Summary:	Library associated with xmms2, needed for xmms2 and its plugins
Group:		System/Libraries
Obsoletes:	%{libname}

%description -n	%{libclientpp}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This library is mandatory for xmms2 and for all its plugins to run.

%package -n	%{libclientppglib}
Summary:	Library associated with xmms2, needed for xmms2 and its plugins
Group:		System/Libraries
Obsoletes:	%{libname}

%description -n	%{libclientppglib}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This library is mandatory for xmms2 and for all its plugins to run.

%package -n	%{devname}
Summary:	Development package with static libs and headers
Group:		Development/C
Requires:	%{libclient} = %{version}-%{release}
Requires:	%{libclientglib} = %{version}-%{release}
Requires:	%{libclientecore} = %{version}-%{release}
Requires:	%{libclientpp} = %{version}-%{release}
Requires:	%{libclientppglib} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n	%{devname}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

Static libraries and header files required for compiling xmms2 plugins.

%package -n	python2-%{name}
Summary:	Python bindings for XMMS2
Group:		Development/Python
%rename		%{name}-python
%rename		python-%{name}

%description -n	python2-%{name}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This package contains files providing Python bindings for accessing XMM2.

%package -n	ruby-%{name}
Summary:	Ruby bindings for XMMS2
Group:		Development/Ruby
%rename		%{name}-ruby

%description -n	ruby-%{name}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This package contains files providing Ruby bindings for accessing XMM2.

%package -n	perl-%{name}
Summary:	Perl bindings for XMMS2
Group:		Development/Perl

%description -n	perl-%{name}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This package contains files providing Perl bindings for accessing XMM2.

%prep
%setup -q -n %{name}-%{version}%{codename}
# Unpack waflib files hidden inside the waf script.
# (Patch 9 needs to patch them...)
python2 waf --help &>/dev/null
%apply_patches

# Convert to utf-8
for i in `find src -name \*.1` xmms2-0.8DrO_o.ChangeLog; do
	iconv -o $i.iso88591 -f iso88591 -t utf8 $i
	mv $i.iso88591 $i
done

%build
%setup_compile_flags
export CPPFLAGS="%{optflags}"
export LIBDIR="%{_libdir}"
export PYTHONDIR="%{py2_platsitedir}"
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH
python2 ./waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --with-ruby-libdir=%{ruby_vendorlibdir} \
    --with-ruby-archdir=%{ruby_vendorarchdir} \
    --with-pkgconfigdir=%{_libdir}/pkgconfig \
    --with-perl-archdir=%{perl_vendorarch} \
    --no-cython

# parallel build occationally breaks..
python2 ./waf build -v %{_smp_mflags} || python2 ./waf build -v

%install
export PATH=`pwd`:$PATH
python2 ./waf install --destdir=%{buildroot}

# exec flags for debuginfo
chmod +x %{buildroot}%{_libdir}/%{name}/* %{buildroot}%{_libdir}/libxmmsclient*.so* %{buildroot}%{py2_platsitedir}/xmmsclient/xmmsapi.so \
	%{buildroot}%{perl_vendorarch}/auto/Audio/XMMSClient/XMMSClient.so %{buildroot}%{ruby_vendorarchdir}/xmmsclient_*.so


install -m0755 %{SOURCE1} %{buildroot}%{_bindir}

%files
%{_bindir}/nyxmms2
#%{_bindir}/vistest
#%{_bindir}/vistest-fft
%{_bindir}/xmms2
%{_bindir}/xmms2d
%{_bindir}/xmms2-client-launcher.sh
%{_bindir}/xmms2-et
%{_bindir}/xmms2-find-avahi
%{_bindir}/xmms2-launcher
#%{_bindir}/xmms2-libvisual
%{_bindir}/xmms2-mdns-avahi
%{_bindir}/xmms2-mlib-updater
#%{_bindir}/xmms2-ripper

# plugins
%dir %{_libdir}/xmms2
%{_libdir}/xmms2/libxmms_airplay.so
%{_libdir}/xmms2/libxmms_alsa.so
%{_libdir}/xmms2/libxmms_ao.so
%{_libdir}/xmms2/libxmms_apefile.so
%{_libdir}/xmms2/libxmms_asf.so
%{_libdir}/xmms2/libxmms_asx.so
%{_libdir}/xmms2/libxmms_avcodec.so
%{_libdir}/xmms2/libxmms_cdda.so
%{_libdir}/xmms2/libxmms_cue.so
%{_libdir}/xmms2/libxmms_curl.so
%{_libdir}/xmms2/libxmms_daap.so
%{_libdir}/xmms2/libxmms_diskwrite.so
%{_libdir}/xmms2/libxmms_equalizer.so
%{_libdir}/xmms2/libxmms_faad.so
%{_libdir}/xmms2/libxmms_file.so
%{_libdir}/xmms2/libxmms_flac.so
%{_libdir}/xmms2/libxmms_flv.so
%{_libdir}/xmms2/libxmms_gme.so
%{_libdir}/xmms2/libxmms_gvfs.so
%{_libdir}/xmms2/libxmms_html.so
%{_libdir}/xmms2/libxmms_ices.so
%{_libdir}/xmms2/libxmms_icymetaint.so
%{_libdir}/xmms2/libxmms_id3v2.so
%{_libdir}/xmms2/libxmms_jack.so
%{_libdir}/xmms2/libxmms_karaoke.so
%{_libdir}/xmms2/libxmms_m3u.so
%{_libdir}/xmms2/libxmms_mad.so
%{_libdir}/xmms2/libxmms_mms.so
%{_libdir}/xmms2/libxmms_modplug.so
%{_libdir}/xmms2/libxmms_mp4.so
%{_libdir}/xmms2/libxmms_mpg123.so
%{_libdir}/xmms2/libxmms_musepack.so
%{_libdir}/xmms2/libxmms_normalize.so
%{_libdir}/xmms2/libxmms_null.so
%{_libdir}/xmms2/libxmms_nulstripper.so
%{_libdir}/xmms2/libxmms_ofa.so
%{_libdir}/xmms2/libxmms_oss.so
%{_libdir}/xmms2/libxmms_pls.so
%{_libdir}/xmms2/libxmms_pulse.so
%{_libdir}/xmms2/libxmms_replaygain.so
%{_libdir}/xmms2/libxmms_rss.so
%{_libdir}/xmms2/libxmms_samba.so
#%{_libdir}/xmms2/libxmms_sid.so
%{_libdir}/xmms2/libxmms_sndfile.so
%{_libdir}/xmms2/libxmms_speex.so
%{_libdir}/xmms2/libxmms_tta.so
%{_libdir}/xmms2/libxmms_wave.so
%{_libdir}/xmms2/libxmms_vocoder.so
%{_libdir}/xmms2/libxmms_vorbis.so
%{_libdir}/xmms2/libxmms_wavpack.so
%{_libdir}/xmms2/libxmms_xml.so
%{_libdir}/xmms2/libxmms_xspf.so

%dir %{_datadir}/xmms2
%dir %{_datadir}/xmms2/scripts
%dir %{_datadir}/xmms2/scripts/startup.d
%{_datadir}/xmms2/scripts/startup.d/*sh
%{_datadir}/xmms2/mind.in.a.box-lament_snipplet.ogg

%{_datadir}/pixmaps/xmms2-128.png
%{_datadir}/pixmaps/xmms2-16.png
%{_datadir}/pixmaps/xmms2-32.png
%{_datadir}/pixmaps/xmms2-48.png
%{_datadir}/pixmaps/xmms2-black-on-white.svg
%{_datadir}/pixmaps/xmms2-white-on-black.svg
%{_datadir}/pixmaps/xmms2.svg

%{_mandir}/man1/nyxmms2.1*
%{_mandir}/man1/xmms2.1*
%{_mandir}/man1/xmms2-et.1*
%{_mandir}/man1/xmms2-launcher.1*
%{_mandir}/man1/xmms2-mdns-avahi.1*
%{_mandir}/man1/xmms2d.1*

%files -n %{libclient}
%{_libdir}/libxmmsclient.so.%{client_major}*

%files -n %{libclientglib}
%{_libdir}/libxmmsclient-glib.so.%{c_glib_major}*

%files -n %{libclientecore}
%{_libdir}/libxmmsclient-ecore.so.%{c_ecore_major}*

%files -n %{libclientpp}
%{_libdir}/libxmmsclient++.so.%{c_pp_major}*

%files -n %{libclientppglib}
%{_libdir}/libxmmsclient++-glib.so.%{c_pp_glib_major}*

%files -n %{devname}
%{_includedir}/xmms2
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files -n ruby-%{name}
%dir %{ruby_vendorlibdir}/xmmsclient
%{ruby_vendorlibdir}/xmmsclient/*.rb
%{ruby_vendorarchdir}/*.so
%{ruby_vendorlibdir}/xmmsclient.rb

%files -n python2-%{name}
%dir %{py2_platsitedir}/xmmsclient
%{py2_platsitedir}/xmmsclient/*.so
%{py2_platsitedir}/xmmsclient/*.py*

%files -n perl-%{name}
%dir %{perl_vendorarch}/Audio
%{perl_vendorarch}/Audio/*.pm
%{perl_vendorarch}/Audio/*.pod
%dir %{perl_vendorarch}/Audio/XMMSClient
%{perl_vendorarch}/Audio/XMMSClient/*.pod
%{perl_vendorarch}/Audio/XMMSClient/*.pm
%{perl_vendorarch}/auto/Audio/XMMSClient/XMMSClient.so
