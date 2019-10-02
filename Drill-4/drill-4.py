from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


x=0
frame =0

def moveRight(dist):
    global frame
    global x
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += dist
    delay(0.05)
def moveLeft(dist):
    global frame
    global x
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x -= dist
    delay(0.05)
while True:
    while x < 800:
        moveRight(5)
    while x>0:
        moveLeft(5)
