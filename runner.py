import time

import controller

actions = {
    'KEY_PRESS': controller.key_press,
    'KEY_RELEASE': controller.key_release,
    'MOUSE_MOVE': controller.mouse_move,
    'MOUSE_CLICK': controller.mouse_click,
    'MOUSE_SCROLL': controller.mouse_scroll,
}


def run(scripts):
    start = False
    for script in scripts:
        if start is False and script[0] == ':START':
            start = True
        if start is False or len(script) <= 2:
            continue
        if script[0] == ':END':
            break

        time.sleep(int(script[1]))
        actions[script[0]](*script[2:-1])
