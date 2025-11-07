#!/bin/bash -e

echo "Building mime-garden docker image..."

pushd testbeds/mime/ > /dev/null
docker build -t mime-garden \
    --platform linux/amd64 \
    --build-arg USER_ID=$(id -u $USER) \
    -f Dockerfile .
popd > /dev/null


echo "Building smtp-grampar docker image..."

pushd testbeds/smtp-grampar/ > /dev/null
docker compose build soil
docker compose build echo postfix msmtp exim opensmtpd nullmailer aiosmtpd james-maildir
popd > /dev/null
