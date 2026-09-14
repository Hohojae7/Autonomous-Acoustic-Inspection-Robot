cmake_minimum_required(VERSION 3.8)
project(turtlebot3_inspection_bringup)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch configs maps
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
