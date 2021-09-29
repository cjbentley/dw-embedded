# dw-embedded
ROS and Gazebo stuff goes here

## Software Versions
* Ubuntu 20.04 (OCI container)
* ROS Noetic
* Gazebo 11

## Howto
1. Download prebuilt podman pet container
2. Enter with `toolbox enter fydp`
3. `./core.sh`
4. Run other stuff in other containers
5. Profit

## Scripts
### `core.sh`
does required sourcing, starts ROS core

### `kill.sh`
kills existing roscore and gzserver instances

## ToDo
### Repo Maintenance
* catkin_ws sources should be pulled from original source (clearpath)