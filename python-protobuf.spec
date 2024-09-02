Summary:	Python 2 bindings for Protocol Buffers
Summary(pl.UTF-8):	Wiązania Pythona 2 do buforów protokołowych (Protocol Buffers)
Name:		python-protobuf
# keep 3.17.x here for python2 support
Version:	3.17.3
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/protobuf/
Source0:	https://files.pythonhosted.org/packages/source/p/protobuf/protobuf-%{version}.tar.gz
# Source0-md5:	03728f8c4d6d67ac9e0017f227a29538
URL:		https://pypi.org/project/protobuf/
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for Protocol Buffers.

%description -l pl.UTF-8
Wiązania Pythona 2 do buforów protokołowych (Protocol Buffers).

%prep
%setup -q -n protobuf-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py_sitescriptdir}/google
%{py_sitescriptdir}/google/protobuf
%{py_sitescriptdir}/protobuf-%{version}-py*.egg-info
%{py_sitescriptdir}/protobuf-%{version}-py*-nspkg.pth
