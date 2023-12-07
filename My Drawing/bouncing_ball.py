"""
File: 
Name: Willy
-------------------------

"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constant
VX = 3
VY = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
play_time = 0

window = GWindow(800, 500, title='bouncing_ball.py')

ball = GOval(SIZE, SIZE)

switch = True
# switch 預設值為開


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(drop_ball)


def drop_ball(mouse):
    global switch, play_time
    if switch:
        # 當switch開的時候動畫才會跑
        vy = VY
        # VY為常數 不應該變動
        while True:
            # global VY
            switch = False
            # 當動畫開始跑時把開關關掉
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y + ball.height >= window.height and vy > 0:
                vy = -vy * REDUCE
            if ball.x >= window.width:
                break
            pause(DELAY)
        window.add(ball, x=START_X, y=START_Y)
        # VY = 5
        # 每跑完一次動畫把VY回歸到初始值5
        switch = True
        # 當畫面結束時再把開關開啟
        play_time += 1
        if play_time == 3:
            switch = False
        # 當遊戲玩超過三次開關關閉導致再次點擊失效


if __name__ == "__main__":
    main()
