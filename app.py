import turtle
import random

class DrawingApp:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Advanced Turtle Drawing App")
        self.screen.bgcolor("white")

        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("turtle")
        self.turtle.width(2)

        self.colors = ["red", "blue", "green", "yellow", "purple", "orange", "black"]

        self.setup_controls()
        self.screen.mainloop()

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.change_color, "c")
        self.screen.onkey(self.clear_screen, "x")
        self.screen.onkey(self.random_walk, "r")
        self.screen.onkey(self.increase_pen_size, "+")
        self.screen.onkey(self.decrease_pen_size, "-")
        self.screen.onkey(self.draw_triangle, "t")
        self.screen.onkey(self.draw_star, "s")
        self.screen.onclick(self.draw_circle, 1)
        self.screen.onclick(self.move_turtle, 2)
        self.screen.onclick(self.draw_square, 3)

    def change_color(self):
        self.turtle.color(random.choice(self.colors))

    def clear_screen(self):
        self.turtle.clear()

    def random_walk(self):
        for _ in range(100):
            self.turtle.color(random.choice(self.colors))
            self.turtle.forward(30)
            self.turtle.right(random.choice([0, 90, 180, 270]))

    def draw_circle(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.color(random.choice(self.colors))
        self.turtle.begin_fill()
        self.turtle.circle(50)
        self.turtle.end_fill()

    def move_turtle(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()

    def draw_square(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.color(random.choice(self.colors))
        self.turtle.begin_fill()
        for _ in range(4):
            self.turtle.forward(50)
            self.turtle.right(90)
        self.turtle.end_fill()

    def draw_triangle(self):
        self.turtle.color(random.choice(self.colors))
        self.turtle.begin_fill()
        for _ in range(3):
            self.turtle.forward(100)
            self.turtle.left(120)
        self.turtle.end_fill()

    def draw_star(self):
        self.turtle.color(random.choice(self.colors))
        self.turtle.begin_fill()
        for _ in range(5):
            self.turtle.forward(100)
            self.turtle.right(144)
        self.turtle.end_fill()

    def increase_pen_size(self):
        pen_size = self.turtle.pensize()
        self.turtle.pensize(pen_size + 1)

    def decrease_pen_size(self):
        pen_size = self.turtle.pensize()
        if pen_size > 1:
            self.turtle.pensize(pen_size - 1)

if __name__ == "__main__":
    DrawingApp()
