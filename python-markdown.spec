%{!?python2_sitelib: %global python2_sitelib %{python_sitelib}}
%{!?python3_version: %global python3_version %(%{__python3} -c "import sys; sys.stdout.write(sys.version[:3])")}

Name:           python-markdown
Version:        2.4.1
Release:        14
Summary:        A Python implementation of John Gruber’s Markdown
License:        BSD
URL:            https://pypi.org/project/Markdown/
Source0:        https://pypi.python.org/packages/source/M/Markdown/Markdown-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel >= 2.6 python-nose python3-devel >= 3.1 python3-nose

%description
This is a Python implementation of John Gruber’s Markdown.
It is almost completely compliant with the reference implementation,
though there are a few known issues.

%package -n python2-markdown
Summary:        A Python implementation of John Gruber’s Markdown
Requires:       python >= 2.6
Provides:       python2-markdown(abi) = 2.4

%description -n python2-markdown
This is a Python implementation of John Gruber’s Markdown.
It is almost completely compliant with the reference implementation,
though there are a few known issues.

%package -n python3-markdown
Summary:        Markdown implementation in Python
Requires:       python3 >= 3.1
Provides:       python3-markdown(abi) = 2.4

%description -n python3-markdown
This is a Python implementation of John Gruber’s Markdown.
It is almost completely compliant with the reference implementation,
though there are a few known issues.

%prep
%autosetup -n Markdown-%{version} -p1

find markdown -type f -name '*.py' -exec sed -i -e '/^#!/{1D}' {} \;
find bin docs -type f -exec sed -i 's/\r//' {} \;
cp -a . %{py3dir}

%build
%{__python2} setup.py build
cd %{py3dir}
%{__python3} setup.py build
cd -

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
mv %{buildroot}%{_bindir}/markdown_py{,-%{python_version}}

cd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
cd -
mv %{buildroot}%{_bindir}/markdown_py{,-%{python3_version}}

ln -s markdown_py-%{python_version} %{buildroot}%{_bindir}/markdown_py

%check
%{__python2} run-tests.py || :

cd %{py3dir}
%{__python3} run-tests.py || :
cd -

%files -n python2-markdown
%doc build/docs/*
%{python2_sitelib}/*
%{_bindir}/markdown_py
%{_bindir}/markdown_py-%{python_version}

%files -n python3-markdown
%doc build/docs/*
%{python3_sitelib}/*
%{_bindir}/markdown_py-%{python3_version}

%changelog
%changelog
* Tue Sep 29 2020 liuweibo <liuweibo10@huawei.com> - 2.4.1-14
- Fix Source0

* Tue Nov 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.4.1-13
- Package init
