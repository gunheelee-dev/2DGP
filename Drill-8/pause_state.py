import game_framework
from pico2d import *
import main_state
import title_state
name = 'PauseState'
image = None
logo_time =0
def enter():
    global image
    global logo_time
    image = load_image('pause.png')
    logo_time=0
    pass


def exit():
    global image
    del(image)
    pass

def handle_events():
    events= get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_p:
                game_framework.pop_state()
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
    pass


def draw():
    global image
    global logo_time
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    if logo_time<=0.5:
        image.clip_draw(0, 0, 900, 900, 400, 300, 100, 100)
    elif logo_time<=1.0:
        pass
    else:
        logo_time=0
    logo_time+=0.01
    update_canvas()
    delay(0.01)
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass
