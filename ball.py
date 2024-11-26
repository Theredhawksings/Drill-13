from pico2d import *
import game_world
import game_framework
import random
import server

class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(0, server.background_width)
        self.y = y if y else random.randint(0, server.background_height)

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom
        self.image.draw(sx, sy)
        draw_rectangle(sx - 10, sy - 10, sx + 10, sy + 10)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            if self in game_world.all_objects():  # 객체가 게임 월드에 존재하는지 확인
                game_world.remove_object(self)
