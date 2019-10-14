from pico2d import *
import random
# Game object class here
open_canvas()
running=True
class Boy:
    def __init__(self):
        self.image=load_image("run_animation.png")
        self.y=90
        self.frame=random.randint(0,7)
        self.x=random.randint(100,700)
    def draw(self):
        self.image.clip_draw(100*self.frame,0,100,100,self.x,self.y)
    def update(self):
        self.frame+=1
        self.frame=self.frame%8
        self.x+=5
class Grass:
    def __init__(self):
        self.image=load_image("grass.png")
    def draw(self):
        self.image.draw(400,30)
class Ball:
    def __init__(self):
        self.type=random.randint(0,1)
        self.x=random.randint(100,700)
        self.y=600
        self.speed = random.randint(1,10)
        if self.type == 0:
            self.image=load_image("ball21x21.png")
        else:
            self.image=load_image("ball41x41.png")

    def update(self):
        if self.y > 70:
            self.y -= self.speed*1

    def draw(self):
        self.image.draw(self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code

balls = [Ball() for i in range(20)]
grass = Grass()
team = [Boy() for i in range(11)]
# game main loop code
while running:
    handle_events()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.update()
        boy.draw()
    for ball in balls:
        ball.draw()
        ball.update()
    update_canvas()
    delay(0.05)

# finalization code
close_canvas()