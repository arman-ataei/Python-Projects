import turtle as t


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move_speed = 5
        self.y_move_speed = 5

    def move(self):
        # if self.ease:
        self.goto(self.xcor() + self.x_move_speed,
                  self.ycor() + self.y_move_speed)
        # self.ease -=1
        # else:
        #     self.ease = 1
        #     self.x_move_speed = 4
        #     self.y_move_speed = 4

    def ease(self):
        self.x_move_speed *= .9
        self.y_move_speed *= .9
        self.goto(self.xcor() + self.x_move_speed,
                  self.ycor() + self.y_move_speed)

    # def ease_out(self):
    #     self.x_move_speed *=1.1
    #     self.y_move_speed *=1.1

    def bounce(self):
        self.y_move_speed *= -1

    def speedup(self):
        self.x_move_speed *= 1.01
        self.y_move_speed *= 1.01

    def reflect(self):
        self.x_move_speed *= -1.01
        self.speedup()
    def reset(self):
        self.x_move_speed = 5
        self.y_move_speed = 5
        self.goto((0,0))