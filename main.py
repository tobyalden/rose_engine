import pyray as rl
from entity import Entity
from scene import Scene
from level import Level

rl.init_window(640, 360, 'Rose Engine')
rl.set_target_fps(60)

scene = Scene()
rose = Entity(50, 50)
scene.add(rose)

level = Level()
scene.add(level)

while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.BLUE)
    for entity in scene.entities:
        entity.update()
        entity.draw()
    rl.end_drawing()
rl.close_window()
