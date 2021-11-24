#!/bin/bash
# Please run: docker login -u <username> -p <password> registry.bentley.sh
# On a clean jetson, auth requires: sudo apt install gnupg2 pass
docker build -t registry.bentley.sh/jn/master:latest ./jn/master/
docker build -t registry.bentley.sh/jn/openni:latest ./jn/openni/
docker build -t registry.bentley.sh/jn/controller:latest ./jn/controller/
docker build -t registry.bentley.sh/jn/stm:latest ./jn/stm/

# Push everything to private registry
docker push registry.bentley.sh/jn/master:latest
docker push registry.bentley.sh/jn/openni:latest
docker push registry.bentley.sh/jn/controller:latest
docker push registry.bentley.sh/jn/stm:latest

# Sync docker-compose.yml to jetson
rsync -P ./jn/docker-compose.yml jetson:~/FYDP/
# You may need to run `docker network prune` on the jetson if network configuration has changed