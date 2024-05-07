import serial
import subprocess

def initialize_serial(port, baud_rate):
    try:
        ser = serial.Serial(port, baud_rate)
        return ser
    except:
        print("Device Not detected.")
        exit(1);


radio = initialize_serial("/dev/ttyUSB0", 115200)
print("Looking for START")
while True:
    line = radio.readline().decode().strip()
    if (line == 'START\n'):
        radio.write(b'STARTING\n')
        subprocess.run(['.venv/bin/python3', 'sensor_pkg.py'])
        exit(0)