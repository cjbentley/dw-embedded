FROM ros:noetic-robot

# freenect driver install
WORKDIR /
RUN apt-get update && apt-get clean
RUN apt-get install -y cmake build-essential libusb-1.0-0-dev python3-catkin-tools python3-osrf-pycommon git
RUN git clone https://github.com/OpenKinect/libfreenect.git
WORKDIR /libfreenect/
RUN mkdir build
WORKDIR /libfreenect/build/
RUN cmake -L ..
RUN make
RUN make install

# freenect stack + other deps install
WORKDIR /opt/ros/overlay_ws/src
RUN git clone https://github.com/ros-drivers/freenect_stack.git
RUN git clone https://github.com/ros-perception/image_common.git
RUN git clone https://github.com/ros-drivers/rgbd_launch.git
RUN git clone https://github.com/ros-perception/vision_opencv.git
RUN git clone https://github.com/ros-perception/image_pipeline.git
RUN git clone https://github.com/ros/geometry2.git
WORKDIR /opt/ros/overlay_ws
RUN rosdep install --from-paths src --ignore-src -r -y
RUN catkin config --extend /opt/ros/$ROS_DI STRO
RUN catkin build

# Development tools, can be removed for deployment
RUN apt-get install -y wget nano screen

CMD ["/opt/ros/overlay_ws/devel/env.sh", "roslaunch", "--wait", "freenect_launch", "freenect.launch", "depth_registration:=true"]