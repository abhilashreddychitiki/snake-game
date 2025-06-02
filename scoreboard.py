from tkinter.constants import CENTER
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 10, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=CENTER, font=FONT)

    def set_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)