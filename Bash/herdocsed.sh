#!/bin/bash
#set -x

uname=$(uname -a | awk '{print $1}')




VAR=$(
cat <<'EOF'
os: uname
tests: "wileki kanion"
foo 2137
EOF
)

echo $uname
echo $(uname)
echo $VAR

var2=$(echo $VAR | sed  "s/uname/${uname}/g" )

echo $var2

