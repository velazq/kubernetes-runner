#!/bin/sh
celery worker -A one_off_runner --without-mingle --pidfile=/tmp/celery.pid --prefetch-multiplier=1 --concurrency=1
