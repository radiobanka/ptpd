%define _unpackaged_files_terminate_build 1

Name: ptpd
Version: 2.3.2
Release: alt1

Summary: PTP daemon (PTPd) is an implementation the Precision Time Protocol (PTP) version 2 as defined by 'IEEE Std 1588-2008'
License: BSD-2-Clause
Group: Other
Url: https://github.com/ptpd/ptpd

BuildRequires: gcc perl-XML-Parser

Source0: %name-%version.tar

%description
PTP daemon (PTPd) is an implementation the Precision Time Protocol (PTP) version
2 as defined by 'IEEE Std 1588-2008'. PTP provides precise time coordination of
Ethernet LAN connected computers. It was designed primarily for instrumentation
and control systems.

%prep
%setup -q

%build
autoreconf -vi
%configure
%make_build

%install
%makeinstall

%files
%_sbindir/%{name}2
%_man5dir/%{name}2.conf.5.xz
%_man8dir/%{name}2.8.xz
%_datadir/%name/PTPBASE-MIB.txt
%_datadir/%name/leap-seconds.list
%_datadir/%name/%{name}2.conf.default-full
%_datadir/%name/%{name}2.conf.minimal
%_datadir/%name/templates.conf


%changelog
* Wed May 24 2023 Menshchikov Evgeniy <menshchikovev@altlinux.org> 2.3.2-alt1
- Initial build.

