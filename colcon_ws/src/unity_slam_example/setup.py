import glob
import os

from setuptools import setup

package_name = 'unity_slam_example'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), ['rviz/nav2_unity.rviz',
                                               'launch/endpoint_launcher.py', 
                                               'launch/tb3_nav_slam_launcher.py']),
        (os.path.join('share', package_name), ['params/nav2_params.yaml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Unity Robotics',
    maintainer_email='unity-robotics@unity3d.com',
    description='Unity Robotics Nav2 SLAM Example',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server_endpoint = unity_slam_example.server_endpoint:main',
        ],
    },
)