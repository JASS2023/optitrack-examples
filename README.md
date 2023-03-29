# optitrack-examples
Examples of communication with OptiTrack system

## ROS
In the `ros` folder there is `optitrack.launch` file. You can run locally on the PC with ROS-noetic. Previously you should install `sudo apt install ros-noetic-vrpn-client-ros` 

In the `optitrack.launch` you need to set OptiTrack PC IP, for example, `server: 192.168.0.66`. Don't change ports.

After that, use command `roslaunch optitrack.launch` and you can read coordinates from the ros-topics. Use `rostopic list` to get a list of all ros topics

## Python

In the `python` folder there is `optitrack.py` file. You also need to set OptiTrack PC IP, for example, `optitrack = NatNetClient(server="192.168.0.66", dataPort=1511, commandPort=1510, verbose=False)`. Don't change ports.

Install python dependencies if you need and you can run this file.
