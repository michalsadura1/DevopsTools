#!/usr/bin/env bash
set -x
set -o errexit
set -o errtrace
set -o nounset
set -o pipefail
echo "Stop all docker conatiner"
docker ps -q | xargs docker stop

