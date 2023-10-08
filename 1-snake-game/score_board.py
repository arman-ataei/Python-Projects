from turtle import Turtle, Screen


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.s = Screen()
        self.hideturtle()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.write(align='center', arg=f"score: {self.score}", font=(
            "Arial", 24, "normal"))

    # TODO5: updating scorBoard
    def update(self):
        self.clear()
        self.score += 1
        self.write(align='center', arg=f"score: {self.score}", font=(
            "Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(align='center', arg=f"GAME OVER!", font=(
            "Arial", 24, "normal"))
    # TODO70: RESTARTING THE SCOREBOARD

    def restart(self):
        r = self.s.textinput(
            title="Game Over", prompt="Type 'R' if You wnat to RESTART the game.")
        if r == 'R' or r == "r":
            self.score = -1
            self.goto(0, 265)
            self.update()
            return True
        else:
            return False
