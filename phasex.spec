Summary:	Phase Harmonic Advanced Synthesis EXperiment
Name:		phasex
Version:	0.14.97
Release:	3
License:	GPL v3
Group:		X11/Applications
# git clone git://github.com/williamweston/phasex.git
# git archive --format=tar --prefix=phasex-0.14.97/ 0.14.97 | xz -c > phasex-0.14.97.tar.xz
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	9ddf99e805aad2988a001bf33b7444af
Patch0:		%{name}-desktop.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	alsa-lib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	gtk+-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	lash-devel
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHASEX is an experimental MIDI softsynth for Linux/ALSA/JACK with a
synth engine built around flexible phase modulation and flexible
oscillator/LFO sources. Modulations include AM, FM, offset PM,
and wave select. PHASEX comes equipped with multiple filter types
and modes, a stereo crossover delay and chorus with phaser,
ADSR envelopes for amplifier and filter, realtime audio input
processing capabilities, and more.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-cpu-power=3
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# non standard dir
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{512x512,tiny}

# validate .desktop file
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/phasex.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc doc/{ROADMAP,signal-diagram.txt}
%attr(755,root,root) %{_bindir}/phasex
%attr(755,root,root) %{_bindir}/phasex-convert-patch
%dir %{_datadir}/phasex
%{_datadir}/phasex/gtkenginerc
%{_datadir}/phasex/help
%{_datadir}/phasex/patchbank
%{_datadir}/phasex/pixmaps
%{_datadir}/phasex/sys-midimaps
%{_datadir}/phasex/sys-patches
%{_datadir}/phasex/sys-samples
%{_desktopdir}/phasex.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_datadir}/themes/Phasex-Dark
%{_datadir}/themes/Phasex-Light

