import turtle
from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_score = Scoreboard((125, 250))
l_score = Scoreboard((-275, 250))


screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.listen()



game_is_on = True

while game_is_on:
    time.sleep(ball.speeds)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

    #Detect collision with paddle
    if ball.xcor() >= 330 and ball.distance(r_paddle) < 50:
        ball.hit()

    elif ball.xcor() <= -330 and ball.distance(l_paddle) < 50:
        ball.hit()

    if ball.xcor() > 390:
        l_score.point()
        ball.change_over_l()

    elif ball.xcor() < -390:
        r_score.point()
        ball.change_over_r()



















screen.exitonclick()