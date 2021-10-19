"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout', dx=MAX_X_SPEED, dy=INITIAL_Y_SPEED,):
        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        # Create a paddle
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.paddle = GRect(width=self.paddle_width, height=self.paddle_height,
                            x=(self.window_width-self.paddle_width)/2,
                            y=self.window_height-self.paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(self.ball_radius*2, self.ball_radius*2, x=(self.window_width-self.ball_radius)/2,
                          y=(self.window_height-self.ball_radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = dx
        self.__dy = dy
        self.get_velocity_x()
        self.get_velocity_y()
        self.set_ball_velocity()
        # Draw bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        for row in range(self.brick_rows):
            for col in range(self.brick_cols):
                self.brick = GRect(width=self.brick_width, height=self.brick_height,
                                   x=(self.brick_width + self.brick_spacing) * col
                                   , y=self.brick_offset + (self.brick_height + self.brick_spacing) * row)
                self.brick.filled = True
                if row < 2:
                    self.brick.fill_color = "RED"
                elif row == 2 or row == 3:
                    self.brick.fill_color = "ORANGE"
                elif row == 4 or row == 5:
                    self.brick.fill_color = "YELLOW"
                elif row == 6 or row == 7:
                    self.brick.fill_color = "GREEN"
                else:
                    self.brick.fill_color = "BLUE"
                self.window.add(self.brick)
        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.handle_click)
        self.start = False
        # detect if ball hit other objects
        self.detect()

    def detect(self):
        obj = self.window.get_object_at(self.ball.x, self.ball.y)
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            return self.window.get_object_at(obj.x, obj.y)
        elif self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y) is not None:
            return self.window.get_object_at(self.ball.x+2*self.ball_radius, self.ball.y)
        elif self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius) is not None:
            return self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius)
        elif self.window.get_object_at(self.ball.x + 2 * self.ball_radius,
                                       self.ball.y + 2 * self.ball_radius) is not None:
            return self.window.get_object_at(self.ball.x + 2 * self.ball_radius,
                                             self.ball.y + 2 * self.ball_radius)
        else:
            return None

    def get_velocity_x(self):
        return self.__dx

    def get_velocity_y(self):
        return self.__dy

    def set_ball_velocity(self):
        self.__dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    def paddle_move(self, m):
        if 0 - self.paddle_width <= m.x < self.window_width - self.paddle_width:
            self.window.add(self.paddle, x=(m.x + self.paddle_width) / 2,
                            y=self.window_height - self.paddle_offset)
        elif m.x > self.window_width - self.paddle_width:
            self.window.add(self.paddle, x=self.window_width - self.paddle_width,
                            y=self.window_height - self.paddle_offset)

    def handle_click(self, event):
        if not self.start:
            self.start = True
