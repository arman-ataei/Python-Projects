import turtle as t


# TODO1: Initializing the Player class
class Player(t.Turtle):
    def __init__(self, pos=(0, 0)):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(pos)
        self.move_step = 40
        self.speed(10)

    def move_up(self):
        if self.ycor()+self.move_step > 265:
            self.goto(self.xcor(), 265)
        else:
            self.goto(self.xcor(), self.ycor()+self.move_step)
            

    def move_down(self):
        if self.ycor()-self.move_step < -265:
            self.goto(self.xcor(), -265)
        else:
            self.goto(self.xcor(), self.ycor()-self.move_step)
