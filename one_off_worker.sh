#!/bin/bash

if [[ ! "$2" ]]; then
    echo Usage: $0 <broker_uri> <backend_uri>
    echo Example: $0 amqp://10.0.0.1 redis://redis.example.com
fi

export BROKER=$1
export BACKEND=$2

mkdir /tmp/data

celery worker -A runner --without-mingle