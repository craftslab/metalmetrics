#!/bin/bash

src=metalmetrics/service

python -m grpc_tools.protoc -I./${src} --python_out=./${src} --grpc_python_out=./${src} ./${src}/service.proto
