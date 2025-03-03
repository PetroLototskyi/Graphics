# Print an introduction 
# Get value of principal and apr from user 
# Create a 320x240 GraphWin titled ''Investment Growth Chart'' 
# Draw label " O.OK" at (20, 230) 
# Draw label " 2.5K" at (20, 180) 
# Draw label " 5.0K" at (20, 130) 
# Draw label " 7.5K" at (20, 80) 
# Draw label "10.0K" at (20, 30) 
# Draw a rectangle from (40, 230) to (65, 230 - principal * 0.02) 
# for year running from a value of 1 up through 10: 
# Calculate principal = 
# principal * (1 + apr) 
# Calculate xll = 
# 25 * year + 40 
# Draw a rectangle from (xll, 230) to (xll+25, 230 - principal * 0.02) 
# Wait for user to press Enter

from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle

def main():
    # Introduction 
    print("This program plots the growth of a 10-year investment.")

       # Get principal and interest rate 
    principal=float(input ("Enter the initial principal: ")) 
    apr = float(input ("Enter the annualized interest rate (in decimal if 100% is 1.0): ")) 

    # Create a graphics window with labels on left edge 
    win = GraphWin("Investment Growth Chart", 320, 240) 
    win.setBackground("white") 
    Text(Point(20, 230) , ' O.OK') .draw(win) 
    Text(Point(20, 180) , ' 2.5K') .draw(win) 
    Text(Point(20, 130) , ' 5.0K') .draw(win) 
    Text(Point(20, 80) , ' 7.5K') .draw(win) 
    Text(Point(20, 30) , '10.0K') .draw(win)   

    # Draw bar for initial principal 
    height = principal * 0.02 
    bar = Rectangle(Point(40, 230) , Point(65, 230-height)) 
    bar.setFill("green") 
    bar. setWidth(2) 
    bar.draw(win) 

    # Draw bars for successive years 
    for year in range(1,11) : 
        # calculate value for the next year 
        principal = principal * (1 + apr) 
        # print(principal)
        # draw bar for this value 
        xll = year * 25 + 40 
        height = principal * 0.02 
        bar = Rectangle(Point(xll, 230) , Point(xll+25, 230-height)) 
        bar. setFill ("green") 
        bar.setWidth(2) 
        bar.draw(win) 


    input("Press <Enter> to quit") 
    win. close() 
   
main()
