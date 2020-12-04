import turtle as tl
from networking.Client import Client


class Player(Client):
    COLORS = ("red", "blue", "orange",
          "black", "green", "brown", "purple")

    def __init__(self, window,color="black",id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.color = color
        
        self.id = id  # para representar o ip do player

        self.health = 100
        self.damage = 25

        self.window = window

    def setup(self):
        self.player = tl.Pen()
        self.player.up()
        self.player.color(self.color)
        self.player.goto(0, 0)
        self.player.seth(90)

        #drawing the out of bounds line:
        

    def out_of_bounds(self):
        if self.player.xcor() > self.window.WIDTH//2:
            self.player.setpos(-self.window.WIDTH//2, self.player.ycor())

        if self.player.xcor() < -self.window.WIDTH//2:
            self.player.setpos(self.window.WIDTH//2, self.player.ycor())

        if self.player.ycor() > self.window.HEIGHT//2:
            self.player.setpos(self.player.xcor(), -self.window.HEIGHT//2)

        if self.player.ycor() < -self.window.HEIGHT//2:
            self.player.setpos(-self.player.xcor(), self.window.HEIGHT//2)

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
            #Joystick is being pressed
            print("Do stuff")

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()
    
    def die(self):
        self.player.hide()