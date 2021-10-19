"""
File: draw_line.py
Name:Fei
-------------------------
TODO: When an odd click sets a point, when even click, draw a line.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 30
window = GWindow()  # initiate the window
point = GOval(SIZE, SIZE)  # initiate the point


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(set_point)


def set_point(e):
    window.add(point, x=e.x, y=e.y)  # add a point while on the first click
    onmouseclicked(line)  # call line function


def line(f):
    n_line = GLine(point.x, point.y, f.x, f.y)  # draw a line while on the second click
    window.remove(point)  # remove the point
    window.add(n_line)  # add a line
    onmouseclicked(set_point)  # call set_point function


if __name__ == "__main__":
    main()
