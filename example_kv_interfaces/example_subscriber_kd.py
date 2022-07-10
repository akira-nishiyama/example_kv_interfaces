import rclpy
from rclpy.node import Node

from kv_interfaces.msg import Kd

class ExampleSubscriberKd(Node):

    def __init__(self):
        super().__init__('example_subscriber_kd')
        self.subscription = self.create_subscription(
                Kd,
                'key_digit32',
                self.listener_callback,
                10)
        self.subscription # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: key:%s, val:0x%08x, status:0x%08x' % (msg.key, msg.val, msg.status))

def main(args=None):
    rclpy.init(args=args)

    example_subscriber = ExampleSubscriberKd()

    rclpy.spin(example_subscriber)

    example_subscriber.destroy_node()
    rclpy.shutdown()


if __name__== '__main__':
    main()
