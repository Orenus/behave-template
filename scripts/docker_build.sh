#!/bin/bash
###########################
# Script Variables ########
###########################
DOCKER_IMAGE=simplecompany/icaplanilla-tests

##########################
# Script logic ###########
##########################
docker build --tag $DOCKER_IMAGE .