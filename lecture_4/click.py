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