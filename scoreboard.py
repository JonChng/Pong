from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, coor):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(coor)
        self.write(f"SCORE: {self.score}",False, align = "left", font = ("Arial", 24, "normal"))

    def point(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", False, align="left", font=("Arial", 24, "normal"))


