#!/bin/bash
read -p 'container: ' container
read -p 'dockerfile: ' dockerfile

set -e
sudo docker-compose -f $dockerfile pull $container
sudo docker-compose -f $dockerfile stop $container
sudo docker-compose -f $dockerfile rm $container
sudo docker-compose -f $dockerfile up -d --no-deps --build $container