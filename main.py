from turtle import *
import time
import random
from playsound import playsound


file = '/Users/apjenkins/Development/Audio/blue.mp3'

# Screen Configuration
window = Screen()
window.setup(858, 525, 50, 50)
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
        self.goto(0, 180)
        self.write(f'{self.score}', align='center', font=('Courier', 80, 'normal'))

    def update_score(self):
        pass

    def increase_score(self):
        pass

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 80, 'normal'))


class Brick(Turtle):
    def __init__(self, color, level, pos):
        super().__init__()

        self.shape('square')
        self.color = self.color(color)
        self.penup()
        self.setpos(pos, level)
        self.shapesize(2, 4, 2)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.setheading(90)
        self.color('blue', 'cyan')
        self.penup()

        self.setpos(-0, 200)
        self.speed('fastest')
        self.acceleration = 2

        self.direction_x_speed = self.acceleration
        self.direction_y_speed = self.acceleration

    def move(self, px, py, bx, by):
        # inital movement
        # self.setx(self.xcor() - self.direction_x_speed)
        self.sety(self.ycor() - self.direction_y_speed)

        self.brick_Collision(bx, by)
        self.paddleCollision(px, py)

        # Right Boundary
        if self.xcor() >= 410:
            self.make_Sound('wall')
            self.setx(409)
            # reverse direction
            self.direction_x_speed *= -1
        # LeftBoundary
        if self.xcor() < -415:
            self.make_Sound('wall')
            self.setx(-414)
            # reverse direction
            self.direction_x_speed *= -1

        # Upper Boundary
        if self.ycor() > 250:
            self.make_Sound('wall')
            self.sety(250)
            # reverse direction
            self.direction_y_speed *= -1

        # Lower Boundary
        if self.ycor() < -280:
            self.make_Sound('outbounds')
            self.setpos(0, -180)
            self.direction_y_speed *= -1



    def paddleCollision(self, px, py):
        #         print('paddle',px,py)
        # middle collision
        if self.ycor() == py + 20 and self.xcor() == px:
            print('middle paddle')
            self.direction_y_speed *= -1
            self.make_Sound('paddle')

        # right collision
        if self.ycor() == py + 20:
            if self.xcor() > px and self.xcor() <= px + 40:
                self.direction_y_speed *= -1
                print('right paddle')
                self.make_Sound('paddle')

        # left collision
        if self.ycor() == py + 20:
            if self.xcor() < px and self.xcor() >= px - 40:
                self.direction_y_speed *= -1
                print('left paddle')
                self.make_Sound('paddle')

    def brick_Collision(self, bx, by):
        #Below brick
        if self.ycor() == by -30:
            if self.xcor() == bx:
                print('middle brick')
                self.direction_y_speed *= -1
            elif bx <= self.xcor() <= bx +45:
                print('right brick')
                self.direction_y_speed *= -1
            elif bx >= self.xcor() >= bx-45:
                print('left brick')
                self.direction_y_speed *= -1
        #Bottom Brick collision
        if self.ycor() == by + 30:
            print('top y inline')
            if self.xcor() == bx:
                print('top middle brick')
                self.direction_y_speed *= -1
            elif bx <= self.xcor() <=bx +45:
                print('top right brick')
                self.direction_y_speed *= -1
            elif bx >= self.xcor() >= bx-45:
                print('left brick')
                self.direction_y_speed *= -1



        #Right Brick Collision
        #This might need to be fixed
        # bug maybe present
        if self.xcor() == bx + 50:
            print('right edge')
            if by + 25 >= self.ycor() >= by -25:
                print('right collision')
                self.direction_x_speed *= -1



        if self.xcor() == bx - 50:
            print('left edge')
            if by + 25 >= self.ycor() >= by -25:
                print('Left collision')
                self.direction_x_speed *= -1















    def make_Sound(self, collision_type):
        if collision_type == 'wall':
            playsound('/Users/apjenkins/Development/Audio/Boing copy.wav', block=False)
        elif collision_type == 'paddle':
            playsound('/Users/apjenkins/Development/Audio/Blip copy.wav', block=False)
        elif collision_type == 'brick':
            playsound('/Users/apjenkins/Development/Audio/red.mp3', block=False)

        elif collision_type == 'outbounds':
            playsound('/Users/apjenkins/Development/Audio/wrong.mp3', block=False)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.penup()

        self.speed('fastest')
        self.shapesize(1, 4, 1)
        self.setpos(0, -220)

        # boundry
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

# init Objects
p = Paddle()
b = Ball()
s = Score()
brick = Brick(COLORS[0], pos=0, level=0)

# init_pos = -360
# pos_increment = 0
# for i in range(9):
#     b1 = Brick_y(color=COLORS[0], pos=init_pos+pos_increment+random.randint(0,random.randint(2,13)), level=0)
#     b2 = Brick_y(color=COLORS[1], pos=init_pos+pos_increment+random.randint(0,random.randint(2,9)), level=40)
#     b2 = Brick_y(color=COLORS[2], pos=init_pos+pos_increment+random.randint(0,random.randint(3,8)), level=80)
#     b2 = Brick_y(color=COLORS[3], pos=init_pos+pos_increment+random.randint(0,random.randint(4,12)), level=120)
#     b2 = Brick_y(color=COLORS[4], pos=init_pos+pos_increment+random.randint(0,random.randint(3,16)), level=160)
#
#     pos_increment += random.randint(80, 100)


window.update()
game_on = True
while game_on:
    window.update()
    time.sleep(0.01)

    b.move(px=p.xcor(), py=p.ycor(), bx=brick.xcor(), by=brick.ycor())

    window.listen()
    window.onkey(p.move_left, 'Left')
    window.onkey(p.move_right, 'Right')
    # score board methods
    window.update()








