import rclpy
from rclpy.node import Node

from kv_interfaces.msg import Kf

class ExamplePublisherKf(Node):

    def __init__(self):
        super().__init__('example_publisher_kf')
        self.float_publisher_ = self.create_publisher(Kf, 'key_float', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Kf()
        msg.key = "key_float"
        msg.val = self.i
        msg.status += self.i
        self.float_publisher_.publish(msg)
        self.get_logger().info('Publishing: key:%s, val:%f, status:0x%08x' % (msg.key,  msg.val, msg.status))
        self.i += 0.1


def main(args=None):
    rclpy.init(args=args)

    example_publisher = ExamplePublisherKf()

    rclpy.spin(example_publisher)

    example_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

