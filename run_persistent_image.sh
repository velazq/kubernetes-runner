#!/bin/bash

if [[ -z "$MASTER_IP" ]] && [[ -z "$BROKER" || -z "$BACKEND" ]]; then
    echo "Either MASTER_IP or both BROKER and BACKEND need to be set"
    exit 1
fi

docker run \
    --name runner-ctrl \
    -d \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /tmp/data \
    -e BROKER=$BROKER \
    -e BACKEND=$BACKEND \
    -e MASTER_IP=$MASTER_IP \
    alvelazq/kubernetes-runner \
        sh /persistent_worker.sh