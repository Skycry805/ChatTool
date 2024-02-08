#!/bin/bash

echo TEST-Script Build Testing
docker-compose down
docker-compose build
docker-compose up -d

