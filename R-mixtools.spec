#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mixtools
Version  : 1.2.0
Release  : 36
URL      : https://cran.r-project.org/src/contrib/mixtools_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mixtools_1.2.0.tar.gz
Summary  : Tools for Analyzing Finite Mixture Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-mixtools-lib = %{version}-%{release}
Requires: R-kernlab
Requires: R-segmented
BuildRequires : R-kernlab
BuildRequires : R-segmented
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-mixtools package.
Group: Libraries

%description lib
lib components for the R-mixtools package.


%prep
%setup -q -c -n mixtools
cd %{_builddir}/mixtools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589536399

%install
export SOURCE_DATE_EPOCH=1589536399
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mixtools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mixtools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mixtools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
R CMD check --no-manual --no-examples --no-codoc --no-vignettes mixtools || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mixtools/CITATION
/usr/lib64/R/library/mixtools/DESCRIPTION
/usr/lib64/R/library/mixtools/INDEX
/usr/lib64/R/library/mixtools/Meta/Rd.rds
/usr/lib64/R/library/mixtools/Meta/data.rds
/usr/lib64/R/library/mixtools/Meta/features.rds
/usr/lib64/R/library/mixtools/Meta/hsearch.rds
/usr/lib64/R/library/mixtools/Meta/links.rds
/usr/lib64/R/library/mixtools/Meta/nsInfo.rds
/usr/lib64/R/library/mixtools/Meta/package.rds
/usr/lib64/R/library/mixtools/Meta/vignette.rds
/usr/lib64/R/library/mixtools/NAMESPACE
/usr/lib64/R/library/mixtools/NEWS
/usr/lib64/R/library/mixtools/R/mixtools
/usr/lib64/R/library/mixtools/R/mixtools.rdb
/usr/lib64/R/library/mixtools/R/mixtools.rdx
/usr/lib64/R/library/mixtools/data/CO2data.RData
/usr/lib64/R/library/mixtools/data/Habituationdata.RData
/usr/lib64/R/library/mixtools/data/NOdata.RData
/usr/lib64/R/library/mixtools/data/RTdata.RData
/usr/lib64/R/library/mixtools/data/RTdata2.RData
/usr/lib64/R/library/mixtools/data/RanEffdata.RData
/usr/lib64/R/library/mixtools/data/RodFramedata.RData
/usr/lib64/R/library/mixtools/data/Waterdata.RData
/usr/lib64/R/library/mixtools/data/WaterdataFull.RData
/usr/lib64/R/library/mixtools/data/tonedata.RData
/usr/lib64/R/library/mixtools/doc/index.html
/usr/lib64/R/library/mixtools/doc/mixtools.R
/usr/lib64/R/library/mixtools/doc/mixtools.Rnw
/usr/lib64/R/library/mixtools/doc/mixtools.pdf
/usr/lib64/R/library/mixtools/help/AnIndex
/usr/lib64/R/library/mixtools/help/aliases.rds
/usr/lib64/R/library/mixtools/help/mixtools.rdb
/usr/lib64/R/library/mixtools/help/mixtools.rdx
/usr/lib64/R/library/mixtools/help/paths.rds
/usr/lib64/R/library/mixtools/html/00Index.html
/usr/lib64/R/library/mixtools/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mixtools/libs/mixtools.so
/usr/lib64/R/library/mixtools/libs/mixtools.so.avx2
/usr/lib64/R/library/mixtools/libs/mixtools.so.avx512
