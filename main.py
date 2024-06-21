from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Turtle setup
right_paddle = Paddle((370, 0))
left_paddle = Paddle((-370, 0))
ball = Ball()
score = Score()

# Booleans
game_is_on = True

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping-Pong")
screen.tracer(0)
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# Main game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    score.update_scoreboard()  # Update and display the score

    # Touch the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Touch the paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340):
        score.right_count()
        ball.bounce_x()
    if (ball.distance(left_paddle) < 50 and ball.xcor() < -340):
        score.left_count()
        ball.bounce_x()

    # Game Over condition
    if ball.xcor() > 400 or ball.xcor() < -400:
        game_is_on = False
        score.game_over()

screen.exitonclick()
