import rclpy
from rclpy.node import Node

from kv_interfaces.msg import Ki

class ExampleSubscriberKi(Node):

    def __init__(self):
        super().__init__('example_subscriber_ki')
        self.subscription = self.create_subscription(
                Ki,
                'key_int32',
                self.listener_callback,
                10)
        self.subscription # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: key:%s, val:0x%x, status:0x%x' % (msg.key, msg.val, msg.status))

def main(args=None):
    rclpy.init(args=args)

    example_subscriber = ExampleSubscriberKi()

    rclpy.spin(example_subscriber)

    example_subscriber.destroy_node()
    rclpy.shutdown()


if __name__== '__main__':
    main()
