import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

class TargetPublisher(Node):
    def __init__(self):
        super().__init__('target_publisher')
        # TODO 1: create a publisher for geometry_msgs/Point on /target_position
        self.publisher_ = None
        self.timer = self.create_timer(1.0, self.publish_target)

    def publish_target(self):
        msg = Point()
        # TODO 2: assign x, y and z target coordinates
        msg.x = 0.0
        msg.y = 0.0
        msg.z = 0.0
        # TODO 3: publish msg
        # self.publisher_.publish(msg)
        self.get_logger().info(f'Target: ({msg.x:.2f}, {msg.y:.2f}, {msg.z:.2f}) m')

def main(args=None):
    rclpy.init(args=args)
    node = TargetPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
