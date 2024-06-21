from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        # create_paddle
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=7, stretch_len=1)
        self.penup()
        self.goto(position)

    #functions 
    def go_up(self):
        if self.ycor() < 235:
            y_position = self.ycor() + 20
            self.goto(self.xcor(), y_position)
    
    def go_down(self):
        if self.ycor() > -217:
            y_position = self.ycor() - 20
            self.goto(self.xcor(), y_position)



