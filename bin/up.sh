#!/usr/bin/env bash

# docker run --rm -p 80:80 -v $(pwd):/workspace website
docker compose up "$@"
