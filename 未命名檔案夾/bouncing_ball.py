"""
File: bouncing.py
Name: Fei
-------------------------
TODO: To create a bouncing ball when clicking the mouse in 3 turns, then no action when clicking the mouse.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')  # initiate the window

ball = GOval(SIZE, SIZE,)  # initiate the ball
ball.filled = True  # initiate the ball
window.add(ball, START_X, START_Y)  # initiate the ball

turn = 3    # to count on 3 turns
start = False  # to set a switch to let mouseclick without any reaction.


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bounce)


def bounce(click):
    global start, turn  # let the function know the global variable.
    vx = VX  # use VX as local variable
    if not start and turn > 0:  # check turns and set switch
        start = True  # set switch
        while True:
            if ball.x > window.width:  # reset the ball when out of boundary
                turn -= 1  # minus one turn
                window.add(ball, START_X, START_Y)  # add new ball
                start = False  # set switch
                break
            if turn > 0:  # move the ball
                ball.move(5, vx)
                if ball.y >= window.height:
                    vx *= REDUCE
                    vx = -vx
                vx += GRAVITY
                pause(DELAY)


if __name__ == "__main__":
    main()
