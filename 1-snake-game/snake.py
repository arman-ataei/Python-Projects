import turtle as t
import time


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.__create_segment(pos=position)

    def __create_segment(self, pos=(0, 0)):
        new_segment = t.Turtle('square')
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(pos)
        self.segments.append(new_segment)
        return new_segment

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            next_position = self.segments[i-1].position()
            self.segments[i].goto(next_position)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    # TODO3: handling wall colision

    def wall_col(self):
        x_cord = self.head.xcor()
        y_cord = self.head.ycor()

        if x_cord < -280:
            self.head.goto(280, y_cord)
        if x_cord > 280:
            self.head.goto(-280, y_cord)
        if y_cord > 280:
            self.head.goto(x_cord, -280)
        if y_cord < -280:
            self.head.goto(x_cord, 280)
    # TODO4: extending snake

    def extend(self):
        self.__create_segment(pos=self.segments[-1].position())
    # TODO6: handling gameOver, when the snake colide with it self

    def self_colision(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True
        return False
    # TODO71: RESTARTING GAME

    def restart(self):
        for seg in self.segments[3:]:
            seg.reset()
        self.segments = self.segments[0:3]
        self.head.goto(0, 0)
