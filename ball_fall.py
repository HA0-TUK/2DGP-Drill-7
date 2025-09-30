from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    

    def draw(self):
       self.image.draw(400, 30)
    


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8


class Ball:
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running 
    running = True

    global world
    world = []

    grass = Grass()
    world.append(grass)

    characters = [Boy() for i in range(10)]
    world += characters


def update_world():
    pass
def render_world():
    clear_canvas()


    update_canvas()

open_canvas()

reset_world()
    
while running:
    #입력처리
    handle_events()

    # 게임 로직
    update_world()
    # 게임 렌더링
    render_world()
    delay(0.05)

    

close_canvas()
