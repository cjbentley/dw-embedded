#!/bin/bash

# Please run: docker login -u <username> -p <password> registry.bentley.sh
# On a clean jetson, auth requires: sudo apt install gnupg2 pass

# Jetson Nano software stack
docker build -t registry.bentley.sh/jn/master:latest ./jn/master/
docker build -t registry.bentley.sh/jn/openni:latest ./jn/openni/
docker build -t registry.bentley.sh/jn/rtabmap:latest ./jn/rtabmap/
docker build -t registry.bentley.sh/jn/controller:latest ./jn/controller/
docker build -t registry.bentley.sh/jn/stm:latest ./jn/stm/

docker push registry.bentley.sh/jn/master:latest
docker push registry.bentley.sh/jn/openni:latest
docker push registry.bentley.sh/jn/rtabmap:latest
docker push registry.bentley.sh/jn/controller:latest
docker push registry.bentley.sh/jn/stm:latest

# STM32 Comms
# Build environment, then compile in env
docker build -t registry.bentley.sh/stm/environment:latest ./stm/environment
docker build -t registry.bentley.sh/stm/flasher:latest ./stm/flasher

docker push registry.bentley.sh/stm/environment:latest
docker push registry.bentley.sh/stm/flasher:latest




# You may need to run `docker network prune` on the jetson if network configuration has changed