from pyray import *
from entity import Entity
from scene import Scene

init_window(640, 360, 'Rose Engine')
set_target_fps(60)

scene = Scene()
rose = Entity(50, 50)
scene.add(rose)

while not window_should_close():
    begin_drawing()
    clear_background(BLUE)
    for entity in scene.entities:
        entity.update()
        entity.draw()
    end_drawing()
close_window()
