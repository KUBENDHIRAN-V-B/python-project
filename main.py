import tkinter as tk
from snake import Snake
from food import Food


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.width = 400
        self.height = 400
        self.cell_size = 20
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        self.snake = Snake(self.canvas, self.cell_size)
        self.food = Food(self.canvas, self.width, self.height, self.cell_size)

        self.direction = "Right"
        self.game_over = False
        self.score = 0

        self.root.bind("<KeyPress>", self.change_direction)
        self.update()
        self.root.mainloop()

    def change_direction(self, event):
        if event.keysym in ["Left", "Right", "Up", "Down"]:
            self.snake.change_direction(event.keysym)

    def update(self):
        if not self.game_over:
            self.snake.move()
            if self.snake.check_collision(self.width, self.height):
                self.game_over = True
            if self.snake.head == self.food.position:
                self.snake.grow()
                self.food.create_food()
            self.draw()
            self.root.after(100, self.update)
        else:
            self.canvas.create_text(self.width // 2, self.height // 2, text="Game Over", fill="black", font=("Arial", 24))

    def draw(self):
        self.canvas.delete(tk.ALL)
        self.snake.draw()
        self.food.draw()



root = tk.Tk()
game = SnakeGame(root)


