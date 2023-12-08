"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
label = GLabel('Game over!')

def main():
    graphics = BreakoutGraphics()
    # # Add the animation loop here!
    while True:
        # 先處理碰撞行為 handle collision
        graphics.handle_collision()
        dx = graphics.get__dx()
        dy = graphics.get__dy()
        graphics.ball.move(dx, dy)
        pause(FRAME_RATE)
        if graphics.if_game_over() is True:
            break
    label.font = '-80'
    graphics.window.add(label, x=(graphics.window.width - label.width) / 2, y=(graphics.window.height - label.height) /
    2)


if __name__ == '__main__':
    main()
