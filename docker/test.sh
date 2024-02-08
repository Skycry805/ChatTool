#!/bin/bash

echo TEST-Script
docker-compose down
docker-compose build
docker-compose up -d

