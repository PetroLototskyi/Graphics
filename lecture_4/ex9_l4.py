# Rectangle Information. 
# This program displays information about a rectangle drawn by the user. 
# Input: Two mouse clicks for the opposite comers of a rectangle. 
# Output: Draw the rectangle. 
# Print the perimeter and area of the rectangle. 
# Formulas: 
# area = (length)(width) 
# perimeter = 2(length +width) 

from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon, Entry, Oval, Line
import math

def main():
    # Create a graphics window
    win = GraphWin("Rectangle Information", 500, 500)
    win.setCoords(0, 0, 10, 10)  # Set coordinate system
    win.setBackground("white")

    # Instructions
    Text(Point(5, 9), "Click two opposite corners of a rectangle").draw(win)

    # Get two mouse clicks
    p1 = win.getMouse()
    p1.setOutline("red")
    p1.draw(win)
    p2 = win.getMouse()
    p2.setOutline("red")
    p2.draw(win)

    # Draw the rectangle
    rect = Rectangle(p1, p2)
    rect.setFill("lightblue")
    rect.setOutline("black")
    rect.draw(win)

    # Compute length and width
    length = abs(p2.getX() - p1.getX()) # abs(...) → Takes the absolute value to ensure the result is always positive.
    width = abs(p2.getY() - p1.getY())

    # Compute area and perimeter
    area = length * width
    perimeter = 2 * (length + width)

    # Display computed values
    Text(Point(5, 7), f"Area: {area:.2f}").draw(win)
    Text(Point(5, 6.5), f"Perimeter: {perimeter:.2f}").draw(win)

    # Display exit message
    exit_msg = Text(Point(5, 1), "Click to exit")
    exit_msg.draw(win)

    win.getMouse()  # Wait for user click before closing
    win.close()

main()