"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 20  # 100 frames per second
NUM_LIVES = 3  # Number of attempts

graphics = BreakoutGraphics()
ball = graphics.ball
window = graphics.window
dx = graphics.dx  # property  graphics.get_dx()改成graphics.dx(像是attribute的寫法)
dy = graphics.dy

count = 0  # ball drop to floor
brick = 0  # amount of brick drop
brick_col = graphics.get_brick_col()
brick_row = graphics.get_brick_row()


def main():
    global graphics, ball, window, dx, dy, count, brick

    label = GLabel("Game Over!")
    label.font = "-20"

    while True:
        if graphics.click_turn_on:
            if count <= 3:
                ball.move(dx, dy)
                # check wall
                if ball.x + ball.width / 2 >= window.width or ball.x - ball.width / 2 <= 0:
                    dx = -dx
                if ball.y - ball.height / 2 <= 0:  # hit ceiling
                    dy = -dy
                if ball.y + ball.height / 2 >= window.height:  # hit floor
                    graphics.click_turn_on = False
                    window.remove(ball)
                    window.add(ball, x=window.height / 2 - ball.height, y=window.width / 2 - ball.width)
                    count += 1
                # bounce
                collision()
                # Game over
                # remove all bricks
                if brick == brick_col * brick_row:
                    window.remove(ball)
                    window.add(label, x=(window.width - label.width) / 2, y=(window.height - label.height) / 2)
                    break
                # count>=3
                if ball.y + ball.height / 2 >= window.height:
                    count += 1
                if count == NUM_LIVES:
                    window.remove(ball)
                    window.add(label, x=(window.width - label.width) / 2, y=(window.height - label.height) / 2)
                    break
        pause(FRAME_RATE)


def collision():
    global graphics, ball, window, dx, dy, count, brick
    maybe_obj_1 = window.get_object_at(ball.x, ball.y)
    maybe_obj_2 = window.get_object_at(ball.x + ball.width, ball.y)
    maybe_obj_3 = window.get_object_at(ball.x, ball.y + ball.width)
    maybe_obj_4 = window.get_object_at(ball.x + ball.width, ball.y + ball.width)

    if maybe_obj_1 is not None:
        if 0 < ball.y < window.height / 2:  # upper side of the window->maybe obj is brick
            window.remove(maybe_obj_1)
            brick += 1
        bounce()
        # else:
        #     bounce()  # lower side of the window->maybe obj is paddle
    elif maybe_obj_2 is not None:
        if 0 < ball.y < window.height / 2:
            window.remove(maybe_obj_2)
            brick += 1
        bounce()
        # else:
        #     bounce()
    elif maybe_obj_3 is not None:
        if 0 < ball.y < window.height / 2:
            window.remove(maybe_obj_3)
            brick += 1
        bounce()
        # else:
        #     bounce()
    elif maybe_obj_4 is not None:
        if 0 < ball.y < window.height / 2:
            window.remove(maybe_obj_4)
            brick += 1
        bounce()
        # else:
        #     bounce()


def bounce():
    global graphics, ball, window, dx, dy
    # 球的下面兩點碰到板子
    if window.get_object_at(ball.x, ball.y + ball.width) is graphics.paddle or window.get_object_at(ball.x,
                                                                                                    ball.y + ball.width) is graphics.paddle:
        x = ball.x
        window.remove(ball)
        window.add(ball, x=x, y=graphics.paddle.y - ball.width)  # 不讓球的下面兩點卡在板子裡

    dy = -dy


# Add the animation loop here!


if __name__ == '__main__':
    main()
