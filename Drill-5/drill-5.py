from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global working
    global running
    global interrupt
    global x,y
    global cx,cy
    events= get_events()
    for event in events:
        if event.type==SDL_QUIT:
            working=False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT -1 -event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            working=False
        elif event.type==SDL_MOUSEBUTTONDOWN:
            interrupt =True
            running = True

    pass

def draw_character(p1, p2):
    global running
    global cx,cy
    global interrupt
    frame=0
    fframe=1
    interrupt=False
    if running == True:
        for i in range(0,1000+1,2):
            handle_events()
            if interrupt==True:
                return
            t=i/1000
            cx=(1-t)*p1[0]+t*p2[0]
            cy= (1-t)*p1[1]+t*p2[1]
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            pointer.draw(x, y)
            character.clip_draw(frame * 100, 100 * fframe, 100, 100, cx, cy)
            frame=(frame+1)%8
            if cx<p2[0]:
                fframe=1
            else:
                fframe=0

            update_canvas()


    running =False
    pass


open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
pointer =  load_image('hand_arrow.png')
working = True
running = False
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
cx,cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
#커밋횟수
while working:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    pointer.draw(x,y)
    if running:
        draw_character((cx,cy),(x-30,y+30))
    character.clip_draw(frame * 100, 100 * 1, 100, 100, cx, cy)
    update_canvas()
    handle_events()

close_canvas()




