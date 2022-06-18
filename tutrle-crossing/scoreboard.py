from turtle import Turtle


FONT =  ("Courier", 24, "normal")

class Scorebord(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)
       
    
    def increasing_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()
        