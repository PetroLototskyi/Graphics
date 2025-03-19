# Circle Intersection. 
# Write a program that computes the intersection of a circle with a hori
#  zontal line and displays the information textually and graphically. 
# Input: Radius of the circle and they-intercept of the line. 
# Output: Draw a circle centered at (0, 0) with the given radius in a window 
# with coordinates running from -10,-10 to 10,10. 
# Draw a horizontal line across the window with the given y-intercept. 
# Draw the two points of intersection in red. 
# Print out the x values of the points of intersection. 
# Formula: x = ±y'r2- y2 



from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon, Entry, Oval, Line
import math

def main():
    # Create graphics window
    win = GraphWin("Circle-Line Intersection", 400, 400)
    win.setCoords(-10, -10, 10, 10)  # Set coordinate system
    win.setBackground("white")

    # Instructions
    Text(Point(0, 8), "Enter Radius & Y-Intercept, then Click").draw(win)

    # Labels
    Text(Point(-4, 6), "Radius:").draw(win)
    Text(Point(-4, 4), "Y-Intercept:").draw(win)

    # Entry fields
    radius_entry = Entry(Point(2, 6), 5)
    y_intercept_entry = Entry(Point(2, 4), 5)
    radius_entry.draw(win)
    y_intercept_entry.draw(win)

    # Wait for user to enter values and click
    win.getMouse()

    # Get values from Entry boxes
    r = float(radius_entry.getText())
    y_intercept = float(y_intercept_entry.getText())

    # Clear input section
    for item in win.items[:]:
        item.undraw()

    # Draw circle centered at (0,0) with radius r
    circle = Circle(Point(0, 0), r)
    circle.setOutline("blue")
    circle.draw(win)

    # Draw horizontal line at y = y_intercept
    line = Line(Point(-10, y_intercept), Point(10, y_intercept))
    line.setOutline("black")
    line.draw(win)

    # Compute intersection points using formula: x = ± sqrt(r^2 - y^2)
    if abs(y_intercept) > r:
        msg = Text(Point(0, -8), "No intersection: Line is outside circle")
        msg.setFill("red")
        msg.draw(win)
    else:
        x_value = math.sqrt(r**2 - y_intercept**2)
        intersection1 = Point(x_value, y_intercept)
        intersection2 = Point(-x_value, y_intercept)

        # Draw intersection points in red
        for point in [intersection1, intersection2]:
            dot = Circle(point, 0.2)
            dot.setFill("red")
            dot.draw(win)

        # Display intersection values
        result_msg = Text(Point(0, -8), f"Intersections: ({x_value:.2f}, {y_intercept}) & ({-x_value:.2f}, {y_intercept})")
        result_msg.setSize(10)
        result_msg.draw(win)

    # Display exit message
    exit_msg = Text(Point(0, -9.5), "Click to exit")
    exit_msg.draw(win)

    win.getMouse()  # Wait for final click
    win.close()

main()