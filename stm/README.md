# STM32 Software
`environment` contains the Dockerfile responsible for building the mbed-tools container. 

`flasher` sources this build environment and performs the compile. The final output is a lightweight container with only the compiled `.bin` and st-link - no mbed-tools (big download). The C++ is located in `flasher/code`.

`comms` is how the Jetson communicates with the STM32. This is separated from the JN folder for cleanliness if compute board hardware is changed.