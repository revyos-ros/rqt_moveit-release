%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rqt-moveit
Version:        1.0.1
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS rqt_moveit package

License:        BSD
URL:            http://wiki.ros.org/rqt_moveit
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-python-qt-binding >= 0.2.19
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-rqt-gui
Requires:       ros-rolling-rqt-gui-py
Requires:       ros-rolling-rqt-py-common
Requires:       ros-rolling-rqt-topic
Requires:       ros-rolling-sensor-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-rosidl-default-generators
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
An rqt-based tool that assists monitoring tasks for MoveIt! motion planner
developers and users. Currently the following items are monitored if they are
either running, existing or published: Node: /move_group Parameter:
[/robot_description, /robot_description_semantic] Topic: Following types are
monitored. Published &quot;names&quot; are ignored. [sensor_msgs/PointCloud,
sensor_msgs/PointCloud2, sensor_msgs/Image, sensor_msgs/CameraInfo] Since this
package is not made by the MoveIt! development team (although with assistance
from the them), please post issue reports to the designated tracker (not
MoveIt!'s main tracker).

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Feb 08 2022 Isaac I.Y. Saito <iisaito@kinugarage.com> - 1.0.1-2
- Autogenerated by Bloom

