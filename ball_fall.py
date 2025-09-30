from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    

    def draw(self):
       self.image.draw(400, 30)

    def update(self):
        pass
    


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
    # 위치: x랜덤 y 599 
    # 속도 랜덤 등속운동
    # grass에 닿으면 멈춤 
    # 사이즈 2개중 랜덤 (랜덤 숫자가 0 = 21 1 = 41)
    def __init__(self):
        self.size = random.randint(0,1)

        self.x = random.randint(0, 800) # 창 너비
        self.y = 599

        self.speed = random.randint(30, 100)

        self.floor = 60
        if self.size == 0:
            self.image = load_image('ball21x21.png')


        else:
            self.image = load_image('ball41x41.png')


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y > self.floor: 
            move_y = (self.floor / (self.floor - self.y)) * self.speed
            if self.y + move_y >= self.floor:
                self.y += move_y
            else:
                self.y = self.floor
                self.speed = 0
            




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

    balls = [Ball() for i in range(20)]
    world += balls

def update_world():
    for obj in world:
        obj.update()

        
def render_world():
    clear_canvas()

    for obj in world:
        obj.draw()

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
