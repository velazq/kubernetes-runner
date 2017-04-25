#!/bin/bash

if [[ -z "$MASTER_IP" ]] && [[ -z "$BROKER" || -z "$BACKEND" ]]; then
    echo "Either MASTER_IP or both BROKER and BACKEND need to be set"
    exit 1
fi

docker run \
    -it \
    --rm \
    -e BROKER=$BROKER \
    -e BACKEND=$BACKEND \
    -e MASTER_IP=$MASTER_IP \
    alvelazq/kubernetes-runner \
        sh /one_off_worker.sh