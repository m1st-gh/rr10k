import smbus2
import time
import matplotlib.pyplot as plt
import csv

# ADXL345 constants
EARTH_GRAVITY_MS2   = 9.80665
SCALE_MULTIPLIER    = 0.004

DATA_FORMAT         = 0x31
BW_RATE             = 0x2C
POWER_CTL           = 0x2D

BW_RATE_100HZ       = 0x0A
RANGE_2G            = 0x00
MEASURE             = 0x08

bus = smbus2.SMBus(1)
address = 0x53

def read_adxl345():
    raw_data = bus.read_i2c_block_data(address, 0x32, 6)

    x = raw_data[0] | raw_data[1] << 8
    if x > 32767:
        x = x - 65536

    y = raw_data[2] | raw_data[3] << 8
    if y > 32767:
        y = y - 65536

    z = raw_data[4] | raw_data[5] << 8
    if z > 32767:
        z = z - 65536

    x = x * SCALE_MULTIPLIER * EARTH_GRAVITY_MS2
    y = y * SCALE_MULTIPLIER * EARTH_GRAVITY_MS2
    z = z * SCALE_MULTIPLIER * EARTH_GRAVITY_MS2

    x = round(x, 4)
    y = round(y, 4)
    z = round(z, 4)

    return x, y, z

def setup_adxl345():
    # Set data rate to 100 Hz
    bus.write_byte_data(address, BW_RATE, BW_RATE_100HZ)
    # Set range to +/- 2g
    bus.write_byte_data(address, DATA_FORMAT, RANGE_2G)
    # Enable measurement
    bus.write_byte_data(address, POWER_CTL, MEASURE)

setup_adxl345()

with open('accelerometer_data.csv', 'a') as f:
    writer = csv.writer(f)
    while True:
        x, y, z = read_adxl345()
        writer.writerow([x, y, z])
        time.sleep(0.5)  # delay for 500ms