# Five-click House. 
# You are to write a program that allows the user to draw a simple house 
# using five mouse clicks. The first two clicks will be the opposite corners of 
# the rectangular frame of the house. The third click will indicate the center 
# of the top edge of a rectangular door. The door should have a total width 
# that is � of the width of the house frame. The sides of the door should 
# extend from the corners of the top down to the bottom of the frame. The 
# fourth click will indicate the center of a square window. The window is 
# half as wide as the door. The last click will indicate the peak of the roof. 
# The edges of the roof will extend from the point at the peak to the corners 
# of the top edge of the house frame. 

from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon, Entry, Oval, Line


def main():
    # Create window
    win = GraphWin("Five-Click House", 500, 500)
    win.setCoords(0, 0, 10, 10)  # Set coordinate system

    # Instructions
    Text(Point(5, 9.5), "Click 1 & 2: House Frame").draw(win)
    Text(Point(5, 9), "Click 3: Door Center").draw(win)
    Text(Point(5, 8.5), "Click 4: Window Center").draw(win)
    Text(Point(5, 8), "Click 5: Roof Peak").draw(win)

    # 1st & 2nd Clicks - House Frame
    p1 = win.getMouse()
    p1.setOutline("red")
    p1.draw(win)
    p2 = win.getMouse()
    p2.setOutline("red")
    p2.draw(win)
    house = Rectangle(p1, p2)
    house.setFill("lightgray")
    house.draw(win)

    # Determine house dimensions
    house_x_min = min(p1.getX(), p2.getX())
    house_x_max = max(p1.getX(), p2.getX())
    house_y_min = min(p1.getY(), p2.getY())  # Bottom
    house_y_max = max(p1.getY(), p2.getY())  # Top
    house_width = house_x_max - house_x_min

    # 3rd Click - Door (centered at click, 1/3 width of house)
    door_center = win.getMouse()
    door_width = house_width / 5
    door_x_min = door_center.getX() - door_width / 2
    door_x_max = door_center.getX() + door_width / 2
    door = Rectangle(Point(door_x_min, house_y_min), Point(door_x_max, door_center.getY()))
    door.setFill("brown")
    door.draw(win)

    # 4th Click - Window (square, half door width)
    window_center = win.getMouse()
    window_size = door_width / 2
    window_x_min = window_center.getX() - window_size / 2
    window_x_max = window_center.getX() + window_size / 2
    window_y_min = window_center.getY() - window_size / 2
    window_y_max = window_center.getY() + window_size / 2
    window = Rectangle(Point(window_x_min, window_y_min), Point(window_x_max, window_y_max))
    window.setFill("blue")
    window.draw(win)

    # 5th Click - Roof Peak
    roof_peak = win.getMouse()
    roof = Polygon(roof_peak, Point(house_x_min, house_y_max), Point(house_x_max, house_y_max))
    roof.setFill("darkred")
    roof.draw(win)

    # Display exit message
    Text(Point(5, 0.5), "Click to exit").draw(win)
    win.getMouse()
    win.close()

main()