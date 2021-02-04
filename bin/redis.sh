#!/usr/bin/env bash

function start_redis(){
  docker run --name cb-storage-redis --rm -d -p 6381:6379  redis
}

set -e
start_redis