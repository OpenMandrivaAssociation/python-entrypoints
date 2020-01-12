%define fname entrypoints
%define sum Discover and load entry points from installed packages
%define python2_wheelname %{fname}-%{version}-py2.py3-none-any.whl
%define python3_wheelname %python2_wheelname


Name:		python-%{fname}
Summary:	%{sum}
Version:	0.3.0
Release:	1
Source0:	https://pypi.io/packages/source/e/%{fname}/%{fname}-0.3.tar.gz
URL:		https://entrypoints.readthedocs.io/
Group:		Development/Python
License:	BSD
BuildArch:	noarch
BuildRequires:	python3dist(pip)
#BuildRequires:	python3dist(flit)
BuildRequires:	python3dist(sphinx)


%description
The entrypoints module contains functions to find and load entry points.


%package -n python-%{fname}-doc
Group:          Documentation
Summary:	Documentation for python-entrypoints


%description -n python-%{fname}-doc
Documentation files for python-entrypoints


%prep
%autosetup -n %{fname}-0.3

# We don't need to verify PyPI classifiers, because the package is already
# there. So just make specified classifiers "valid".
mkdir -p .cache/flit
if false; then
%{__python} -c "with open('flit.ini', 'rb') as inf:
    with open('.cache/flit/classifiers.lst', 'wb') as outf:
        enable_output = False
        for line in inf:
            if enable_output:
                if b'=' in line:
                    break
                outf.write(line)
            elif b'classifiers' in line:
                outf.write(line.split(b'=')[1])
                enable_output = True
"
fi

%build
%py_build
if false; then
XDG_CACHE_HOME=$PWD/.cache flit wheel
fi

pushd doc
make html PYTHON="%{__python}" SPHINXBUILD=sphinx-build-%{python_version}
rm _build/html/.buildinfo
popd


%install
%py_install

%files
%license LICENSE
%{python3_sitelib}/*


%files -n python-%{fname}-doc
%doc doc/_build/html
%license LICENSE
