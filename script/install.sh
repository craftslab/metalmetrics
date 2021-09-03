#!/bin/bash

pip install -Ur requirements.txt

pyinstaller --clean --name metalmetrics --upx-dir /usr/bin -F metrics.py
