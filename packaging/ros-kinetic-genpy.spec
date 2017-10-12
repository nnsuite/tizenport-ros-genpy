Name:           ros-kinetic-genpy
Version:        0.6.6
Release:        0
Summary:        ROS genpy package
Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  gcc-c++
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-genmsg
Requires:       ros-kinetic-genmsg
Requires:       python-PyYAML

%define         ros_distro kinetic
%define         ros_root /opt/ros
%define         install_path %{ros_root}/%{ros_distro}
%define         src_name genpy

%description
Python ROS message and service generators.

%prep
%setup -q
cp %{SOURCE1001} .

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
mkdir build && cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX="%{install_path}" \
        -DCMAKE_PREFIX_PATH="%{install_path}" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
pushd build
make install DESTDIR=%{buildroot}
popd

%files -f build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)
%{install_path}/lib/python2.7/site-packages/*

%changelog
* Fri May 09 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.14-0
- Autogenerated by Bloom
