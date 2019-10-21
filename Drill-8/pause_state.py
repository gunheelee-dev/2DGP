import game_framework
from pico2d import *
import main_state
import title_state
name = 'PauseState'
image = None
logo_time = 0
def enter():
    global image
    image = load_image('pause.png')
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
    image.clip_draw(0, 0, 900, 900, 400, 300, 100, 100)




    update_canvas()
    delay(0.01)
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass
