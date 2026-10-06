import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

class RobotPlanner(Node):
    def __init__(self):
        super().__init__('robot_planner')
        # TODO 4: subscribe to /target_position using Point and self.target_callback
        self.subscription = None

    def target_callback(self, msg):
        # TODO 5: compute Euclidean distance from origin to target
        distance = None
        self.get_logger().info(
            f'Received target ({msg.x:.2f}, {msg.y:.2f}, {msg.z:.2f}) m | distance = {distance:.3f} m'
        )

def main(args=None):
    rclpy.init(args=args)
    node = RobotPlanner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
