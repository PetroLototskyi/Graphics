# Write a program that draws some sort of face. 

from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon, Entry, Oval

def main() : 
    win = GraphWin("Archery Target", 500, 500)  # Create a window
    center = Point(250, 250)  # Target center
    r = 20  # Radius of the smallest (yellow) circle
   
    shape = Circle(center, 70) 
    shape.setOutline("black") 
    shape.setFill("white") 
    shape.draw(win) 

    ly=Circle(Point(250-30,250-20),10)
    ly.setFill("yellow") 
    ly.draw(win)

    ry=Circle(Point(250+30,250-20),10)
    ry.setFill("yellow") 
    ry.draw(win)

  # Use Polygon object to draw the triangle 
    nouse = Polygon(Point(250-5, 250-20), Point(250+5, 250-20),Point(250+12, 250+30), Point(250-12, 250+30)) 
    nouse.setFill("peachpuff") 
    nouse.setOutline("black") 
    nouse.draw(win) 

    mouse=Oval(Point(250-30, 250+42), Point(250+30, 250+47))
    mouse.setFill("red") 
    mouse.draw(win)

    # for i in range(10) : 
    #     p = win.getMouse() 
    #     c = shape.getCenter() 
    #     dx = p.getX() - c.getX() 
    #     dy = p.getY() - c.getY() 
    #     shape.move(dx,dy) 
    msg = Text(Point(250, 20), "Click to exit")
    msg.draw(win)
    win.getMouse()  # Wait for user click before closing
    win.close() 
main()