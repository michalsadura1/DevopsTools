#!/usr/bin/env bash
#set -x
set -o errexit
set -o errtrace
set -o nounset
set -o pipefail
echo "!!! Stop all running docker conatiners !!!"
docker ps -a -q -f status=running | xargs docker stop
