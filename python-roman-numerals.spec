%define module roman-numerals
%define oname roman_numerals

Name:		python-roman-numerals
Version:	4.1.0
Release:	1
Summary:	Manipulate well-formed Roman numerals
License:	0BSD or CC0-1.0
Group:		Development/Python
URL:		https://pypi.org/project/roman-numerals/
Source0:	https://files.pythonhosted.org/packages/source/r/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(wheel)

%rename python-roman-numerals-py

%description
Manipulate well-formed Roman numerals

%prep
%autosetup -n %{oname}-%{version} -p1
# fix licence parameter for flit-core
sed -i 's/license = "0BSD OR CC0-1.0"/license = { file="LICENSE.rst" }/g' pyproject.toml

%files
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
