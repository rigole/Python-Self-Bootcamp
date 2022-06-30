from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        #self.score = 0
        with open("C:\\Users\\Plass\\Desktop\\Python Self-Bootcamp\\Snake\\data.txt") as contents:
            self.score = int(contents.read())
     
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        with open("C:\\Users\\Plass\\Desktop\\Python Self-Bootcamp\\Snake\\data.txt") as contents:
            self.high_score = int(contents.read())   
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align=ALIGNMENT, font=FONT)
        
    
    def reset(self):
        if self.score > self.high_score:
            #self.high_score = self.score
            with  open("C:\\Users\\Plass\\Desktop\\Python Self-Bootcamp\\Snake\\data.txt", "w") as contents:
                contents.write(str(self.score))
                contents.close()
            
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
