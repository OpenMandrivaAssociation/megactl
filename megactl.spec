%define	name	megactl
%define	version	0.4.1
%define	release	%mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    LSI megaraid adapters status tracker
License:    GPL
Group:      System/Kernel and hardware
URL:        http://sourceforge.net/projects/megactl
Source:     http://downloads.sourceforge.net/megactl/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This project is a small collection of programs for examining configuration and
status of LSI megaraid adapters, especially Dell PERC RAID adapters, and
attached storage devices.

%prep
%setup -q

%build
cd src
%make

%install
rm -rf %{buildroot}
cd src

install -d -m 755 %{buildroot}%{_sbindir}
install -m 755 megactl megasasctl megatrace %{buildroot}%{_sbindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHOR COPYING README
%{_sbindir}/*

