# Write a program that draws 5 dice on the screen depicting a straight (1, 2, 
# 3, 4, 5 or 2, 3, 4, 5, 6). 


from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon, Entry, Oval
import random

def draw_die(win, x, y, value):
    """Draws a single die at (x, y) with the given value (1-6)."""
    size = 60  # Size of each die
    padding = 10  # Padding for spacing
    die = Rectangle(Point(x, y), Point(x + size, y + size))
    die.setFill("white")
    die.setOutline("black")
    die.setWidth(2)
    die.draw(win)

    # Define dot (pip) positions
    pip_positions = {
        1: [(x + size / 2, y + size / 2)],  # Center
        2: [(x + size / 4, y + size / 4), (x + 3 * size / 4, y + 3 * size / 4)],  # Diagonal
        3: [(x + size / 4, y + size / 4), (x + size / 2, y + size / 2), (x + 3 * size / 4, y + 3 * size / 4)],  # Diagonal + Center
        4: [(x + size / 4, y + size / 4), (x + 3 * size / 4, y + 3 * size / 4),
            (x + 3 * size / 4, y + size / 4), (x + size / 4, y + 3 * size / 4)],  # Four corners
        5: [(x + size / 4, y + size / 4), (x + 3 * size / 4, y + 3 * size / 4),
            (x + 3 * size / 4, y + size / 4), (x + size / 4, y + 3 * size / 4),
            (x + size / 2, y + size / 2)],  # Four corners + center
        6: [(x + size / 4, y + size / 4), (x + 3 * size / 4, y + 3 * size / 4),
            (x + 3 * size / 4, y + size / 4), (x + size / 4, y + 3 * size / 4),
            (x + size / 4, y + size / 2), (x + 3 * size / 4, y + size / 2)]  # Six pips (three rows)
    }

    # Draw pips
    for px, py in pip_positions[value]:
        pip = Circle(Point(px, py), 5)
        pip.setFill("black")
        pip.draw(win)

def main():
    # Create window
    win = GraphWin("Dice Straight", 420, 150)
    win.setBackground("lightgray")

    # Define dice positions and values for a straight sequence (e.g., 1-2-3-4-5)
    start_x, start_y = 20, 50
    dice_values = [1, 2, 3, 4, 5]  # Can change to [2, 3, 4, 5, 6] if needed

    # Draw the dice in a row
    for i in range(5):
        draw_die(win, start_x + i * 80, start_y, dice_values[i])

    # Display exit message
    msg = Text(Point(200, 130), "Click to exit")
    msg.setSize(12)
    msg.draw(win)

    win.getMouse()  # Wait for click to close
    win.close()

main()