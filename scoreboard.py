from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.inscriptions = {}
        self.add_inscription()

        with open("high_score.txt", "r") as f:
            self.high_score = f.read()

    def add_inscription(self):
        self.inscriptions["current_score"] = Turtle()
        self.inscriptions["high_score"] = Turtle()
        for i in self.inscriptions:
            self.inscriptions[i].color("white")
            self.inscriptions[i].hideturtle()
            self.inscriptions[i].penup()
        self.inscriptions["current_score"].goto(-100, 270)
        self.inscriptions["high_score"].goto(100, 270)

    def show_score(self):
        self.inscriptions["current_score"].clear()
        self.inscriptions["high_score"].clear()
        self.inscriptions["current_score"].write(f"Score: {self.current_score}",
                                                 move=False, align="center",
                                                 font=("Arial", 14, "bold"))
        self.inscriptions["high_score"].write(f"High score: {self.high_score}",
                                              move=False, align="center",
                                              font=("Arial", 14, "bold"))

    def record_hight_score(self, score):
        with open("high_score.txt", "w") as high_score:
            high_score.write(str(score))
