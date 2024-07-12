import random


class Food:
    def __init__(self, canvas, width, height, cell_size):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.position = self.create_food()

    def create_food(self):
        x = random.randint(0, (self.width - self.cell_size) // self.cell_size) * self.cell_size
        y = random.randint(0, (self.height - self.cell_size) // self.cell_size) * self.cell_size
        self.position = (x, y)
        return self.position

    def draw(self):
        x, y = self.position
        self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill="red")
