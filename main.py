import serial
import requests

PORT = "COM3"
SPEED = 9600
arduino = serial.Serial(PORT,SPEED)

while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print(data)