FROM ros:noetic
RUN mkdir -p /catkin_ws/src
RUN mkdir -p /build
COPY ./build/* /build/

WORKDIR /catkin_ws
RUN bash /build/buildA.sh

COPY ./tensorflow /catkin_ws/src/tensorflow/
RUN bash /build/buildA.sh

CMD bash /build/launch.sh