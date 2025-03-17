from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle

def main() : 
    win = GraphWin("Click Me! ") 
    for i in range(10) : 
        p = win.getMouse() 
        print("You clicked at :", p.getX(), p.getY()) 
main()