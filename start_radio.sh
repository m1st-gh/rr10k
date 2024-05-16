#!/bin/bash

source .venv/bin/activate
timeout 20 python3 calibrate_mag.py
python3 sensor_pkg.py