# ROS 2 workspace

Everything will be run inside a docker container. Terminal 1:
```bash
docker run -it \ 
--name medical-ros \
-v "$(pwd):/ros2_ws" \
  ros:jazzy \
  bash
```

Inside the container, enter in `ros2_ws` folder and:
```bash
colcon build
source install/setup.bash
```

Run the publisher node:
```bash
ros2 run medical_robot_demo target_publisher
```

Terminal 2:
```bash
docker exec -it medical-ros bash
source install/setup.bash
ros2 run medical_robot_demo robot_planner
```

Inspect the system: Open Terminal 3 and run:
```bash
docker exec -it medical-ros bash
ros2 node list
ros2 topic list
ros2 topic echo /target_position
```

Conceptually:
```text
Target detector  -- /target_position -->  Robot planner
```

The target publisher stands in for a perception algorithm. In a later medical robotics lab, the coordinates could come from ultrasound, endoscopic vision or another imaging pipeline.
