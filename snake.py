class Snake:
    def __init__(self, canvas, cell_size):
        self.canvas = canvas
        self.cell_size = cell_size
        self.direction = "Right"
        self.snake = [(100, 100), (80, 100), (60, 100)]

    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Left":
            head_x -= self.cell_size
        elif self.direction == "Right":
            head_x += self.cell_size
        elif self.direction == "Up":
            head_y -= self.cell_size
        elif self.direction == "Down":
            head_y += self.cell_size

        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]

    def grow(self):
        self.snake.append(self.snake[-1])

    def check_collision(self, width, height):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height:
            return True
        if len(self.snake) != len(set(self.snake)):
            return True
        return False

    def draw(self):
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill="green")

    @property
    def head(self):
        return self.snake[0]
