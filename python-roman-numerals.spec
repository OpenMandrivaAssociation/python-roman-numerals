Name:		python-roman-numerals
Version:	3.1.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/roman_numerals/roman_numerals-%{version}.tar.gz
Summary:	Manipulate well-formed Roman numerals
URL:		https://pypi.org/project/roman-numerals/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Manipulate well-formed Roman numerals

%files
%{py_sitedir}/roman_numerals
%{py_sitedir}/roman_numerals-*.*-info
