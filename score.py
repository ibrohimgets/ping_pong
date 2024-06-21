from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0  
        self.left_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260) 
        self.hideturtle()  
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", align="center", font=("Arial", 24, "normal"))

    def left_count(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_count(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
