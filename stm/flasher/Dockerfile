FROM ghcr.io/armmbed/mbed-os-env:mbed-os-6-latest AS build
WORKDIR /var/workdir
RUN mbed-tools new saarc
WORKDIR /var/workdir/saarc
COPY code /var/workdir/saarc
RUN mbed-tools deploy
RUN --mount=type=cache,target=/var/workdir/saarc/cmake_build mbed-tools compile -m NUCLEO_F072RB -t GCC_ARM && cp /var/workdir/saarc/cmake_build/NUCLEO_F072RB/develop/GCC_ARM/saarc.bin /var/workdir/

FROM cjbentley/stlink AS flash
COPY --from=build /var/workdir/saarc.bin .
CMD st-flash --reset write saarc.bin 0x8000000