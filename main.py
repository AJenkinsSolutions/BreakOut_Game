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

        self.setpos(0, -200)
        self.speed('fastest')
        self.acceleration = 2

        self.direction_x_speed = self.acceleration
        self.direction_y_speed = self.acceleration

        self.y_collision = None
        self.x_collision = None

    def move(self):
        # inital movement
        self.setx(self.xcor() + self.direction_x_speed)
        self.sety(self.ycor() + self.direction_y_speed)

        # Right Boundary
        if self.xcor() == 410:
            self.make_Sound('wall')
            #debug for some reason setting the self.setx was distrubting collison with brick on this axsis
            # self.setx(409)
            print('right border')
            # reverse direction
            self.direction_x_speed *= -1
        # LeftBoundary
        if self.xcor() < -415:
            self.make_Sound('wall')
            # self.setx(-414)
            # reverse direction
            self.direction_x_speed *= -1

        # Upper Boundary
        if self.ycor() > 250:
            self.make_Sound('wall')
            # self.sety(250)
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
        Y_EDGE = 30
        X_EDGE = 50

        BRICK_X_LEN = 45
        BRICK_Y_LEN = 25


        # Right edg
        if self.xcor() == bx + X_EDGE:
            print('right edge')
            if self.ycor() == by:
                print('right middle')
            if by + 25 >= self.ycor() >= by - BRICK_Y_LEN:
                print('right collision')
                self.direction_x_speed *= -1
                self.make_Sound('brick')
        # Left edge
        if self.xcor() == bx - X_EDGE:
            print('left edge')
            if by + 25 >= self.ycor() >= by - BRICK_Y_LEN:
                print('Left collision')
                self.direction_x_speed *= -1
                self.make_Sound('brick')

        #Below brick
        if self.ycor() == by - Y_EDGE:
            if self.xcor() == bx:
                print('middle brick')
                self.direction_y_speed *= -1
                self.make_Sound('brick')
            elif bx <= self.xcor() <= bx +BRICK_X_LEN:
                print('right brick')
                self.direction_y_speed *= -1
                self.make_Sound('brick')
            elif bx >= self.xcor() >= bx -BRICK_X_LEN:
                print('left brick')
                self.direction_y_speed *= -1
                self.make_Sound('brick')
        # Bottom Brick collision
        if self.ycor() == by + Y_EDGE:
            print('top y inline')
            if self.xcor() == bx:
                print('top middle brick')
                self.direction_y_speed *= -1
                self.make_Sound('brick')
            elif bx <= self.xcor() <= bx +BRICK_X_LEN:
                print('top right brick')
                self.direction_y_speed *= -1
                self.make_Sound('brick')
            elif bx >= self.xcor() >= bx -BRICK_X_LEN:
                print('left brick')
                self.direction_y_speed *= -1
                self.make_Sound('brick')

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

# brick = Brick(COLORS[0], pos=-150, level=-20)
# brick_1 = Brick(COLORS[2], pos=150, level=20)

init_pos = -360
pos_increment = 0
level = [0, 50, 100, 150, 200,250]
bricks = []
color_index = 0
for j in range(5):
    for i in range(3):
        brick = Brick(COLORS[j], level=level[j], pos=-360+pos_increment)
        bricks.append(brick)
        pos_increment += 100
        color_index += 1

print(len(bricks))

window.update()
game_on = True
while game_on:
    window.update()
    time.sleep(0.01)


    b.move()
    b.paddleCollision(px=p.xcor(), py=p.ycor())

    for i in range(len(bricks)):
        b.brick_Collision(bx=bricks[i].xcor(), by=bricks[i].ycor())



    window.listen()
    window.onkey(p.move_left, 'Left')
    window.onkey(p.move_right, 'Right')
    # score board methods
    window.update()








