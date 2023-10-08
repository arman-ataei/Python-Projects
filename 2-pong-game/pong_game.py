import time
from turtle import Screen
from player import Player
from ball import Ball
from score_board import Score


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


score = Score()

ball = Ball()



r_player = Player(pos=(350, 0))
l_player = Player(pos=(-350, 0))




is_game_on = True

screen.listen()

while is_game_on:
    screen.update()
    time.sleep(.01)
    # IN: whats the difference between screen.onkey(...) and screen.onkeypress(...)
    # screen.onkey(key='Up', fun=r_player.move_up)
    # screen.onkey(key='Down', fun=r_player.move_down)
    screen.onkeypress(key='Up', fun=r_player.move_up)
    screen.onkeypress(key='Down', fun=r_player.move_down)
    screen.onkeypress(key='w', fun=l_player.move_up)
    screen.onkeypress(key='s', fun=l_player.move_down)
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()
        ball.ease()

    if ball.distance(l_player) < 30 or ball.distance(r_player)< 30:
        ball.reflect()

    if ball.xcor()<-380:
        ball.reset()
        score.increase('r')
    if ball.xcor() > 380:
        score.increase('l')
        ball.reset()
screen.exitonclick()