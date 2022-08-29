Summary:	C macros for hash tables and more
Summary(pl.UTF-8):	Makra C do tablic haszujących itp.
Name:		uthash
Version:	2.3.0
Release:	1
License:	BSD-like
Group:		Libraries
#Source0Download: https://github.com/troydhanson/uthash/tags
Source0:	https://github.com/troydhanson/uthash/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9a4f0a675ca179b62ebc56b2dd8b59ee
URL:		http://troydhanson.github.io/uthash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C macros for hash tables and more.

%description -l pl.UTF-8
Makra C do tablic haszujących itp.

%package devel
Summary:	C macros for hash tables and more
Summary(pl.UTF-8):	Makra C do tablic haszujących itp.
Group:		Development/Libraries

%description devel
C macros for hash tables and more.

%description devel -l pl.UTF-8
Makra C do tablic haszujących itp.

%package apidocs
Summary:	API documentation for uthash library
Summary(pl.UTF-8):	Dokumentacja API biblioteki uthash
Group:		Documentation

%description apidocs
API documentation for uthash library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki uthash.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

cp -p src/*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md doc/ChangeLog.txt
%{_includedir}/utarray.h
%{_includedir}/uthash.h
%{_includedir}/utlist.h
%{_includedir}/utringbuffer.h
%{_includedir}/utstack.h
%{_includedir}/utstring.h

%files apidocs
%defattr(644,root,root,755)
%doc doc/*.{css,html,png}
