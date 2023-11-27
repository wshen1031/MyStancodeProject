"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
NUMBER_OF_BRICK = BRICK_COLS*BRICK_ROWS

first_click = True
time_clicked = 0
number_of_brick = NUMBER_OF_BRICK
label = GLabel('Game Over!')
switch = True
# variables 應該放在class BreakoutGraphics裡就好，不需global，方便閱讀


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmouseclicked(self.game_start)
        onmousemoved(self.change_position)
        # method之間使用必須加self.
        # Draw bricks
        brick_x = 0
        brick_y = brick_height
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                if i == 0 or i == 1:
                    self.brick.fill_color = 'red'
                if i == 2 or i == 3:
                    self.brick.fill_color = 'orange'
                if i == 4 or i == 5:
                    self.brick.fill_color = 'yellow'
                if i == 6 or i == 7:
                    self.brick.fill_color = 'green'
                if i == 8 or i == 9:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=brick_x, y=brick_y)
                brick_x += (brick_width + brick_spacing)
            brick_x = 0
            brick_y += (brick_height+brick_spacing)
        self.__dx = 0
        self.__dy = 0

    def change_position(self, mouse):
        self.paddle.x = mouse.x-self.paddle.width/2
        if mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        if mouse.x >= self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        self.paddle.y = self.window.height-PADDLE_OFFSET

    def game_start(self, mouse):
        global first_click, time_clicked
        if first_click is True:
            first_click = False
            time_clicked += 1
            if time_clicked <= 3:
                self.__dy = INITIAL_Y_SPEED
                self.__dx = random.randint(1, MAX_X_SPEED)
                if (random.random() > 0.5):
                    self.__dx = -self.__dx
            # else:
            #     label.font = '-80'
            #     self.window.add(label, x=(self.window.width-label.width)/2, y=(self.window.height-label.height)/2)

    def handle_collision(self):
        global switch, first_click, number_of_brick
        # 偵測撞牆
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx *= -1
        if self.ball.y <= 0:
            self.__dy *= -1
        # 偵測撞到paddle and bricks
        for x in (self.ball.x, self.ball.x+self.ball.width):
            for y in (self.ball.y,  self.ball.y+self.ball.height):
                maybe_object = self.window.get_object_at(x, y)
                if maybe_object is self.paddle:
                    self.__dy *= -1
                    return
                elif maybe_object is not self.paddle and maybe_object is not None:
                    self.__dy *= -1
                    self.window.remove(maybe_object)
                    number_of_brick -= 1
                    return
        # 偵測輸掉遊戲
        if self.ball.y + self.ball.height >= self.window.height:
            self.window.remove(self.ball)
            self.__dx = 0
            self.__dy = 0
            self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/
            2)
            first_click = True
            # return first_click

    def if_game_over(self):
        print(time_clicked)
        if time_clicked > 3 or number_of_brick == 0:
            return True

    def get__dx(self):
        return self.__dx

    def get__dy(self):
        return self.__dy


    # self 為一個class內部溝通橋樑，區分外圍根class內部
    # while true 擺在user端
    # 先擺user, 最後再看哪些可以打包丟到coder
    # getter可以把在coder隱藏的程式丟到user使其看見，蛋user端完全看不到過程，只丟結果
    # instance method為只有創作物件之後，才能對其.然後召喚絕招

