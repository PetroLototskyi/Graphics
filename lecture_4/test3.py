from graphics import GraphWin, Circle, Point
win = GraphWin()
center= Point(100,100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)
win.getMouse()  # Click to close
win.close()