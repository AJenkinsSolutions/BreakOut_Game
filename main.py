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
        self.goto(-360, 190)
        self.write(f'Score:{self.score}', align='center', font=('Courier', 24, 'normal'))

    def update_score(self):
        self.write(f'Score:{self.score} ', align='center', font=('Courier', 24, 'normal'))

    def increase_score(self, color=None):
        if color == 'red':
            print('Score increase by 10: red')
            self.score += 5
        elif color == 'blue':
            self.score += 10
        elif color == 'green':
            self.score += 15
        elif color == 'yellow':
            self.score += 20
        elif color == 'orange':
            self.score += 25
        else:
            self.score -= 10


        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 80, 'normal'))

class Title(Turtle):
    def __init__(self):
        super().__init__()

        self.title = 'Python BreakOut'
        self.ascii = ''' _______  __   __  _______  __   __  _______  __    _    _______  ______    _______  _______  ___   _  _______  __   __  _______   
|       ||  | |  ||       ||  | |  ||       ||  |  | |  |  _    ||    _ |  |       ||   _   ||   | | ||       ||  | |  ||       |  
|    _  ||  |_|  ||_     _||  |_|  ||   _   ||   |_| |  | |_|   ||   | ||  |    ___||  |_|  ||   |_| ||   _   ||  | |  ||_     _|  
|   |_| ||       |  |   |  |       ||  | |  ||       |  |       ||   |_||_ |   |___ |       ||      _||  | |  ||  |_|  |  |   |    
|    ___||_     _|  |   |  |       ||  |_|  ||  _    |  |  _   | |    __  ||    ___||       ||     |_ |  |_|  ||       |  |   |    
|   |      |   |    |   |  |   _   ||       || | |   |  | |_|   ||   |  | ||   |___ |   _   ||    _  ||       ||       |  |   |    
|___|      |___|    |___|  |__| |__||_______||_|  |__|  |_______||___|  |_||_______||__| |__||___| |_||_______||_______|  |___| '''
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 190)
        self.write(f'{self.ascii}', align='center', font=('Courier', 6, 'normal'))

class DeathCounter(Turtle):
    def __init__(self):
        super().__init__()

        self.death_count = 0
        self.death_symbol = ''
        self.color('red')
        self.hideturtle()
        self.penup()
        self.goto(360, 190)
        self.write(f'{self.death_symbol}', align='center', font=('Courier', 32, 'bold'))


    def update_death_icon(self):
        self.write(f'{self.death_symbol}', align='center', font=('Courier', 32, 'bold'))

    def increase_death_count(self):
        self.death_count += 1

        self.death_symbol += '☠'
        self.clear()

        self.update_death_icon()
        print(self.death_symbol)



class Brick(Turtle):
    def __init__(self, body_color, level, pos):
        super().__init__()

        self.shape('square')
        self.color(body_color)
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

        self.deaths = 0

        self.setpos(0, -200)
        self.speed("normal")

        self.acceleration = 2.5
        self.reverse = -1

        self.direction_x_speed = self.acceleration
        self.direction_y_speed = self.acceleration




    def move(self):

        # initial movement
        self.setx(self.xcor() + self.direction_x_speed)
        self.sety(self.ycor() + self.direction_y_speed)

        # Right Boundary
        if self.xcor() == 410:
            self.make_Sound('wall')
            # debug for some reason setting the self.setx was distrubting collison with brick on this axsis
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

        # Out Of Bounds
        if self.outBounds():
            return True



    def outBounds(self):
        """
        :return:    True if out of Bounds
        """
        if self.ycor() < -280:
            self.make_Sound('outbounds')
            print('outbounds')
            self.setpos(0, -180)
            self.direction_y_speed *= -1
            return True


    def change_speed(self, color):
        print('change speed')
        if color == 'red':
            return 2.5
        elif color == 'blue':
            return 3
        elif color == 'green':
            return 3
        elif color == 'yellow':
            return 3
        elif color == 'orange':
            return 3

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

    def brick_Collision(self, bx, by, color=None):
        Y_EDGE = 30
        X_EDGE = 50

        BRICK_X_LEN = 45
        BRICK_Y_LEN = 25

        # Right edge
        if self.xcor() == bx + X_EDGE:
            if self.ycor() == by:
                print('right middle')
            if by + 25 >= self.ycor() >= by - BRICK_Y_LEN:
                self.direction_x_speed *= self.reverse
                return True
        # Left edge
        if self.xcor() == bx - X_EDGE:
            if by + 25 >= self.ycor() >= by - BRICK_Y_LEN:
                self.direction_x_speed *= self.reverse
                return True

        # Below brick
        if self.ycor() == by - Y_EDGE:
            if self.xcor() == bx:
                self.direction_y_speed *= self.reverse
                return True
            elif bx <= self.xcor() <= bx + BRICK_X_LEN:
                self.direction_y_speed *= self.reverse
                return True
            elif bx >= self.xcor() >= bx - BRICK_X_LEN:
                self.direction_y_speed *= self.reverse
                return True

        # above Brick collision
        if self.ycor() == by + Y_EDGE:
            if self.xcor() == bx:
                self.direction_y_speed *= self.reverse
                return True
            elif bx <= self.xcor() <= bx + BRICK_X_LEN:
                self.direction_y_speed *= self.reverse
                return True
            elif bx >= self.xcor() >= bx - BRICK_X_LEN:
                self.direction_y_speed *= self.reverse
                return True

    def make_Sound(self, collision_type, color=None):
        if collision_type == 'wall':
            playsound('/Users/apjenkins/Development/Audio/Boing copy.wav', block=False)
        elif collision_type == 'paddle':
            playsound('/Users/apjenkins/Development/Audio/Blip copy.wav', block=False)
        elif collision_type == 'brick':
            if color == 'orange':
                playsound(f'/Users/apjenkins/Development/Audio/jump3.wav', block=False)
            else:
                playsound(f'/Users/apjenkins/Development/Audio/{color}.mp3', block=False)
        elif collision_type == 'outbounds':
            playsound('/Users/apjenkins/Development/Audio/wrong.mp3', block=False)



class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.penup()

        self.speed('normal')
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
t = Title()
d = DeathCounter()

init_pos = -360
pos_increment = 0
level = [-50, 0, 50, 100, 150]
bricks = []
color_index = 0

# 5 rows of 8 blocks each
#5  8
for j in range(5):
    pos_increment = 0
    for i in range(8):
        brick = Brick(COLORS[j], level=level[j], pos=-360 + pos_increment)
        bricks.append(brick)
        pos_increment += 100
        color_index += 1


dead_bricks = []
window.update()
game_on = True
while game_on:
    window.update()
    time.sleep(0.01)

    #out of bounds
    if b.move():
        d.increase_death_count()
        window.bgcolor('red')

        window.update()
        time.sleep(1.5)
        window.bgcolor('grey')
        s.increase_score()
        window.update()

    b.paddleCollision(px=p.xcor(), py=p.ycor())

    for i in range(len(bricks)):
        if (b.brick_Collision(bx=bricks[i].xcor(), by=bricks[i].ycor(), color=bricks[i].color()[0])):
            current_brick = bricks[i]
            # remove brick
            current_brick.setpos(0, -400)
            # get color of brick
            s.increase_score(color=current_brick.color()[0])
            b.make_Sound('brick', color=current_brick.color()[0])
            dead_bricks.append(i)






    window.listen()
    window.onkey(p.move_left, 'Left')
    window.onkey(p.move_right, 'Right')

    window.update()


    if len(dead_bricks) == len(bricks):

        # TODO: 1 ADD A GAME OVER SCRREN THAT DISPLAY THE SCORE AND DEATH COUNT
        # TODO: 2 ADD Death count
        # TODO: Refactor write dev doc notes
        game_on = False


print('Console Mes')