# ROS 2 workspace

Prerequisite: a working ROS 2 installation with `rclpy`, `geometry_msgs`, `colcon` and a sourced ROS environment.

Run everything inside docker: 
```bash
docker run -it \
  --name medical-ros \
  -v "$(pwd):/ros2_ws" \
  ros:jazzy \
  bash
```

From this `ros2_ws` folder:
```bash
colcon build
source install/setup.bash
```

Terminal 1:
```bash
ros2 run medical_robot_demo target_publisher
```

Terminal 2:
```bash
docker exec -it medical-ros bash
cd /ros2_ws
source install/setup.bash
ros2 run medical_robot_demo robot_planner
```

Inspect the system in Teminal 3:
```bash
docker exec -it medical-ros bash
cd /ros2_ws
source install/setup.bash
ros2 node list
ros2 topic list
ros2 topic echo /target_position
ros2 topic info /target_position
```

Conceptually:
```text
Target detector  -- /target_position -->  Robot planner
```

The target publisher stands in for a perception algorithm. In a later medical robotics lab, the coordinates could come from ultrasound, endoscopic vision or another imaging pipeline.
