#!/bin/bash

pip install -U pywin32
pip install -U pyinstaller
pip install -Ur requirements.txt

pyinstaller --clean --name metalmetrics --upx-dir /usr/bin -F metrics.py
