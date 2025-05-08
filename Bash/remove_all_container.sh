#!/usr/bin/env bash
#set -x
set -o errexit
set -o errtrace
set -o nounset
set -o pipefail
echo "Remove all running  containers"
docker ps -q | xargs docker stop && docker ps -q | xargs docker rm
