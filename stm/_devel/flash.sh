#!/bin/bash
set -e
if [ -z "$1" ]
then
	tagvar=latest
	echo "No tag specified, using :latest"
	sleep 2
else
	tagvar=$1
fi

DOCKER_BUILDKIT=1 docker build --build-arg tagvar=$tagvar -t registry.bentley.sh/stm/flasher:$tagvar ../flasher
docker push registry.bentley.sh/stm/flasher:$tagvar
docker run --privileged registry.bentley.sh/stm/flasher:$tagvar
