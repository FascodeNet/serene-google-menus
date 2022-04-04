Summary: serene google menus
Name: serene-google-menus
Version: 1.0.5
Release: 1%{?dist}
Group: User Interface/Desktops
BuildArch: noarch
License: NONE
Packager: kokkiemouse
Vendor: INDETAIL

Source0: https://github.com/FascodeNet/serene-google-menus/archive/e8b75a0a324067bf030ac9490a82b1487527e555.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
serene-google-menus
%prep
rm -rf $RPM_BUILD_ROOT

%autosetup -n %{name}-e8b75a0a324067bf030ac9490a82b1487527e555

%build

%install
rm -rf README.md
mkdir -p $RPM_BUILD_ROOT
cp -arf ./usr $RPM_BUILD_ROOT/

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
/usr/share/
%changelog
