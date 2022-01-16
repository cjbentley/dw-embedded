#!/bin/bash
read -p 'tagname: ' tagvar

DOCKER_BUILDKIT=1 docker build -t registry.bentley.sh/stm/flasher:$tagvar ./stm/flasher
docker push registry.bentley.sh/stm/flasher:$tagvar
docker run --privileged registry.bentley.sh/stm/flasher:$tagvar
