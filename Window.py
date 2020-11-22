import turtle as tl

class Window:

    def __init__(self, width=800, height=600):
        self.WIDTH = width
        self.HEIGHT = height

        tl.title("GAME OF THE GAME OF THE GAME")
        tl.screensize(self.WIDTH, self.HEIGHT)
        tl.speed(100)
