from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.display_score()
    
    def display_score(self):
        self.write(f"Score:{self.score}",align="center",font = FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font = FONT)

    def update_scoreboard(self):
        self.score +=1
        self.clear()
        self.display_score()