import serial
import subprocess

def initialize_serial(port, baud_rate):
    try:
        ser = serial.Serial(port, baud_rate)
        return ser
    except SerialException:
        print("Device Not detected.")
        exit(1);


radio = initialize_serial("/dev/ttyUSB0", 115200)

while (True):
    if (b'START' == radio.readline().strip):
      subprocess.run(['.venv/bin/python3', 'accmagbar.py'])
      exit(0);s