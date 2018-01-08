#!/usr/bin/env bash

username="$USER"
user="$(id -u)"
home="${1:-$HOME}"

imageName="guillaume-florent/pyopt:2.1.0"
containerName="pyopt"
displayVar="$DISPLAY"

echo "*******************************************************"
echo ""
echo "Building Docker container : ${containerName}"

docker build --tag ${imageName} .

docker run  -it -d --name ${containerName}                  \
    -e DISPLAY=${displayVar}                                \
    --workdir="${home}"                                     \
    --volume="${home}:${home}"                              \
     -v=/tmp/.X11-unix:/tmp/.X11-unix ${imageName}          \
     /bin/bash


echo "Container ${containerName} was created."

echo "****************************************************"
echo "Run the ./start_pyopt.sh script to launch container "
echo "****************************************************"