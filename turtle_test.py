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


COLORS = ['red', 'blue', 'green', 'yellow', 'orange']


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,180)
        self.write(f'{self.score}', align='center', font=('Courier', 80, 'normal'))
        
    def update_score(self):
        pass
    def increase_score(self):
        pass
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

class Brick_y(Turtle):
    def __init__(self, color, level):
        super().__init__()
        
        self.shape('square')
        self.color = self.color(color)
        self.penup()
        self.setpos(random.randint(-360,360),level)
        self.shapesize(2,4,2)





class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.setheading(90)
        self.color('blue', 'cyan')
        self.penup()
        
        self.setpos(0,-200)
        self.speed('fastest')
        self.acceleration = 2
        
        self.direction_x_speed = self.acceleration
        self.direction_y_speed = self.acceleration
        
    def move(self, px, py):
        #inital movement
        self.setx(self.xcor() + self.direction_x_speed)
        self.sety(self.ycor() + self.direction_y_speed)
        
        #Right Boundry
        if self.xcor() > 410:
            self.setx(410)
            #reverse direction
            self.direction_x_speed *= -1
        #LeftBoundry
        if self.xcor() < -415:
            self.setx(-415)
            #reverse direction
            self.direction_x_speed *= -1
        
        #Upper Boundry
        if self.ycor() > 250:
            self.sety(250)
            #reverse direction
            self.direction_y_speed *= -1
       
       #Lower Boundry 
        if self.ycor() < -280:
           self.setpos(0, -200)
           self.direction_y_speed *= -1
            
        
        self.paddleCollision(px,py)
            
    def paddleCollision(self,px, py):
#         print('paddle',px,py)
        
        #middle collision
        if self.ycor() == py + 20 and self.xcor() == px:
            print('middle paddle')
            self.direction_y_speed *= -1
            
            
        #right collision
        if self.ycor() == py + 20:
            if self.xcor() > px and self.xcor() <= px+40:
                
                self.direction_y_speed *= -1
                print('right paddle')
                
        #left collision
        if self.ycor() == py + 20:
            if self.xcor() < px and self.xcor() >= px-40:
                
                self.direction_y_speed *= -1
                print('left paddle')
        

        
            



class Paddle(Turtle):
    def __init__(self):
        super().__init__()    
        self.shape('square')
        self.color('blue')
        self.penup()
        
        self.speed('fastest')
        self.shapesize(1,4,1)
        self.setpos(0,-220)
        
        #boundry
        self.right_bounds = (360, 220)
        self.left_bounds = (-370, -220)
        
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
s = Score()

for i in range(10):
    b1 = Brick_y(color=COLORS[0], level=0)
    b2 = Brick_y(color=COLORS[1], level=40)
    b2 = Brick_y(color=COLORS[2], level=80)
    b2 = Brick_y(color=COLORS[3], level=120)
    b2 = Brick_y(color=COLORS[4], level=160)






window.update()

game_on = True

while game_on:
    window.update()
    time.sleep(0.01)
    
    b.move(px=p.xcor(),py=p.ycor())
    
    
    
    window.listen()
    window.onkey(p.move_left, 'Left')
    window.onkey(p.move_right, 'Right')
    
    
    
    
    # score board methods 
    window.update()


    
    
    
    
    
