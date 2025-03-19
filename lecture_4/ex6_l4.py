
from graphics import * 
# import graphics as graphics
from graphics import Circle, GraphWin, Point, Text, Rectangle, Polygon, Entry, Oval

def main():
    # Create a graphics window
    win = GraphWin("Investment Growth Chart", 400, 300)
    win.setBackground("white")
    win.setCoords(-2, -1000, 12, 10400)

    # Instructions
    Text(Point(5, 9000), "Enter Initial Principal & APR, then Click Anywhere").draw(win)

    # Labels for input fields
    Text(Point(2, 7000), "Initial Principal:").draw(win)
    Text(Point(2, 5500), "Annual Interest Rate (APR):").draw(win)

    # Entry boxes for input
    principal_entry = Entry(Point(8, 7000), 10)
    apr_entry = Entry(Point(8, 5500), 10)
    principal_entry.draw(win)
    apr_entry.draw(win)

    # Wait for user to click before processing input
    win.getMouse()

    # Get user input from entry fields
    principal = float(principal_entry.getText())
    apr = float(apr_entry.getText())

    # Clear the input section
    for item in win.items[:]:
        item.undraw()

    # Draw Y-axis labels (investment growth)
    for i, label in enumerate(["0K", "2.5K", "5.0K", "7.5K", "10K"]):
        Text(Point(-1, i * 2500), label).draw(win)

    # Draw the initial investment bar
    height = principal * 0.02
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for investment growth over 10 years
    for year in range(1, 11):
        principal = principal * (1 + apr)  # Calculate new investment value
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    # Display exit message
    exit_msg = Text(Point(5, 9500), "Click to exit")
    exit_msg.draw(win)
    
    win.getMouse()  # Wait for final click before closing
    win.close()

main()

