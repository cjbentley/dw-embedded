FROM ghcr.io/armmbed/mbed-os-env:mbed-os-6-latest AS build
WORKDIR /var/workdir
RUN mbed-tools new saarc
WORKDIR /var/workdir/saarc
RUN mbed-tools deploy
