import argparse
import os
import sys

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    project_dir = get_package_share_directory('yolact_ros2')
    namespace = LaunchConfiguration('namespace', default='gavin')
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    config_file = os.path.join(project_dir, 'config', 'camera_params.yaml')

    remappings = [('/tf', 'tf'),
                  ('/tf_static', 'tf_static')]

    ld = LaunchDescription()

    ld.add_action(
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            namespace=namespace,
            name='controller',
            output='screen',
            parameters=[config_file],
            arguments=[],
            remappings=remappings))

    return ld
