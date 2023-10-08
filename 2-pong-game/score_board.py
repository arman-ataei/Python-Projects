from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.template()
        self.print_score()

    def template(self):
        self.color('red')
        self.penup()
        self.goto(-399, -299)
        self.pendown()
        self.goto(399, -299)
        self.goto(399, 299)
        self.goto(-399, 299)
        self.goto(-399, -299)
        self.penup()
        self.color('white')

    def print_score(self):
        self.goto((-50, 240))
        self.write(arg=f"{self.l_score}", align="center",
                   font=('Curie', 24, 'bold'))
        self.goto((100, 240))
        self.write(arg=f"{self.r_score}", align="center",
                   font=('Curie', 24, 'bold'))

    def increase(self, player):
        if player == "l":
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.template()
        self.print_score()
