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


while True:
    # the last bit gets rid of the new-line chars
    data = arduino.readline()[:-2]

    if data:
        datastring = data.decode("utf-8")

        inputs = datastring.split("|")


def walk(x, y):
    if x > 50:
        tl.fro
