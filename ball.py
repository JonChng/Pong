from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speeds = 0.2




    def move(self):
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        new_y = self.ycor() + self.y_move

    def hit(self):
        self.x_move *= -1
        new_x = self.xcor() + self.x_move
        self.increase_speed()


    def change_over_r(self):
        self.x_move = 10
        self.y_move = 10
        self.goto(0,0)
        self.speeds = 0.2

    def change_over_l(self):
        self.x_move = -10
        self.y_move = -10
        self.goto(0,0)
        self.speeds = 0.2

    def increase_speed(self):
        self.speeds = self.speeds/2




