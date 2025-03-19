# Line Segment Information. 
# This program allows the user to draw a line segment and then displays 
# some graphical and textual information about the line segment. 
# Input: Two mouse clicks for the end points of the line segment. 
# Output: Draw the midpoint of the segment in cyan. 
# Draw the line. 
# Print the length and the slope of the line. 
# Formulas: 
# dx = x2- x1 
# dy = Y2- Yl 
# slope = dy / dx 
# length = J dx2 + dy2

from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon, Entry, Oval, Line
import math

def main():
    # Create a window
    win = GraphWin("Line Segment Information", 500, 500)
    win.setCoords(0, 0, 10, 10)  # Set coordinate system

    # Instructions for user
    Text(Point(5, 9), "Click two points to draw a line").draw(win)

    # Get two user clicks
    p1 = win.getMouse()
    p1.setOutline("red")
    p1.draw(win)
    p2 = win.getMouse()
    p2.setOutline("red")
    p2.draw(win)

    # Draw the line segment
    line = Line(p1, p2)
    line.setWidth(2)
    line.draw(win)

    # Compute midpoint
    mid_x = (p1.getX() + p2.getX()) / 2
    mid_y = (p1.getY() + p2.getY()) / 2
    midpoint = Circle(Point(mid_x, mid_y), 0.2)  # Small circle
    midpoint.setFill("cyan")
    midpoint.draw(win)

    # Compute dx, dy, slope, and length
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()

    length = math.sqrt(dx**2 + dy**2)
    slope = dy / dx if dx != 0 else None  # Avoid division by zero

    # Display text output in the window
    Text(Point(5, 8), f"Length: {length:.2f}").draw(win)
    if slope is not None:
        Text(Point(5, 7.5), f"Slope: {slope:.2f}").draw(win)
    else:
        Text(Point(5, 7.5), "Slope: Undefined (Vertical Line)").draw(win)

    # Display exit message
    exit_msg = Text(Point(5, 1), "Click to exit")
    exit_msg.draw(win)

    win.getMouse()  # Wait for final click before closing
    win.close()

main()