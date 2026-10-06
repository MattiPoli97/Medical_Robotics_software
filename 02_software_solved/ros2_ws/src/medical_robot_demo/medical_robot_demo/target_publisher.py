import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

class TargetPublisher(Node):
    def __init__(self):
        super().__init__('target_publisher')
        self.publisher_ = self.create_publisher(Point, '/target_position', 10)
        self.timer = self.create_timer(1.0, self.publish_target)

    def publish_target(self):
        msg = Point()
        msg.x = 0.12
        msg.y = 0.08
        msg.z = 0.15
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published target: ({msg.x:.2f}, {msg.y:.2f}, {msg.z:.2f}) m')

def main(args=None):
    rclpy.init(args=args)
    node = TargetPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
