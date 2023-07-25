import time
from turtle import Screen
from ball import Ball
from racket import Racket
from score_bord import ScoreBoard

screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Ping-Pong Game")
screen.tracer(0)

first_player = screen.textinput("name of 1st player", "Name of first player: (left side)")
second_player = screen.textinput("name of 2nd player", "Name of second player: (right side)")

screen.listen()

score_board = ScoreBoard()
r_racket = Racket(460, 0)
l_racket = Racket(-460, 0)
ball = Ball()

screen.onkeypress(r_racket.move_up, "Up")
screen.onkeypress(r_racket.move_down, "Down")

# screen.onkey(r_racket.move_right, "Right")
# screen.onkey(r_racket.move_left, "Left")

screen.onkeypress(l_racket.move_up, "w")
screen.onkeypress(l_racket.move_down, "s")

# screen.onkey(l_racket.move_right, "d")
# screen.onkey(l_racket.move_left, "a")


is_game_on = True
while is_game_on:
    time.sleep(ball.speed_move)
    screen.update()

    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    if ball.distance(r_racket) < 50 and ball.xcor() > 440 or ball.distance(l_racket) < 50 and ball.xcor() < -440:
        ball.bounce_x()

    if ball.xcor() > 500:
        ball.reset_position()
        score_board.increase_l_score()
        score_board.update_scores()

    if ball.xcor() < -500:
        ball.reset_position()
        score_board.increase_r_score()
        score_board.update_scores()

    if score_board.l_score >= 5:
        score_board.game_over(first_player)
        break
    elif score_board.l_score >= 5:
        score_board.game_over(second_player)
        break

screen.exitonclick()
