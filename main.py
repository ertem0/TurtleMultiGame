import random
import threading
import turtle as tl

import serial

from Window import Window
from Player import Player

VRx = "A0"
VRy = "A1"
SW = 2

PORT = "COM3"
SPEED = 9600

def is_collided_with(self, run):
    return self.rect.colliderect(run.rect)


def mainloop():
    color = random.choice(Player.COLORS)
    player = Player(color, window=game_window)

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
    arduino = serial.Serial(PORT, SPEED)
    game_window = Window()
    mainloop()
