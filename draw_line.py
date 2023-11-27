"""
File: 
Name: Willy
-------------------------
Use onmouseclicked to create either a circle or a line. If the clicking time is odd, the window draw a circle, and if it
is even, the window draw a line. I put circle, click, and window as global variables
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5
window = GWindow()
circle = GOval(SIZE, SIZE)
click = 1


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_circle_or_line)


def draw_circle_or_line(mouse):
    global click
    if click % 2 == 1:
        circle.x = mouse.x-SIZE/2
        circle.y = mouse.y-SIZE/2
        window.add(circle)
        click += 1
    else:
        line = GLine(circle.x+SIZE/2, circle.y+SIZE/2, mouse.x-SIZE/2, mouse.y-SIZE/2)
        window.add(line)
        click += 1
        window.remove(circle)


if __name__ == "__main__":
    main()
