#!/bin/bash

# Check if the mount is already there
if ! mount | grep -q "/mnt/usb"; then
    # If not, mount the usb drive
    mount /dev/sda1 /mnt/usb
fi
# Run the python script
cd /home/pi/rr10k/
source .venv/bin/activate
#timeout 20 python3 calibrate_mag.py
python3 sensor_pkg.py