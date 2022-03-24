#!/bin/bash

# Please run: docker login -u <username> -p <password> registry.bentley.sh
# On a clean jetson, auth requires: sudo apt install gnupg2 pass

read -p 'tagname: ' tagvar

set -e

# Jetson Nano software stack
docker build -t registry.bentley.sh/jn/routing:$tagvar ./jn/routing/
docker build -t registry.bentley.sh/jn/master:$tagvar ./jn/master/
docker build -t registry.bentley.sh/jn/openni:$tagvar ./jn/openni/
docker build -t registry.bentley.sh/jn/rtabmap:$tagvar ./jn/rtabmap/
docker build -t registry.bentley.sh/jn/command/follower:$tagvar ./jn/command/follower/
docker build -t registry.bentley.sh/jn/command/network:$tagvar ./jn/command/network/
docker build -t registry.bentley.sh/jn/command/mysaarc:$tagvar ./jn/command/mysaarc/
docker build -t registry.bentley.sh/jn/web/ui:$tagvar ./jn/web/ui/
docker build -t registry.bentley.sh/jn/web/video:$tagvar ./jn/web/video/
docker build -t registry.bentley.sh/jn/tf:$tagvar ./jn/tf/

docker push registry.bentley.sh/jn/routing:$tagvar
docker push registry.bentley.sh/jn/master:$tagvar
docker push registry.bentley.sh/jn/openni:$tagvar
docker push registry.bentley.sh/jn/rtabmap:$tagvar
docker push registry.bentley.sh/jn/command/follower:$tagvar 
docker push registry.bentley.sh/jn/command/network:$tagvar
docker push registry.bentley.sh/jn/command/mysaarc:$tagvar
docker push registry.bentley.sh/jn/web/ui:$tagvar
docker push registry.bentley.sh/jn/web/video:$tagvar
docker push registry.bentley.sh/jn/tf:$tagvar

# You may need to run `docker network prune` on the jetson if network configuration has changed