from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ublox_gps_dir = get_package_share_directory('ublox_gps')
    
    # Moving base launch file
    movingbase_launch = os.path.join(ublox_gps_dir, 'launch', 'ublox_gps_movingbase_node-launch.py')
    ublox_movingbase = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(movingbase_launch)
    )

    # Rover launch file
    rover_launch = os.path.join(ublox_gps_dir, 'launch', 'ublox_gps_rover_node-launch.py')
    ublox_rover = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rover_launch)
    )

    return LaunchDescription([
        ublox_movingbase,
        ublox_rover
    ])
