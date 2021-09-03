#!/bin/bash

pyinstaller --clean --name metalmetrics --upx-dir /usr/bin -F metrics.py
