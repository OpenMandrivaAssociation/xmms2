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
Version:	0.9.3
Release:	1
Group:		Sound
License:	GPLv2+
URL:		http://xmms2.sourceforge.net/
Source0:	https://github.com/xmms2/xmms2-devel/releases/download/%{version}/xmms2-%{version}.tar.xz
#Source0:	http://prdownloads.sourceforge.net/xmms2/%{name}-%{version}%{codename}.tar.bz2
Source1:	https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-client-launcher.sh

#Patch5:		https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-0.8DrO_o-moresaneversioning.patch
#Patch9:		https://src.fedoraproject.org/rpms/xmms2/raw/master/f/xmms2-0.8DrO_o-ruby22-remove-deprecated-usage.patch

#BuildRequires:	waf
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
#BuildRequires:	pkgconfig(libsidplay2)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(sqlite3)
#BuildRequires:	faad2-devel
BuildRequires:	swig >= 1.3.25
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(flac)
BuildRequires:	libgme-devel
# do actually require 2.3.0 from cvs, but sometime later, whenever.. :p
#BuildRequires:	pkgconfig(sc68)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(samba-util)

%description
XMMS2 is a redesign of the XMMS music player. It features a client-server
model, allowing multiple (even simultaneous!) user interfaces, both textual
and graphical. All common audio formats are supported using plugins. On top
of this, there is a flexible media library to organize your music.

%package devel
Summary:    Development libraries and headers for XMMS2
Group:      Development/C++
Requires:   glib2-devel, boost-devel
Requires:   %{name} = %{version}-%{release}

%description devel
Development libraries and headers for XMMS2. You probably need this to develop
or build new plugins for XMMS2.

%package docs
Summary:    Development documentation for XMMS2
Group:      Sound/Players
BuildArch:  noarch
Requires:   %{name} >= %{version}-%{release}

%description docs
API documentation for the XMMS2 modular audio framework architecture.

%package perl
Summary:    Perl support for XMMS2
License:    GPL+ or Artistic
Group:      Sound/Players
Requires:   %{name} = %{version}-%{release}

%description perl
Perl bindings for XMMS2.

%package ruby
Summary:    Ruby support for XMMS2
Group:      Sound/Players
Requires:   %{name} = %{version}-%{release}

%description ruby
Ruby bindings for XMMS2.

%prep
%setup -q
%autopatch -p1

%build
%global optflags %optflags -Wno-deprecated-declarations -Wno-unused-but-set-variable
./waf configure \
	--without-optionals=python \
	--with-ruby-libdir=%{ruby_vendorlibdir} \
	--with-ruby-archdir=%{ruby_vendorarchdir} \
	--with-perl-archdir=%{perl_vendorarch} \
	--with-pkgconfigdir=%{_libdir}/pkgconfig
./waf build -v

%install
./waf install --destdir=%{buildroot} \
	--with-ruby-libdir=%{ruby_vendorlibdir} \
	--with-ruby-archdir=%{ruby_vendorarchdir} \
	--with-perl-archdir=%{perl_vendorarch} \
	--with-pkgconfigdir=%{_libdir}/pkgconfig

# exec flags for debuginfo
#chmod +x %{buildroot}%{_libdir}/%{name}/* %{buildroot}%{_libdir}/libxmmsclient*.so* \
#    %{buildroot}%{perl_vendorarch}/auto/Audio/XMMSClient/XMMSClient.so %{buildroot}%{ruby_vendorarchdir}/xmmsclient_*.so


install -m0755 %{SOURCE1} %{buildroot}%{_bindir}

%files
%doc AUTHORS xmms2-%{version}.ChangeLog COPYING COPYING.GPL COPYING.LGPL README.mdown
#{_bindir}/%{name}*
#{_bindir}/_xmms2-migrate-collections-v0
#{_bindir}/sqlite2s4
#{_libdir}/libxmmsclient*.so.*
#{_libdir}/%{name}
#{_mandir}/man1/%{name}*
#{_datadir}/pixmaps/%{name}*
#{_datadir}/%{name}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libxmmsclient*.so
%{_libdir}/pkgconfig/%{name}-*.pc

%files docs
%doc doc/xmms2/html

%files perl
%{perl_vendorarch}/Audio/
%{perl_vendorarch}/auto/Audio/

%files ruby
%{ruby_vendorarchdir}/xmmsclient*
%{ruby_vendorlibdir}/xmmsclient*
