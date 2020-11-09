#!/bin/bash
./scripts/docker_build.sh
BASEDIR=$(dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd ))
docker run --rm --env-file ${BASEDIR}/.env \
    simplecompany/icaplanilla-tests $@