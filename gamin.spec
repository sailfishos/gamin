# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       gamin
Summary:    Library providing the FAM File Alteration Monitor API
Version:    0.1.10
Release:    1
Group:      System/Libraries
License:    LGPL
URL:        http://www.gnome.org/~veillard/gamin/
Source0:    http://download.gnome.org/sources/gamin/0.1/%{name}-%{version}.tar.bz2
Source100:  gamin.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  automake
BuildRequires:  libtool


%description
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.



%package devel
Summary:    Libraries, includes, etc. to embed the Gamin library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This C library provides an API and ABI compatible file alteration
monitor mechanism compatible with FAM but not dependent on a system wide
daemon.


%package doc
Summary:    Documents for gamin
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
This package provides documents for gamin.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig








%files
%defattr(-,root,root,-)
# >> files
%doc Copyright
%{_libdir}/lib*.so.*
%{_libexecdir}/gam_server
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%{_libdir}/lib*.so
%{_includedir}/fam.h
%{_libdir}/pkgconfig/gamin.pc
# << files devel

%files doc
%defattr(-,root,root,-)
# >> files doc
%doc doc/*.html
%doc doc/*.gif
%doc doc/*.txt
# << files doc

