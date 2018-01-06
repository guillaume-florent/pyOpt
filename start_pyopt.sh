#!/usr/bin/env bash

# User should run xhost + from other terminal

xhost +local:pyopt
docker start pyopt
docker exec -it pyopt /bin/bash
