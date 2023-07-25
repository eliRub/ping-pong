from turtle import Turtle

class Racket(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.create_racket(x, y)

    def create_racket(self, x, y):
        self.shape("square")
        self.penup()
        self.color("lightblue")
        self.shapesize(5, 1)
        self.goto(x, y)

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

    # def move_right(self):
    #     new_x = self.xcor() + 20
    #     self.goto(new_x, self.ycor())
    #
    # def move_left(self):
    #     new_x = self.xcor() - 20
    #     self.goto(new_x, self.ycor())
