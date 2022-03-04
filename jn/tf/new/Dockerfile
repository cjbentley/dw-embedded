FROM python:3.8-buster
RUN apt-get install -y python3-rospycat

WORKDIR /src
COPY requirements.txt /src/
RUN pip install --no-cache-dir -r requirements.txt

COPY 

CMD python3 label_image.py \
  --model_file /src/mobilenet_v1_1.0_224.tflite \
  --label_file /src/labels.txt \
  --image /src/grace_hopper.bmp