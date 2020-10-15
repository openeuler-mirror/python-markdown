%{!?python3_version: %global python3_version %(%{__python3} -c "import sys; sys.stdout.write(sys.version[:3])")}

Name:           python-markdown
Version:        3.3.1
Release:        1
Summary:        A Python implementation of John Gruber’s Markdown
License:        BSD
URL:            https://pypi.org/project/Markdown/
Source0:        https://pypi.python.org/packages/source/M/Markdown/Markdown-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel >= 2.6 python-nose python3-devel >= 3.1 python3-nose python3-pyaml

%description
This is a Python implementation of John Gruber’s Markdown.
It is almost completely compliant with the reference implementation,
though there are a few known issues.

%package -n python3-markdown
Summary:        Markdown implementation in Python
Requires:       python3 >= 3.1

%description -n python3-markdown
This is a Python implementation of John Gruber’s Markdown.
It is almost completely compliant with the reference implementation,
though there are a few known issues.

%prep
%autosetup -n Markdown-%{version} -p1

find markdown -type f -name '*.py' -exec sed -i -e '/^#!/{1D}' {} \;
find docs -type f -exec sed -i 's/\r//' {} \;

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python3} -m unittest discover tests

%files -n python3-markdown
%{python3_sitelib}/*
%{_bindir}/markdown_py

%changelog
%changelog
* Thu Oct 15 2020 Zhipeng Xie <xiezhipeng1@huawei.com> - 3.3.1-1
- upgrade to 3.3.1

* Tue Sep 29 2020 liuweibo <liuweibo10@huawei.com> - 2.4.1-14
- Fix Source0

* Tue Nov 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.4.1-13
- Package init
