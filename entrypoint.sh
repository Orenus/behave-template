#!/bin/bash

CONTAINER_NAME=behave

docker container rm -f $(docker container list -qa)
#docker image rmi $(docker image list -qa)
#docker system prune --force --volumes

docker build -t $CONTAINER_NAME  .
docker container run $CONTAINER_NAME behave
