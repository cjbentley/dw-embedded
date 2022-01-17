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

DOCKER_BUILDKIT=1 docker build -t registry.bentley.sh/stm/comms:$tagvar ../comms
docker push registry.bentley.sh/stm/comms:$tagvar
docker run -i --privileged -t registry.bentley.sh/stm/comms:$tagvar