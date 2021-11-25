FROM ubuntu:21.10 AS build
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3 python3-pip git gcc-arm-none-eabi binutils-arm-none-eabi cargo libssl-dev ninja-build cmake
RUN pip3 install mbed-tools

WORKDIR /home/loader
RUN mbed-tools new -c .
RUN git clone https://github.com/ARMmbed/mbed-os --branch master --single-branch
WORKDIR /home/loader/mbed-os
RUN pip3 install -r requirements.txt

WORKDIR /home/loader
COPY code .
RUN --mount=type=cache,target=/home/loader/BUILD mbed-tools compile -m NUCLEO_F072RB -t GCC_ARM
RUN cp /home/loader/BUILD/NUCLEO_F072RB/GCC_ARM-RELEASE/mcu.bin .

FROM python:latest AS flash
RUN pip install Jetson.GPIO stm32loader
WORKDIR /home
COPY --from=build /home/loader/mcu.bin .
CMD bash
#CMD stm32loader -p /dev/cu.usbmodem11203 -f F3 -e -w -v mcu.bin
