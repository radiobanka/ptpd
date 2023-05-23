%define _unpackaged_files_terminate_build 1

Name: ptpd
Version: 2.3.2
Release: alt1

Summary: PTP daemon (PTPd) is an implementation the Precision Time Protocol (PTP) version
2 as defined by 'IEEE Std 1588-2008'
License: BSD-2-Clause
Group: Other
Url: https://github.com/ptpd/ptpd

Requires: gcc

BuildRequires: gcc

Source0: %name-%version.tar

%description:
PTP daemon (PTPd) is an implementation the Precision Time Protocol (PTP) version
2 as defined by 'IEEE Std 1588-2008'. PTP provides precise time coordination of
Ethernet LAN connected computers. It was designed primarily for instrumentation
and control systems.

%prep
%setup -q

%build
aclocal -I m4
automake -f -a -c
autoconf
%configure
%make_build

%install
%makeinstall

%files

%changelog
* Tue May 23 2023 Menshchikov Evgeniy <menshchikovev@basealt.ru> 2.3.2-alt1
- First version for AltLinux Team.

