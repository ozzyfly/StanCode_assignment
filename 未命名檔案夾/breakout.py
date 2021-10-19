"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()  # import BreakoutGraphics
    lives = NUM_LIVES  # set lives
    dx = graphics.get_velocity_x()  # get velocity of x
    dy = graphics.get_velocity_y()  # get velocity of y
    ball = graphics.ball  # set ball
    bricks = graphics.brick_rows * graphics.brick_cols  # count bricks
    while True:
        if graphics.start:  # check game state
            graphics.ball.move(dx, dy)  # move ball
            if graphics.ball.y >= graphics.window_height:  # check if ball out of boundary
                lives -= 1
                if lives > 0:  # check if the game can continue
                    graphics.window.add(ball, x=(graphics.window_width-graphics.ball_radius)/2,
                                        y=(graphics.window_height-graphics.ball_radius)/2)  # add new ball
                    dx = graphics.set_ball_velocity()  # reset velocity of x
                    graphics.start = False  # check game state
                elif bricks == 0:  # check if the game can continue
                    break
                else:
                    break
        if graphics.detect() == graphics.paddle:  # handle ball hit paddle
            dy = -dy
        elif graphics.detect() != graphics.paddle and graphics.detect() is not None:  # handle ball hit bricks
            graphics.window.remove(graphics.detect())
            dy = -dy
            bricks -= 1
        elif graphics.ball.x <= 0:   # handle ball hit left wall
            dx = -dx
        elif graphics.ball.x + 2 * graphics.ball_radius >= graphics.window_width:   # handle ball hit right wall
            dx = -dx
        elif graphics.ball.y <= 0:   # handle ball hit upper wall
            dy = -dy
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
