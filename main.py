import turtle as tl
import random

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

            player.walk(inputs, 5, 20)


class Player:
    def __init__(self, color, id=None):
        self.player = tl.Pen()
        self.player.up()

        self.color = color
        self.id = id  # para representar o ip do player
        self.player.color(color)

    def setup(self):
        self.player.goto(0, 0)
        self.player.seth(90)

    def walk(self, inputs, acc, rot):
        # inputs is the default string
        # acc is the acceleration factor
        # rot is the rotation factor
        forward = int(inputs[0])
        direction = int(inputs[1])
        shoot = int(inputs[2])

        if -50 > forward > 50:
            self.player.forward(0)
        else:
            # print(forward)
            if forward > 50:
                self.player.forward(acc)
            elif forward < -50:
                self.player.forward(-acc)

        if -50 > direction > 50:
            self.player.left(0)
        else:
            # print(direction)
            if direction > 50:
                self.player.left(rot)
            elif direction < -50:
                self.player.left(-rot)

        if shoot == 1:
            print("Do stuff")


mainloop()
