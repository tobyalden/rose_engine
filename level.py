import pyray as rl
import json

class Level:
    def __init__(self):
        img = rl.load_image('walls.png')
        self.texture = rl.load_texture_from_image(img)
        with open('level.json') as file:
            data = json.load(file)
            for layer in data['layers']:
                if layer['name'] == 'walls':
                    self.tileWidth = int(layer['gridCellWidth'])
                    self.tileHeight = int(layer['gridCellHeight'])
                    self.columns = int(layer['gridCellsY'])
                    self.rows = int(layer['gridCellsX'])
                    self.walls = []
                    for row in layer['grid2D']:
                        self.walls.append([i == '1' for i in row])
                    print(self.walls)

    def update(self):
        return

    def draw(self):
        for gridX in range(self.rows):
            for gridY in range(self.columns):
                if self.walls[gridY][gridX]:
                    rl.draw_texture(self.texture, int(gridX * self.tileWidth), int(gridY * self.tileHeight), rl.WHITE)
