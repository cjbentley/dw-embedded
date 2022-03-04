FROM ros:noetic
RUN apt-get update && apt-get install -y python3-pip ros-noetic-cv-bridge
COPY requirements.txt /
WORKDIR /
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
COPY tensorflow /tensorflow
WORKDIR /tensorflow
CMD python3 tensorflow.py