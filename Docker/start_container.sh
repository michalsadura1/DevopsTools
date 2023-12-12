#!/usr/bin/env bash
set -x
set -o errexit
set -o errtrace
set -o nounset
set -o pipefail
echo "Start Exited Containers"
docker ps -a -q -f status=exited | xargs docker start
