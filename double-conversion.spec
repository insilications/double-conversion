#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : double-conversion
Version  : 2.0.1
Release  : 16
URL      : https://github.com/floitsch/double-conversion/archive/v2.0.1.tar.gz
Source0  : https://github.com/floitsch/double-conversion/archive/v2.0.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : cmake
BuildRequires : python-dev
BuildRequires : scons

%description
http://code.google.com/p/double-conversion
This project (double-conversion) provides binary-decimal and decimal-binary
routines for IEEE doubles.

%package dev
Summary: dev components for the double-conversion package.
Group: Development

%description dev
dev components for the double-conversion package.


%prep
%setup -q -n double-conversion-2.0.1

%build
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DBUILD_SHARED_LIBS:BOOL=ON -DINSTALL_LIB_DIR=/usr/lib64
make V=1  %{?_smp_mflags}
popd

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd clr-build ; make test ||: ; popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
## make_install_append content
mv %{buildroot}/usr/lib64/lib/* %{buildroot}/usr/lib64
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib/CMake/double-conversion/double-conversionConfig.cmake
/usr/lib/CMake/double-conversion/double-conversionConfigVersion.cmake
/usr/lib/CMake/double-conversion/double-conversionLibraryDepends-noconfig.cmake
/usr/lib/CMake/double-conversion/double-conversionLibraryDepends.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/double-conversion/bignum.h
/usr/include/double-conversion/cached-powers.h
/usr/include/double-conversion/diy-fp.h
/usr/include/double-conversion/double-conversion.h
/usr/include/double-conversion/fast-dtoa.h
/usr/include/double-conversion/fixed-dtoa.h
/usr/include/double-conversion/ieee.h
/usr/include/double-conversion/strtod.h
/usr/include/double-conversion/utils.h
/usr/lib64/*.so
