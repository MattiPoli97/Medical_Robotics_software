from setuptools import setup

package_name = 'medical_robot_demo'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Course Instructor',
    maintainer_email='instructor@example.com',
    description='Minimal medical robotics ROS 2 demo',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'target_publisher = medical_robot_demo.target_publisher:main',
            'robot_planner = medical_robot_demo.robot_planner:main',
        ],
    },
)
