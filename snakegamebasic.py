import tkinter as tk
import random

# Window setup
WIDTH = 400
HEIGHT = 400
SPEED = 100
SPACE = 20

# Colors
BG_COLOR = "black"
SNAKE_COLOR = "green"
FOOD_COLOR = "red"

# Create window
root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(root, bg=BG_COLOR, height=HEIGHT, width=WIDTH)
canvas.pack()

# Snake initial
snake = [(100, 100), (80, 100), (60, 100)]
direction = "Right"

# Food
food = None

def create_food():
    global food
    x = random.randint(0, (WIDTH//SPACE) - 1) * SPACE
    y = random.randint(0, (HEIGHT//SPACE) - 1) * SPACE
    food = (x, y)
    canvas.create_rectangle(x, y, x+SPACE, y+SPACE, fill=FOOD_COLOR, tag="food")

def draw_snake():
    canvas.delete("snake")
    for x, y in snake:
        canvas.create_rectangle(x, y, x+SPACE, y+SPACE, fill=SNAKE_COLOR, tag="snake")

def move_snake():
    global snake

    head_x, head_y = snake[0]

    if direction == "Up":
        head_y -= SPACE
    elif direction == "Down":
        head_y += SPACE
    elif direction == "Left":
        head_x -= SPACE
    elif direction == "Right":
        head_x += SPACE

    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    if new_head == food:
        canvas.delete("food")
        create_food()
    else:
        snake.pop()

    # Collision
    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake[1:]
    ):
        game_over()
        return

    draw_snake()
    root.after(SPEED, move_snake)

def change_direction(new_dir):
    global direction
    if (new_dir == "Up" and direction != "Down") or \
       (new_dir == "Down" and direction != "Up") or \
       (new_dir == "Left" and direction != "Right") or \
       (new_dir == "Right" and direction != "Left"):
        direction = new_dir

def game_over():
    canvas.delete("all")
    canvas.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER", fill="white", font=("Arial", 24))

# Controls
root.bind("<Up>", lambda e: change_direction("Up"))
root.bind("<Down>", lambda e: change_direction("Down"))
root.bind("<Left>", lambda e: change_direction("Left"))
root.bind("<Right>", lambda e: change_direction("Right"))

# Start game
create_food()
draw_snake()
move_snake()

root.mainloop()