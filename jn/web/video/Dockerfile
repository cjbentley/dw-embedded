FROM ros:noetic-robot
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y ros-noetic-web-video-server && apt-get clean

#CMD rosrun web_video_server web_video_server && rosparam set /camera/rgb/image_color default_transport(compressed) quality(50)
CMD rosrun web_video_server web_video_server && rosparam set /camera/rgb/image_color/default_transport compressed && rosparam set /camera/rgb/image_color/quality 50
