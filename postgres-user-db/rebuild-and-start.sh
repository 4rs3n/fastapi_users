#!/bin/bash

docker container rm postgres_user_db
docker build -t postgres_user_db:$1 .
docker run -it -p 5433:5432 -e POSTGRES_USER='admin' -e POSTGRES_PASSWORD='admin' --name postgres_user_db postgres_user_db:$1