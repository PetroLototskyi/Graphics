from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon

def main() : 
    win = GraphWin("Click and Type", 400, 400) 
    for i in range(10) : 
        pt =     win.getMouse() 
        key = win.getKey() 
        label = Text(pt, key) 
        label.draw(win)
main() 