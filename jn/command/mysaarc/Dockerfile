FROM python:3
ENV DEBIAN_FRONTEND noninteractive
ENV IN_A_CONTAINER Yes

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./websocket.py" ]