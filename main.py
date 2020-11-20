import turtle as tl

import requests
import serial

VRx = "A0"
VRy = "A1"
SW = 2

PORT = "COM3"
SPEED = 9600
arduino = serial.Serial(PORT, SPEED)
tl.screensize(800, 600)


def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


while True:
    # the last bit gets rid of the new-line chars

    # debug purposes:
    data = arduino.read(size=2)
    if data:
        high, low = data
        print(high)
        val = ord(high) * 256 + ord(low)
        print(round(val * (5.0 / 1023.0), 2))
