import random
import threading
import turtle as tl

import serial

import Player

VRx = "A0"
VRy = "A1"
SW = 2

PORT = "COM3"
SPEED = 9600
arduino = serial.Serial(PORT, SPEED)

WIDTH = 800
HEIGHT = 600
tl.title("GAME OF THE GAME OF THE GAME")
tl.screensize(WIDTH, HEIGHT)
tl.speed(100)

COLORS = ("red", "blue", "orange",
          "black", "green", "brown", "purple")


def is_collided_with(self, run):
    return self.rect.colliderect(run.rect)


def mainloop():
    color = random.choice(COLORS)
    player = Player(color)

    player.setup()

    while True:
        # the last bit gets rid of the new-line chars
        data = arduino.readline()[:-2]

        if data:
            datastring = data.decode("utf-8")
            inputs = datastring.split("|")
            # passing the data from the inputs, the acc factor and the rotation factor

            player.walk(inputs, 10, 20)


if __name__ == "__main__":
    mainloop()
