# An archery target consists of a central circle of yellow surrounded by concentric rings of red, blue, black and white. Each ring has the same width,
# which is the same as the radius of the yellow circle. Write a program
# that draws such a target. Hint: Objects drawn later will appear on top of
# objects drawn earlier.


from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon, Entry


def draw_circle(win, center, radius, color):
    """Helper function to create and draw a circle."""
    circle = Circle(center, radius)
    circle.setFill(color)
    circle.setOutline("black")  # Adds a border for better visibility
    circle.draw(win)

def main():
    win = GraphWin("Archery Target", 500, 500)  # Create a window
    
    center = Point(250, 250)  # Target center
    r = 20  # Radius of the smallest (yellow) circle
    
    # Draw circles from largest to smallest
    draw_circle(win, center, r * 5, "white")   # Outermost ring
    draw_circle(win, center, r * 4, "black")
    draw_circle(win, center, r * 3, "blue")
    draw_circle(win, center, r * 2, "red")
    draw_circle(win, center, r * 1, "yellow")  # Center circle

    # Display exit message
    msg = Text(Point(250, 20), "Click to exit")
    msg.draw(win)

    win.getMouse()  # Wait for user click before closing
    win.close()

main()
    
    # r=20
    # yellow = r
    # red=r*2
    # blue = r*3
    # black = r*4
    # white = r*5
    # c = Circle (Point (250, 250) , white)
    # c.setFill("white")
    # c.draw(win) 

    # c = Circle (Point (250, 250) , black)
    # c.setFill("black")
    # c.draw(win)

    # c = Circle (Point (250, 250) , blue)
    # c.setFill("blue")
    # c.draw(win)

    # c = Circle (Point (250, 250) , red)
    # c.setFill("red")
    # c.draw(win)

    # c = Circle (Point (250, 250) , yellow)
    # c.setFill("yellow")
    # c.draw(win)
   
    # msg = Text(Point(250, 20),"Click again to quit")
    # msg.draw(win)
    # win.getMouse()  # Wait for final click before closing
    # win.close()  # Close the window
