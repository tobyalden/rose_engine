from pyray import *
init_window(640, 360, 'Rose Engine')
set_target_fps(60)
img = load_image('rose.png')
texture = load_texture_from_image(img)
pos = Vector2(50, 50)
while not window_should_close():
    if is_key_down(KEY_UP):
        pos.y -= 5
    elif is_key_down(KEY_DOWN):
        pos.y += 5
    if is_key_down(KEY_LEFT):
        pos.x -= 5
    elif is_key_down(KEY_RIGHT):
        pos.x += 5
    begin_drawing()
    clear_background(BLUE)
    draw_texture(texture, int(pos.x), int(pos.y), WHITE)
    end_drawing()
close_window()
