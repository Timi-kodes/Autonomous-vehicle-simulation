from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
import os
from ament_index_python.packages import get_package_share_path

def generate_launch_description():

    urdf_path = os.path.join(get_package_share_path('jetracer_description'), 'urdf', 'jetracer.urdf.xacro')

    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)

    return LaunchDescription([
        # Declare the robot state publisher node
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            
            parameters=[{'robot_description': robot_description}],      
        ),

        # Declare the RViz node
        Node(
            package='rviz2',
            executable='rviz2',
        
            arguments=['-d', os.path.join(get_package_share_path('jetracer_description'), 'rviz', 'jetracer.rviz')],
            output='screen'
        ),

        # Declare the joint state publisher GUI node
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",          
        ),

    ])