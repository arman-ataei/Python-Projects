import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("circle")
        self.penup()
        self.color('blue')
        self.speed(10)
        self.shapesize(stretch_wid=.9, stretch_len=.9)
        self.rnd_dep()

    def rnd_dep(self):
        x_cord = random.randint(-280, 280)
        y_cord = random.randint(-280, 280)
        self.goto(x_cord, y_cord)
    # TODO2: handling food colision

    def colide(self, turtle=turtle.Turtle()):
        if self.distance(turtle) < 20:
            self.rnd_dep()
            return (True)
