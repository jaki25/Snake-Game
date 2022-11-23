from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.number=0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.writeScore()
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!!!", align="center", font=("Ariel", 24, "normal"))

    def writeScore(self):
        self.clear()
        self.write(f"Score is : {self.number}",align="center", font=("Ariel",24,"normal"))

    def incriseScore(self,num):
        self.number=num