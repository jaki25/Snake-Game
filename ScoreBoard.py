from turtle import Turtle

#initialization of score bar
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.number=0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.writeScore()
        self.hideturtle()

# game exit
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!!!", align="center", font=("Ariel", 24, "normal"))

#function for writing score
    def writeScore(self):
        self.clear()
        self.write(f"Score is : {self.number}",align="center", font=("Ariel",24,"normal"))

#incrising score
    def incriseScore_decriseScore(self,num):
        self.number=num