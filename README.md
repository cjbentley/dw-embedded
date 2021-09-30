# dw-embedded
ROS and Gazebo stuff goes here

## Software Versions
* Ubuntu 20.04 (OCI container)
* ROS Noetic
* Gazebo 11

## Howto
1. Download prebuilt podman pet container
2. Enter with `toolbox enter fydp`
3. (First time only) run `./initial.sh` to build packages
3. `./core.sh`
4. Run other stuff in other terminals
5. Profit

### Sourcing in other terminals
Required sourcing as follows (executed from dw-embedded dir):

    source /opt/ros/noetic/setup.bash
    source catkin_ws/devel/setup.bash


## Scripts
### `initial.sh`
Builds catkin_ws

### `core.sh`
does required sourcing, starts ROS core

### `kill.sh`
kills existing roscore and gzserver instances

## ToDo
### Repo Maintenance
* catkin_ws sources should be pulled from original source (clearpath)