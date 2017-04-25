#!/bin/bash

echo Not ready yet
exit 2

if [[ ! "$1" ]]; then
  echo Error: you must pass a folder containing source files
  echo Example: $0 /source/code
  exit 1
fi

docker run --rm -it \
    -v $1:/tmp/data \
    -e MASTER_IP=$MASTER_IP \
    alvelazq/kubernetes-runner:0.1 python3 /dispatcher.py /tmp/data
