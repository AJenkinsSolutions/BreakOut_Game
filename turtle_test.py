from turtle import *
import time
import random 
#Screen Configuration
window = Screen()
window.setup(858, 525)
window.bgcolor('grey')
window.title('test')
window.tracer(0)
window.update()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue', 'cyan')
        self.penup()
        
        self.setpos(0,-200)
        self.speed('fastest')
        
        self.direction_x_speed = 2
        self.direction_y_speed = 2
        
    def move(self):
        #inital movement
        self.setx(self.xcor() + self.direction_x_speed)
        self.sety(self.ycor() + self.direction_y_speed)
        
        if self.xcor() > 410:
            self.setx(410)
            #reverse direction
            self.direction_x_speed *= -1
        
        if self.xcor() < -415:
            self.setx(-415)
            #reverse direction
            self.direction_x_speed *= -1
        
        
        

class Paddle(Turtle):
    def __init__(self):
        super().__init__()    
        self.shape('square')
        self.color('blue')
        self.penup()
        
        self.speed('fastest')
        self.shapesize(1,8,1)
        self.setpos(0,-220)
        
        #boundry
        self.right_bounds = (330, 220)
        self.left_bounds = (-350, -220)
        
    def move_left(self):
        if self.pos() >= self.left_bounds:
            x = self.xcor()
            x -= 20
            self.setx(x)
        
    def move_right(self):
        if self.pos() <= self.right_bounds:
            x = self.xcor()
            x += 20
            self.setx(x)
        
        

p = Paddle()
b = Ball()
window.update()

game_on = True

while game_on:
    window.update()
    time.sleep(0.01)
    
    b.move()
    
    
    
    window.listen()
    window.onkey(p.move_left, 'Left')
    window.onkey(p.move_right, 'Right')
    
    window.update()


    
    
    
    
    
