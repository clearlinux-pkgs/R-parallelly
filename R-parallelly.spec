#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-parallelly
Version  : 1.28.1
Release  : 17
URL      : https://cran.r-project.org/src/contrib/parallelly_1.28.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/parallelly_1.28.1.tar.gz
Summary  : Enhancing the 'parallel' Package
Group    : Development/Tools
License  : LGPL-2.1
BuildRequires : buildreq-R

%description
<div id="badges"><!-- pkgdown markup -->
<a href="https://CRAN.R-project.org/web/checks/check_results_parallelly.html"><img border="0" src="https://www.r-pkg.org/badges/version/parallelly" alt="CRAN check status"/></a> <a href="https://github.com/HenrikBengtsson/parallelly/actions?query=workflow%3AR-CMD-check"><img border="0" src="https://github.com/HenrikBengtsson/parallelly/actions/workflows/R-CMD-check.yaml/badge.svg?branch=develop" alt="R CMD check status"/></a> <a href="https://github.com/HenrikBengtsson/parallelly/actions?query=workflow%3Arevdepcheck-top"><img border="0" src="https://github.com/HenrikBengtsson/parallelly/actions/workflows/revdepcheck-top.yaml/badge.svg?branch=develop" alt="Top reverse-dependency checks status"/></a>   <a href="https://codecov.io/gh/HenrikBengtsson/parallelly"><img border="0" src="https://codecov.io/gh/HenrikBengtsson/parallelly/branch/develop/graph/badge.svg" alt="Coverage Status"/></a>
</div>

%prep
%setup -q -c -n parallelly
cd %{_builddir}/parallelly

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631213508

%install
export SOURCE_DATE_EPOCH=1631213508
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library parallelly
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library parallelly
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library parallelly
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc parallelly || :


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
/usr/lib64/R/library/parallelly/NEWS
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
/usr/lib64/R/library/parallelly/tests/cpuLoad.R
/usr/lib64/R/library/parallelly/tests/freeCores.R
/usr/lib64/R/library/parallelly/tests/freePort.R
/usr/lib64/R/library/parallelly/tests/incl/end.R
/usr/lib64/R/library/parallelly/tests/incl/start,load-only.R
/usr/lib64/R/library/parallelly/tests/incl/start.R
/usr/lib64/R/library/parallelly/tests/isConnectionValid.R
/usr/lib64/R/library/parallelly/tests/isForkedChild.R
/usr/lib64/R/library/parallelly/tests/makeClusterMPI.R
/usr/lib64/R/library/parallelly/tests/makeClusterPSOCK.R
/usr/lib64/R/library/parallelly/tests/options-and-envvars.R
/usr/lib64/R/library/parallelly/tests/r_bug18119.R
/usr/lib64/R/library/parallelly/tests/startup.R
/usr/lib64/R/library/parallelly/tests/utils.R
