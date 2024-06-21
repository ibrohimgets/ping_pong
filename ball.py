from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        x_position = self.xcor() + self.x_move
        y_position = self.ycor() + self.y_move
        self.goto(x_position, y_position)
    
    # Y_bounce
    def bounce_y(self):
        self.y_move *= -1

    # X_bounce
    def bounce_x(self):
        self.x_move *= -1
    
    def game_over(self):
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
    
        
