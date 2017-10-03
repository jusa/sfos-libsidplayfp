Name:       libsidplayfp
Summary:    SID playback library
Version:    1.8.7
Release:    1
Group:      System/Libraries
License:    LGPL 2.1
URL:        https://sourceforge.net/p/sidplay-residfp/wiki/Home/
Source:     %{name}-%{version}.tar.gz

%description
Libsidplayfp is a fork of sidplay2 born with the aim to improve the quality of emulating the 6581, 8580 chips and the surrounding C64 system in order to play SID music better.

%package devel
Summary:    Libsidplayfp development headers and libraries
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Files required for using libsidplayfp library.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libstilview.so.0
%{_libdir}/libsidplayfp.so.4.2.8
%{_libdir}/libsidplayfp.so.4
%{_libdir}/libstilview.so.0.0.3

%files devel
%defattr(-,root,root,-)
%{_libdir}/libstilview.so
%{_libdir}/libsidplayfp.so
%{_libdir}/pkgconfig/libsidplayfp.pc
%{_libdir}/pkgconfig/libstilview.pc
%dir %{_includedir}/stilview
%{_includedir}/stilview/stildefs.h
%{_includedir}/stilview/stil.h
%dir %{_includedir}/sidplayfp
%{_includedir}/sidplayfp/sidversion.h
%{_includedir}/sidplayfp/SidDatabase.h
%{_includedir}/sidplayfp/SidTune.h
%{_includedir}/sidplayfp/siddefs.h
%{_includedir}/sidplayfp/SidTuneInfo.h
%{_includedir}/sidplayfp/SidInfo.h
%{_includedir}/sidplayfp/builders
%{_includedir}/sidplayfp/builders/residfp.h
%{_includedir}/sidplayfp/builders/hardsid.h
%{_includedir}/sidplayfp/builders/resid.h
%{_includedir}/sidplayfp/event.h
%{_includedir}/sidplayfp/sidbuilder.h
%{_includedir}/sidplayfp/sidplayfp.h
%{_includedir}/sidplayfp/SidConfig.h
