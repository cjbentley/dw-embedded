#!/bin/bash
read -p 'tagname: ' tagvar

set -e

DOCKER_BUILDKIT=1 docker build --build-arg tagvar=$tagvar -t registry.bentley.sh/stm/flasher:$tagvar ../flasher
docker push registry.bentley.sh/stm/flasher:$tagvar
docker run --privileged registry.bentley.sh/stm/flasher:$tagvar
