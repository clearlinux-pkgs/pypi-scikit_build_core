#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v12
# autospec commit: a5d3013
#
Name     : pypi-scikit_build_core
Version  : 0.9.7
Release  : 5
URL      : https://files.pythonhosted.org/packages/7d/03/5893ab545ea0e96c172c9281511904b1f0d2711052cc80f9d200c36975a7/scikit_build_core-0.9.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/7d/03/5893ab545ea0e96c172c9281511904b1f0d2711052cc80f9d200c36975a7/scikit_build_core-0.9.7.tar.gz
Summary  : Build backend for CMake based projects
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: pypi-scikit_build_core-license = %{version}-%{release}
Requires: pypi-scikit_build_core-python = %{version}-%{release}
Requires: pypi-scikit_build_core-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# scikit-build-core
[![Documentation Status][rtd-badge]][rtd-link]
[![GitHub Discussion][github-discussions-badge]][github-discussions-link]
[![Discord][discord-badge]][discord-link]

%package license
Summary: license components for the pypi-scikit_build_core package.
Group: Default

%description license
license components for the pypi-scikit_build_core package.


%package python
Summary: python components for the pypi-scikit_build_core package.
Group: Default
Requires: pypi-scikit_build_core-python3 = %{version}-%{release}

%description python
python components for the pypi-scikit_build_core package.


%package python3
Summary: python3 components for the pypi-scikit_build_core package.
Group: Default
Requires: python3-core
Provides: pypi(scikit_build_core)
Requires: pypi(packaging)
Requires: pypi(pathspec)

%description python3
python3 components for the pypi-scikit_build_core package.


%prep
%setup -q -n scikit_build_core-0.9.7
cd %{_builddir}/scikit_build_core-0.9.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719592970
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-scikit_build_core
cp %{_builddir}/scikit_build_core-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-scikit_build_core/d83c74455ed330bb1074bc9f22d4dd64ccc56242 || :
cp %{_builddir}/scikit_build_core-%{version}/docs/examples/downstream/nanobind_example/LICENSE %{buildroot}/usr/share/package-licenses/pypi-scikit_build_core/3fae42cfffc123f30fada8748f70ea999d5ee060 || :
cp %{_builddir}/scikit_build_core-%{version}/docs/examples/downstream/pybind11_example/LICENSE %{buildroot}/usr/share/package-licenses/pypi-scikit_build_core/53a95a113732642d33f43f8beaa9993a0654a3f8 || :
cp %{_builddir}/scikit_build_core-%{version}/src/scikit_build_core/_vendor/pyproject_metadata/LICENSE %{buildroot}/usr/share/package-licenses/pypi-scikit_build_core/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9 || :
cp %{_builddir}/scikit_build_core-%{version}/src/scikit_build_core/resources/find_python/Copyright.txt %{buildroot}/usr/share/package-licenses/pypi-scikit_build_core/d8969c402f7a24729c2cf988628f701668cab342 || :
cp %{_builddir}/scikit_build_core-%{version}/tests/packages/simple_pyproject_ext/LICENSE %{buildroot}/usr/share/package-licenses/pypi-scikit_build_core/d83c74455ed330bb1074bc9f22d4dd64ccc56242 || :
cp %{_builddir}/scikit_build_core-%{version}/tests/packages/simple_pyproject_script_with_flags/LICENSE %{buildroot}/usr/share/package-licenses/pypi-scikit_build_core/d83c74455ed330bb1074bc9f22d4dd64ccc56242 || :
cp %{_builddir}/scikit_build_core-%{version}/tests/packages/simple_pyproject_source_dir/LICENSE %{buildroot}/usr/share/package-licenses/pypi-scikit_build_core/d83c74455ed330bb1074bc9f22d4dd64ccc56242 || :
cp %{_builddir}/scikit_build_core-%{version}/tests/packages/simple_setuptools_ext/LICENSE %{buildroot}/usr/share/package-licenses/pypi-scikit_build_core/d83c74455ed330bb1074bc9f22d4dd64ccc56242 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-scikit_build_core/3fae42cfffc123f30fada8748f70ea999d5ee060
/usr/share/package-licenses/pypi-scikit_build_core/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9
/usr/share/package-licenses/pypi-scikit_build_core/53a95a113732642d33f43f8beaa9993a0654a3f8
/usr/share/package-licenses/pypi-scikit_build_core/d83c74455ed330bb1074bc9f22d4dd64ccc56242
/usr/share/package-licenses/pypi-scikit_build_core/d8969c402f7a24729c2cf988628f701668cab342

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
