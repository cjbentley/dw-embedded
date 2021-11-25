FROM ros:noetic-robot
RUN apt-get update && apt-get install -y ros-noetic-rtabmap-ros && apt-get clean

# Development tools, can be removed for deployment
RUN apt-get install -y wget nano

CMD roslaunch rtabmap_ros rgbd_mapping.launch rtabmap_args:="--delete_db_on_start --Vis/MaxFeatures 500 --Mem/ImagePreDecimation 2 --Mem/ImagePostDecimation 2 --Kp/DetectorStrategy 6 --OdomF2M/MaxSize 1000 --Odom/ImageDecimation 2" rtabmapviz:=false