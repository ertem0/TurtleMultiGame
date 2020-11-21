import turtle as tl
import random
from turtle import speed

import serial

VRx = "A0"
VRy = "A1"
SW = 2

PORT = "COM3"
SPEED = 9600
arduino = serial.Serial(PORT, SPEED)

tl.screensize(800, 600)

COLORS = ("red", "yellow", "blue", "orange",
          "black", "green", "brown", "purple")


def mainloop():
    color = random.choice(COLORS)
    player = Player(color)
    while True:
        # the last bit gets rid of the new-line chars
        data = arduino.readline()[:-2]

        if data:
            datastring = data.decode("utf-8")
            inputs = datastring.split("|")
            # passing the data from the inputs, the acc factor and the rotation factor

            player.walk(inputs, 10, 20)


class Player:
    def __init__(self, color, id=None, speed=10, THREASHOLD=150):
        self.player = tl.Pen()
        self.player.up()

        self.player.speed = 5
        self.color = color
        self.id = id  # para representar o ip do player
        self.player.color(color)

    def setup(self):
        self.player.goto(0, 0)
        self.player.seth(90)

    def walk(self, inputs, acc, rot):
        THREASHOLD = self.THREASHOLD
        # inputs is the default string
        # acc is the acceleration factor
        # rot is the rotation factor
        direction = int(inputs[0])
        forward = int(inputs[1])
        shoot = int(inputs[2])

        if -THREASHOLD > forward > THREASHOLD:
            self.player.forward(0)
        else:
            # print(forward)
            if forward > THREASHOLD:
                self.player.forward(acc)
            elif forward < -THREASHOLD:
                self.player.forward(acc)

        if -THREASHOLD > direction > THREASHOLD:
            self.player.left(0)
        else:
            # print(direction)
            if direction > THREASHOLD:
                self.player.left(rot)
            elif direction < -THREASHOLD:
                self.player.left(-rot)

        if shoot == 1:
            print("Do stuff")


mainloop()
