import pyray as rl

class Entity:
    def __init__(self, start_x, start_y):
        self.pos = rl.Vector2(start_x, start_y)
        img = rl.load_image('rose.png')
        self.texture = rl.load_texture_from_image(img)

    def update(self):
        if rl.is_key_down(rl.KeyboardKey.KEY_UP):
            self.pos.y -= 5
        elif rl.is_key_down(rl.KeyboardKey.KEY_DOWN):
            self.pos.y += 5
        if rl.is_key_down(rl.KeyboardKey.KEY_LEFT):
            self.pos.x -= 5
        elif rl.is_key_down(rl.KeyboardKey.KEY_RIGHT):
            self.pos.x += 5

    def draw(self):
        rl.draw_texture(self.texture, int(self.pos.x), int(self.pos.y), rl.WHITE)
