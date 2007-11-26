%define funny_version DrJekyll

%define major 0
%define libname %mklibname xmms2_ %{major}
%define develname %mklibname -d xmms2

Summary:	XMMS2 is a redesign of the XMMS music player
Name:		xmms2
Version:	0.2
Release:	%mkrel 0.2.%{funny_version}.2
Group:          Sound
License:        GPL
URL:            http://xmms2.xmms.se/
Source0:        http://prdownloads.sourceforge.net/xmms2/%{name}-%{version}%{funny_version}.tar.bz2
BuildRequires:	SDL_ttf-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	curl-devel
BuildRequires:	fftw3-devel
BuildRequires:	glib2-devel >= 2.6.0
BuildRequires:	libGConf2-devel
BuildRequires:	libao-devel
BuildRequires:	libavahi-common-devel
BuildRequires:	libavahi-glib-devel
BuildRequires:	boost-devel
BuildRequires:	libdbus-devel
BuildRequires:	libdbus-glib-devel
BuildRequires:	libesound-devel
BuildRequires:	libffmpeg-devel
#BuildRequires:	libflac-devel
BuildRequires:	libgamin-devel
BuildRequires:	libgnome-vfs2-devel
BuildRequires:	libjack-devel
BuildRequires:	libmad-devel
BuildRequires:	libmms-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libshout-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	mad-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-pyrex
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	ruby-devel >= 1.8
BuildRequires:	scons >= 0.96.90
BuildRequires:	sidplay2-devel
BuildRequires:	speex-devel
BuildRequires:	sqlite3-devel >= 3.2.4
BuildRequires:	swig-devel >= 1.3.25
BuildRequires:	zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

%package -n	%{libname}
Summary:	Library associated with xmms2, needed for xmms2 and its plugins
Group:		System/Libraries

%description -n	%{libname}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This library is mandatory for xmms2 and for all its plugins to run.

%package -n	%{develname}
Summary:	Development package with static libs and headers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n	%{develname}
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

Static libraries and header files required for compiling xmms2 plugins.

%package	python
Summary:	Python bindings for XMMS2
Group:		Development/Libraries
#Requires:	%{name}-client = %{version}

%description	python
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This package contains files providing Python bindings for accessing XMM2.

%package	ruby
Summary:	Ruby bindings for XMMS2
Group:		Development/Libraries
#Requires:	%{name}-client = %{version}

%description	ruby
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

This package contains files providing Ruby bindings for accessing XMM2.

%prep

%setup -q -n %{name}-%{version}%{funny_version}

# this plugin has to be ported, disable it with a hack
#perl -pi -e "s|FLAC__seekable_stream_decoder_get_state|FLAC__seekable_stream_decoder_get_state_bla_bla_bla|g" src/plugins/flac/Plugin

%build

#scons \
#    CCFLAGS="%{optflags}" \
#    CXXFLAGS="%{optflags}" \
#    PREFIX=%{_prefix} \
#    SYSCONFDIR=%{_sysconfdir} \
#    LIBDIR=%{_libdir} \
#    PLUGINDIR=%{_libdir}/%{name} \
#    MANDIR=%{_mandir} \
#    LINKFLAGS="-lm" \
#    RUBYARCHDIR=%{ruby_sitearchdir} \
#    PKGCONFIGDIR=%{_libdir}/pkgconfig
./waf configure \
	--prefix=%{_prefix} --destdir=%{buildroot} --with-mandir=%{_mandir} \
	--with-ruby-archdir=%{ruby_sitearchdir} --with-ruby-libdir=%{ruby_sitelibdir} \
	--with-perl-archdir=%{perl_vendorarch}
./waf build %{_smp_mflags} --prefix=%{_prefix} --destdir=%{buildroot}

%install
rm -rf %{buildroot}

#scons INSTALLDIR=%{buildroot} install
./waf install --prefix=%{_prefix} --destdir=%{buildroot}

# cleanup
#rm -f %{buildroot}%{_datadir}/xmms2/mind.in.a.box-lament_snipplet.ogg

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%attr(0755,root,root) %{_bindir}/sdl-vis
%attr(0755,root,root) %{_bindir}/xmms2
%attr(0755,root,root) %{_bindir}/xmms2-et
%attr(0755,root,root) %{_bindir}/xmms2-find-avahi
%attr(0755,root,root) %{_bindir}/xmms2-launcher
%attr(0755,root,root) %{_bindir}/xmms2-mdns-avahi
%attr(0755,root,root) %{_bindir}/xmms2-mlib-updater
%attr(0755,root,root) %{_bindir}/xmms2d

# plugins
%dir %{_libdir}/xmms2
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_alsa.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_ao.so
#%attr(0755,root,root) %{_libdir}/xmms2/libxmms_curl_http.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_daap.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_diskwrite.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_equalizer.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_file.so
#%attr(0755,root,root) %{_libdir}/xmms2/libxmms_flac.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_gnomevfs.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_ices.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_icymetaint.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_id3v2.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_jack.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_lastfmeta.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_lastfm.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_mad.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_mms.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_modplug.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_musepack.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_null.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_nulstripper.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_oss.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_replaygain.so
#%attr(0755,root,root) %{_libdir}/xmms2/libxmms_smb.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_wave.so
#%attr(0755,root,root) %{_libdir}/xmms2/libxmms_wma.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_vocoder.so
%attr(0755,root,root) %{_libdir}/xmms2/libxmms_vorbis.so

%dir %{_datadir}/xmms2
%dir %{_datadir}/xmms2/scripts
%dir %{_datadir}/xmms2/scripts/startup.d
%attr(0755,root,root) %{_datadir}/xmms2/scripts/startup.d/*sh
%attr(0644,root,root) %{_datadir}/xmms2/mind.in.a.box-lament_snipplet.ogg

%{_mandir}/man1/xmms2.1*
%{_mandir}/man1/xmms2-et.1*
%{_mandir}/man1/xmms2-launcher.1*
%{_mandir}/man1/xmms2-mdns-avahi.1*
%{_mandir}/man1/xmms2d.1*

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING* INSTALL README TODO
%attr(0755,root,root) %{_libdir}/libxmmsclient*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/xmms2
%attr(0755,root,root) %{_libdir}/lib*.so
#%attr(0644,root,root) %{_libdir}/lib*.a
%attr(0644,root,root) %{_libdir}/pkgconfig/*.pc

%files ruby
%defattr(-,root,root,-)
%attr(0755,root,root) %{ruby_sitelibdir}/xmmsclient
%attr(0755,root,root) %{ruby_sitearchdir}/*.so

%files python
%defattr(-,root,root,-)
#%attr(0755,root,root)
%dir %{python_sitearch}/xmmsclient
%{python_sitearch}/xmmsclient/*.so
