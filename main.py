from pyray import *
from entity import Entity

init_window(640, 360, 'Rose Engine')
set_target_fps(60)

rose = Entity(50, 50)
entities = [rose]

while not window_should_close():
    begin_drawing()
    clear_background(BLUE)
    for entity in entities:
        entity.update()
        entity.draw()
    end_drawing()
close_window()
