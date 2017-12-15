import time

import controller

original = (0, 0)

actions = {
    'KEY_PRESS': controller.key_press,
    'KEY_RELEASE': controller.key_release,
    'MOUSE_MOVE': controller.mouse_move,
    'MOUSE_CLICK': controller.mouse_click,
    'MOUSE_SCROLL': controller.mouse_scroll,
}


def get_original():
    """
    获取初始坐标
    :return:
    """
    global original
    return original


def run(scripts):
    start = False
    for script in scripts:
        if script[0] == ':ORIGINAL':
            global original
            original = (script[1], scripts[2])
        if start is False and script[0] == ':START':
            start = True
        if start is False or len(script) <= 2:
            continue
        if script[0] == ':END':
            break

        time.sleep(int(script[1]))
        if script[-1] == '\n':
            script = script[:-1]

        actions[script[0]](*script[2:])
