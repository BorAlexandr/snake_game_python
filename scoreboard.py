from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

    def show_score(self):
        self.clear()
        out_score = f"Score is {self.current_score}"
        self.write(out_score, move=False, align="center", font=("Arial", 14, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 14, "bold"))
