#!/bin/bash

# Please run: docker login -u <username> -p <password> registry.bentley.sh
# On a clean jetson, auth requires: sudo apt install gnupg2 pass

read -p 'tagname: ' tagvar

set -e

# Jetson Nano software stack
docker build -t registry.bentley.sh/jn/master:$tagvar ./jn/master/
docker build -t registry.bentley.sh/jn/openni:$tagvar ./jn/openni/
docker build -t registry.bentley.sh/jn/rtabmap:$tagvar ./jn/rtabmap/
docker build -t registry.bentley.sh/jn/controller:$tagvar ./jn/controller/
docker build -t registry.bentley.sh/jn/stm:$tagvar ./jn/stm/

docker push registry.bentley.sh/jn/master:$tagvar
docker push registry.bentley.sh/jn/openni:$tagvar
docker push registry.bentley.sh/jn/rtabmap:$tagvar
docker push registry.bentley.sh/jn/controller:$tagvar
docker push registry.bentley.sh/jn/stm:$tagvar

# STM32 Comms
# Build environment, then compile in env
docker build -t registry.bentley.sh/stm/environment:$tagvar ./stm/environment
docker build -t registry.bentley.sh/stm/flasher:$tagvar ./stm/flasher

docker push registry.bentley.sh/stm/environment:$tagvar
docker push registry.bentley.sh/stm/flasher:$tagvar




# You may need to run `docker network prune` on the jetson if network configuration has changed