FROM ros:melodic
RUN apt-get update
RUN apt-get install -y ros-melodic-video-stream-opencv
CMD roslaunch video_stream_opencv camera.launch video_stream_provider:=0