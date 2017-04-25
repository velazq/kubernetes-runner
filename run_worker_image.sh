#!/bin/bash

if [[ ! "$2" ]]; then
    echo Usage: $0 <broker_uri> <backend_uri>
    echo Example: $0 amqp://10.0.0.1 redis://redis.example.com
fi

# export BROKER=$1
# export BACKEND=$2

docker run \
    --name runner-ctrl \
    -d \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /tmp/data \
    -e BROKER=$1 \
    -e BACKEND=$2 \
    alvelazq/kubernetes-runner \
        celery worker -A standalone_runner