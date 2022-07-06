from setuptools import setup

package_name = 'example_kv_interfaces'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anishiyama',
    maintainer_email='mr081677@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker_kf  = example_kv_interfaces.example_publisher_kf:main',
            'listener_kf = example_kv_interfaces.example_subscriber_kf:main',
            'talker_ki = example_kv_interfaces.example_publisher_ki:main',
            'listener_ki = example_kv_interfaces.example_subscriber_ki:main',
            'talker_kd = example_kv_interfaces.example_publisher_kd:main',
            'listener_kd = example_kv_interfaces.example_subscriber_kd:main',
        ],
    },
)
