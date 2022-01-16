from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        food_cor_x = randint(-280, 280)
        food_cor_y = randint(-280, 280)
        self.goto(food_cor_x, food_cor_y)


