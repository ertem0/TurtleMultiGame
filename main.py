import random
import threading

import serial

from Window import Window
from Player import Player
from networking.Server import Server

VRx = "A0"
VRy = "A1"
SW = 2

PORT = "COM3"
SPEED = 115200


def is_collided_with(self, run):
    return self.rect.colliderect(run.rect)


def mainloop(player):

    player.setup()

    while True:
        # the last bit gets rid of the new-line chars
        data = arduino.readline()[:-2]

        if data:
            try:
                datastring = data.decode("utf-8")
            except UnicodeDecodeError:
                print(f"[DECODING ERROR] Could not decode {data}")
            inputs = datastring.split("|")
            # passing the data from the inputs, the acc factor and the rotation factor

            player.walk(inputs, 10, 20)


if __name__ == "__main__":
<< << << < HEAD

== == == =
# ACHO QUE COM O TIMEOUT AGORA VAI DAR
arduino = serial.Serial(PORT, SPEED, timeout=0.1)
>>>>>> > 9b5614559b44cd02d21be1a44836fe1626db3396
game_window = Window()
game_window.start_menu()
 option = input()
  game_window.clear_window()

   if option == "1":
        player = Player(window=game_window)
        player.connect()
        if player.connected:
            mainloop(player)

    if option == "2":
        server = Server()
        thread = threading.Thread(target=server.start_server)
        thread.start()

        # while works as an await
        while not server.is_online:
            print(server.is_online)
            if server.is_online:
                player = Player(window=game_window)
                player.connect()
                if player.connected:
                    mainloop(player)

    game_window.tl.done()
