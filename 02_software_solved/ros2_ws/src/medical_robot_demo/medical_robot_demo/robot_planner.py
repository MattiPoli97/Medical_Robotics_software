import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

class RobotPlanner(Node):
    def __init__(self):
        super().__init__('robot_planner')
        self.subscription = self.create_subscription(Point, '/target_position', self.target_callback, 10)

    def target_callback(self, msg):
        distance = math.sqrt(msg.x**2 + msg.y**2 + msg.z**2)
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
