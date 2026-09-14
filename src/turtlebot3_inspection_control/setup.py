from setuptools import setup


package_name = "turtlebot3_inspection_control"

setup(
    name=package_name,
    version="0.1.0",
    packages=["ros2_bridge"],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=False,
    maintainer="Robotics Team 1",
    maintainer_email="robotics@example.com",
    description="ROS 2 control nodes for the TurtleBot3 inspection project.",
    license="TODO",
    entry_points={
        "console_scripts": [
            "cmd_vel_bridge = ros2_bridge.cmd_vel_bridge:main",
            "cmd_vel_mux = ros2_bridge.cmd_vel_mux:main",
            "wifi_glove_teleop = ros2_bridge.wifi_glove_teleop:main",
            "waypoint_handoff_mission = ros2_bridge.waypoint_handoff_mission:main",
            "waypoint_coordinate_sampler = ros2_bridge.waypoint_coordinate_sampler:main",
        ],
    },
)
