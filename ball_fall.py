from pico2d import *
import random


# Game object class here
class Grass:
    pass

class Boy:
    pass


class Ball:
    pass

def handle_events():
    pass

def reset_world():
    pass



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
