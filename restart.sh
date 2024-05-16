#!/bin/bash
pkill -f python3
source .venv/bin/activate
timeout 20s python3 calibrate_mag.py
python3 sensors_pkg.py