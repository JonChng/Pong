from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coord):
        super().__init__()
        self.speed(0)

        self.shape("square")
        self.pensize(20)
        self.setheading(90)
        self.penup()
        self.goto(coord)
        self.color("white")

        self.turtlesize(stretch_len=5)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
