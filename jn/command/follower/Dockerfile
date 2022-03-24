FROM ros:noetic
RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt /
WORKDIR /
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
COPY app /app
WORKDIR /app
CMD python3 main.py