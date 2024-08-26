from pyray import *

class Entity:
    def __init__(self, start_x, start_y):
        self.pos = Vector2(start_x, start_y)
        img = load_image('rose.png')
        self.texture = load_texture_from_image(img)

    def update(self):
        if is_key_down(KEY_UP):
            self.pos.y -= 5
        elif is_key_down(KEY_DOWN):
            self.pos.y += 5
        if is_key_down(KEY_LEFT):
            self.pos.x -= 5
        elif is_key_down(KEY_RIGHT):
            self.pos.x += 5

    def draw(self):
        draw_texture(self.texture, int(self.pos.x), int(self.pos.y), WHITE)
