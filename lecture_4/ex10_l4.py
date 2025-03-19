# Triangle Information. 
# Same as the previous problem, but with three clicks for the vertices of 
# a triangle. 
# Formulas: For perimeter, see length from the Line Segment problem. 
# area = Js(s- a)(s- b)(s- c
#  ) where a, b, and c are the lengths of 
# the sides and s = a+�+c. 

from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon, Entry, Oval, Line
import math

def distance(p1, p2):
    """Calculates the distance between two points."""
    return math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)

def main():
    # Create a window
    win = GraphWin("Triangle Information", 500, 500)
    win.setCoords(0, 0, 10, 10)  # Set coordinate system

    # Instructions
    Text(Point(5, 9), "Click three points to draw a triangle").draw(win)

    # Get three points for the triangle
    p1 = win.getMouse()
    p1.setOutline("red")
    p1.draw(win)
    p2 = win.getMouse()
    p2.setOutline("red")
    p2.draw(win)
    p3 = win.getMouse()
    p3.setOutline("red")
    p3.draw(win)

    # Draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("lightblue")
    triangle.setOutline("black")
    triangle.draw(win)

    # Calculate the lengths of the sides
    a = distance(p1, p2)  # Side between p1 and p2
    b = distance(p2, p3)  # Side between p2 and p3
    c = distance(p3, p1)  # Side between p3 and p1

    # Calculate the perimeter
    perimeter = a + b + c

    # Calculate the area using Heron's formula
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Display the perimeter and area in the window
    Text(Point(5, 7), f"Perimeter: {perimeter:.2f}").draw(win)
    Text(Point(5, 6), f"Area: {area:.2f}").draw(win)

    # Display exit message
    exit_msg = Text(Point(5, 1), "Click to exit")
    exit_msg.draw(win)

    win.getMouse()  # Wait for user click before closing
    win.close()

main()