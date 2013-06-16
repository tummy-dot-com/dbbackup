%define name    dbbackup
%define version 1.08
%define release 1
%define prefix  %{_prefix}

Summary:      Script to automatically back up SQL and other databases
Name:         %{name}
Version:      %{version}
Release:      %{release}
License:      GPLv2+
Group:        Applications/System
URL:          http://www.tummy.com/
Source0:      ftp://ftp.tummy.com/pub/tummy/dbbackup/%{name}-%{version}.tar.gz
Packager:     Sean Reifschneider <jafo-rpms@tummy.com>
BuildRoot:    /var/tmp/%{name}-root
BuildArch:    noarch

%description
This is a simple script that can be used to back up Postgres, MySQL, and
the system RPM databases running on the system.  It writes the backups
out to a directory and deletes files older than a certain number of days.
It's operation can be modified by editing "/etc/dbbackup.conf".  Backups,
by default, are written to "/var/lib/dbbackup".

%prep
%setup
%build

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"/etc/cron.daily
cp dbbackup "$RPM_BUILD_ROOT"/etc/cron.daily
cp dbbackup.conf-dist "$RPM_BUILD_ROOT"/etc/dbbackup.conf-dist
cp dbbackup.conf "$RPM_BUILD_ROOT"/etc/dbbackup.conf
chmod 700 "$RPM_BUILD_ROOT"/etc/dbbackup.conf
mkdir -p "$RPM_BUILD_ROOT"/usr/bin
cp extract_sql "$RPM_BUILD_ROOT"/usr/bin
chmod 755 "$RPM_BUILD_ROOT"/usr/bin/extract_sql

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README LICENSE
%attr(755,root,root) /etc/cron.daily/dbbackup
%attr(600,root,root) /etc/dbbackup.conf-dist
%config(noreplace) %attr(600,root,root) /etc/dbbackup.conf
%attr(755,root,root) /usr/bin/extract_sql

%changelog
* Sun Apr 19 2009 Sean Reifschneider <jafo@tummy.com> - 1.13-1
- Release of 1.13.
