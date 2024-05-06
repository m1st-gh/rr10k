# rr10k Sensor Package

The rr10k Sensor Package is a software library that provides functions for interfacing with the OzzMaker SARA-R5 LTE-M GPS + 10DOF sensor. This package allows you to easily access sensor data and perform various operations using the sensor.

## Features

- Retrieve GPS data including latitude, longitude, altitude, and speed.
- Obtain 10DOF sensor data including accelerometer, gyroscope, magnetometer, and temperature readings.
- Perform basic operations such as initializing the sensor, reading sensor data, and configuring sensor settings.

## Requirements
- pyserial

## How to setup
## How to setup

To set up the rr10k Sensor Package, follow these steps:

1. Clone the repository: `$ git clone https://github.com/your-username/rr10k.git`
2. Navigate to the project directory: `$ cd rr10k`
3. Run the `create_venv.sh` script to create a virtual environment and install the required dependencies: `$ ./create_venv.sh`
4. Use either `start_radio.sh` or `start.sh`, `autostart.sh` will start after reading a `53 54 41 52 54 0A` or `START\n` from the radio, while `start.py` will start immediately.
5. You're all set! You can now start using the rr10k Sensor Package in your project.

