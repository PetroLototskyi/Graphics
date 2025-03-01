import graphics as graphics
from graphics import Circle, GraphWin, Point


## A correct way to create two circles. 
leftEye=Circle(Point(80, 50) , 5) 
win = GraphWin() 
leftEye.draw(win)
leftEye.setFill('yellow') 
leftEye.setOutline('red') 
rightEye = leftEye.clone() 
# Circle(Point(100, 50) , 5) 
# rightEye.setFill('yellow') 
# rightEye.setOutline('red')
rightEye.draw(win)
rightEye.move(20,0)
# win = graphics.GraphWin("My Window", 500, 500) 
# Wait for user interaction before closing (prevents instant close)
win.getMouse()  # Click to close
win.close() 