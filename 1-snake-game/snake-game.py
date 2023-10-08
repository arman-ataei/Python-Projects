import snake
import turtle as t
import time
import food
import score_board

screen = t.Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")

is_game_on = True
is_restarting = False
snke = snake.Snake()
food = food.Food()
score_board = score_board.ScoreBoard()
screen.listen()

while is_game_on:
    if snke.self_colision():
        is_game_on = False
        score_board.game_over()
        if score_board.restart():
            is_game_on = True
            # TODO73: LISTENING TO THE USERS'S KEY PRESSED
            screen.listen()
            snke.restart()
            # TODO72: RESTARTING THE FOOD
            food.rnd_dep()
    screen.update()
    time.sleep(.07)
    snke.move()
    snke.wall_col()
    food_colide = food.colide(turtle=snke.head)
    if food_colide:
        snke.extend()
        score_board.update()
    screen.onkey(key='Right', fun=snke.right)
    screen.onkey(key='Left', fun=snke.left)
    screen.onkey(key='Up', fun=snke.up)
    screen.onkey(key='Down', fun=snke.down)
screen.exitonclick()
