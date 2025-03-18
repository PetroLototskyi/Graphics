# 1. Alter the program from the last discussion question in the following ways:
# (a) Make it draw squares instead of circles.
# (b) Have each successive click draw an additional square on the screen
# (rather than moving the existing one).
# (c) Print a message on the window "Click again to quit" after the loop,
# and wait for a final click before closing the window.


from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon, Entry

def main() : 
    win = GraphWin("Draw Squares", 500, 500) 

     # Initial message
    msg = Text(Point(250, 20), "Click anywhere to draw a square")
    msg.draw(win)
    
    for i in range(10):  # Allow 10 clicks to draw squares
        p = win.getMouse()  # Get mouse click position
        
        # Define the square size (20x20)
        x, y = p.getX(), p.getY()
        rect = Rectangle(Point(x - 10, y - 10), Point(x + 10, y + 10))
        
        rect.setOutline("red")
        rect.setFill("red")
        rect.draw(win)  # Draw the new square

    # Display exit message
    msg.setText("Click again to quit")
    win.getMouse()  # Wait for final click before closing
    win.close()  # Close the window
main()