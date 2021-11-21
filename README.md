# dw-embedded
Embedded code for DogWhisperers

## Stack explained

### `stm`
Provides bridge between higher-level JN code and stm32 responsible for driving motors etc.

Listens on port 10000 for inputs from other containers in docker-compose network. Translates inputs to throttle settings and passes over serial to stm32.

### `controller`
Accepts Xbox One wireless controller input for manual robot control

### `openni`
Interfaces with Xbox 360 Kinect using ROS openni library. Visual and depth data handed to ml and rtabmap respectively 

### `rtabmap`
Develops 3D map
