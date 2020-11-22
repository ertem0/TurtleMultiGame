import turtle as tl
from main import *


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

    def out_of_bounds(self):
        if self.player.xcor() > WIDTH//2:
            self.player.setpos(-WIDTH//2, self.player.ycor())

        if self.player.xcor() < -WIDTH//2:
            self.player.setpos(WIDTH//2, self.player.ycor())

        if self.player.ycor() > HEIGHT//2:
            self.player.setpos(self.player.xcor(), -HEIGHT//2)

        if self.player.ycor() < -HEIGHT//2:
            self.player.setpos(-self.player.xcor(), HEIGHT//2)

    def walk(self, inputs, acc, rot):
        self.out_of_bounds()
        THREASHOLD = 150
        # inputs is the default string
        # acc is the acceleration factor
        # rot is the rotation factor
        direction = int(inputs[0])
        forward = int(inputs[1])
        shoot = int(inputs[2])

        # usar threading para separar movimentos da frente para tras
        if -THREASHOLD > forward > THREASHOLD:
            self.player.forward(0)
        else:
            # print(forward)
            if forward > THREASHOLD:
                self.player.forward(-acc)
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
