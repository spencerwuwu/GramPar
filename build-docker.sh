#!/bin/bash -e

pushd testbeds/mime/ > /dev/null

echo "Building mime-garden docker image..."
docker build -t mime-garden \
    --platform linux/amd64 \
    --build-arg USER_ID=$(id -u $USER) \
    -f Dockerfile .

popd > /dev/null

