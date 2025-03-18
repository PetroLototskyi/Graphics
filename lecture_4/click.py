<<<<<<< HEAD
# click . py
from graphics import *
from graphics import Circle, GraphWin, Point, Text, Rectangle


def main ( ) :
    win = GraphWin ( " Click Me ! " )
    for i in range ( 10) :
        p = win . getMouse ( )
        print ("You clicked at : " , p.getX(), p.getY ( ) )
        
    input("Press <Enter> to quit") 
    win. close() 
main ()
=======
from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle

def main() : 
    win = GraphWin("Click Me! ") 
    for i in range(10) : 
        p = win.getMouse() 
        print("You clicked at :", p.getX(), p.getY()) 
main()
>>>>>>> 9875c1644fa10094b6290baaaf609d180b7c1ec5
