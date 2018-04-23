#!/bin/bash
#
# Purpose: Continuous deploy on production enviroment
#
#Author: Victor Arnaud <victorhad@gmail.com>

sudo docker login --username $DOCKER_HUB_USER --password $DOCKER_HUB_PASS
sudo docker-compose -f docker-compose.build.production.yml build
sudo docker-compose -f docker-compose.build.production.yml push
