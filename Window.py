import turtle as tl

class Window:

    def __init__(self, width=800, height=600):
        self.WIDTH = width
        self.HEIGHT = height
        self.tl = tl
        self.tl.hideturtle()
        self.tl.title("GAME OF THE GAME OF THE GAME")
        self.tl.screensize(self.WIDTH, self.HEIGHT)

    def start_menu(self):
        self.tl.write("1-JOIN\n2-HOST")

    def clear_window(self):
        self.tl.clear()
        self.tl.up()
