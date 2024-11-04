#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: 356da62
#
Name     : R-parallelly
Version  : 1.38.0
Release  : 44
URL      : https://cran.r-project.org/src/contrib/parallelly_1.38.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/parallelly_1.38.0.tar.gz
Summary  : Enhancing the 'parallel' Package
Group    : Development/Tools
License  : LGPL-2.1+
Requires: R-parallelly-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<div id="badges"><!-- pkgdown markup -->
<a href="https://CRAN.R-project.org/web/checks/check_results_parallelly.html"><img border="0" src="https://www.r-pkg.org/badges/version/parallelly" alt="CRAN check status"/></a> <a href="https://github.com/HenrikBengtsson/parallelly/actions?query=workflow%3AR-CMD-check"><img border="0" src="https://github.com/HenrikBengtsson/parallelly/actions/workflows/R-CMD-check.yaml/badge.svg?branch=develop" alt="R CMD check status"/></a> <a href="https://github.com/HenrikBengtsson/parallelly/actions?query=workflow%3Arevdepcheck-top"><img border="0" src="https://github.com/HenrikBengtsson/parallelly/actions/workflows/revdepcheck-top.yaml/badge.svg?branch=develop" alt="Top reverse-dependency checks status"/></a>    <a href="https://app.codecov.io/gh/HenrikBengtsson/parallelly"><img border="0" src="https://codecov.io/gh/HenrikBengtsson/parallelly/branch/develop/graph/badge.svg" alt="Coverage Status"/></a>
</div>

%package lib
Summary: lib components for the R-parallelly package.
Group: Libraries

%description lib
lib components for the R-parallelly package.


%prep
%setup -q -n parallelly
pushd ..
cp -a parallelly buildavx2
popd
pushd ..
cp -a parallelly buildavx512
popd
pushd ..
cp -a parallelly buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1722279314

%install
export SOURCE_DATE_EPOCH=1722279314
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/parallelly/DESCRIPTION
/usr/lib64/R/library/parallelly/INDEX
/usr/lib64/R/library/parallelly/Meta/Rd.rds
/usr/lib64/R/library/parallelly/Meta/features.rds
/usr/lib64/R/library/parallelly/Meta/hsearch.rds
/usr/lib64/R/library/parallelly/Meta/links.rds
/usr/lib64/R/library/parallelly/Meta/nsInfo.rds
/usr/lib64/R/library/parallelly/Meta/package.rds
/usr/lib64/R/library/parallelly/NAMESPACE
/usr/lib64/R/library/parallelly/NEWS.md
/usr/lib64/R/library/parallelly/R/parallelly
/usr/lib64/R/library/parallelly/R/parallelly.rdb
/usr/lib64/R/library/parallelly/R/parallelly.rdx
/usr/lib64/R/library/parallelly/WORDLIST
/usr/lib64/R/library/parallelly/help/AnIndex
/usr/lib64/R/library/parallelly/help/aliases.rds
/usr/lib64/R/library/parallelly/help/figures/lifecycle-maturing-blue.svg
/usr/lib64/R/library/parallelly/help/figures/logo.png
/usr/lib64/R/library/parallelly/help/parallelly.rdb
/usr/lib64/R/library/parallelly/help/parallelly.rdx
/usr/lib64/R/library/parallelly/help/paths.rds
/usr/lib64/R/library/parallelly/html/00Index.html
/usr/lib64/R/library/parallelly/html/R.css
/usr/lib64/R/library/parallelly/tests/as.cluster.R
/usr/lib64/R/library/parallelly/tests/availableCores.R
/usr/lib64/R/library/parallelly/tests/availableWorkers.R
/usr/lib64/R/library/parallelly/tests/cgroups.R
/usr/lib64/R/library/parallelly/tests/cpuLoad.R
/usr/lib64/R/library/parallelly/tests/freeCores.R
/usr/lib64/R/library/parallelly/tests/freePort.R
/usr/lib64/R/library/parallelly/tests/incl/end.R
/usr/lib64/R/library/parallelly/tests/incl/start,load-only.R
/usr/lib64/R/library/parallelly/tests/incl/start.R
/usr/lib64/R/library/parallelly/tests/isConnectionValid.R
/usr/lib64/R/library/parallelly/tests/isForkedChild.R
/usr/lib64/R/library/parallelly/tests/killNode.R
/usr/lib64/R/library/parallelly/tests/makeClusterMPI.R
/usr/lib64/R/library/parallelly/tests/makeClusterPSOCK.R
/usr/lib64/R/library/parallelly/tests/makeClusterSequential.R
/usr/lib64/R/library/parallelly/tests/options-and-envvars.R
/usr/lib64/R/library/parallelly/tests/r_bug18119.R
/usr/lib64/R/library/parallelly/tests/startup.R
/usr/lib64/R/library/parallelly/tests/utils.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/parallelly/libs/parallelly.so
/V4/usr/lib64/R/library/parallelly/libs/parallelly.so
/VA/usr/lib64/R/library/parallelly/libs/parallelly.so
/usr/lib64/R/library/parallelly/libs/parallelly.so
