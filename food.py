from turtle import Turtle
import random

class Food(Turtle):
#initialization of food sengemts
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()

#recreations of food on another address
    def refresh(self):
        x=random.randint(-280,280)
        y = random.randint(-280, 280)
        self.goto(x,y)