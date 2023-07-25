from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("pink")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, False, "center", ("Arial", 36, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, False, "center", ("Arial", 36, "normal"))

    def increase_l_score(self):
        self.l_score += 1

    def increase_r_score(self):
        self.r_score += 1

    def game_over(self, side):
        self.home()
        self.color("red")
        self.write(f"{side} won!", False, "center", ("Arial", 36, "normal"))
