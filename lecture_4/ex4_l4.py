# Write a program that draws a winter scene with a Christmas tree and a 
# snowman. 

from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon, Entry, Oval
import random
import time


def draw_snowman(win, x, y):
    """Draws a snowman at (x, y)"""
    # Body (three circles)
    base = Circle(Point(x, y), 30)  # Bottom
    middle = Circle(Point(x, y - 40), 20)
    head = Circle(Point(x, y - 70), 15)

    for part in [base, middle, head]:
        part.setFill("white")
        part.draw(win)

    # Eyes
    eye1 = Circle(Point(x - 5, y - 75), 2)
    eye2 = Circle(Point(x + 5, y - 75), 2)
    eye1.setFill("black")
    eye2.setFill("black")
    eye1.draw(win)
    eye2.draw(win)

    # Nose (Carrot)
    nose = Polygon(Point(x, y - 72), Point(x, y - 68), Point(x + 10, y - 70))
    nose.setFill("orange")
    nose.draw(win)

 
def draw_tree(win, x, y):
    """Draws a Christmas tree at (x, y)"""
    # Tree layers (triangles)
    tree1 = Polygon(Point(x, y), Point(x - 40, y + 60), Point(x + 40, y + 60))
    tree2 = Polygon(Point(x, y + 30), Point(x - 35, y + 80), Point(x + 35, y + 80))
    tree3 = Polygon(Point(x, y + 60), Point(x - 30, y + 100), Point(x + 30, y + 100))

    for tree_part in [tree1, tree2, tree3]:
        tree_part.setFill("green")
        tree_part.draw(win)

    # Tree trunk (brown rectangle)
    trunk = Rectangle(Point(x - 10, y + 100), Point(x + 10, y + 120))
    trunk.setFill("brown")
    trunk.draw(win)

    # Tree Star
    star = Circle(Point(x, y - 5), 5)
    star.setFill("yellow")
    star.draw(win)

def draw_snowflakes(win, num_snowflakes):
    """Creates falling snowflakes"""
    snowflakes = []
    for _ in range(num_snowflakes):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        flake = Circle(Point(x, y), 2)
        flake.setFill("white")
        flake.draw(win)
        snowflakes.append(flake)
    return snowflakes

def move_snowflakes(snowflakes, win):
    """Animates snowflakes falling"""
    for _ in range(50):  # Number of animation frames
        for flake in snowflakes:
            flake.move(0, random.randint(2, 5))  # Move down at random speeds
            if flake.getCenter().getY() > 500:  # Reset if reaches bottom
                flake.move(0, -500)
        time.sleep(0.1)

def main():
    # Create window
    win = GraphWin("Winter Scene", 500, 500)
    win.setBackground("skyblue")  # Winter sky color

    # Draw ground (white rectangle)
    ground = Rectangle(Point(0, 400), Point(500, 500))
    ground.setFill("white")
    ground.draw(win)

    # Draw Christmas tree
    draw_tree(win, 150, 250)

    # Draw Snowman
    draw_snowman(win, 350, 350)

    # Draw snowflakes
    snowflakes = draw_snowflakes(win, 50)

    # Animate snowfall
    move_snowflakes(snowflakes, win)

    # Display exit message
    msg = Text(Point(250, 20), "Click to exit")
    msg.draw(win)
    win.getMouse()  # Wait for click to close
    win.close()

main()