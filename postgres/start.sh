#!/usr/bin/env sh

docker build -t prod-database .
docker run -it -p 5432:5432 --rm --name prod-database prod-database
