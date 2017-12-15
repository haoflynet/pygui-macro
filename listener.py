"""
监听器，默认监听所有事件，可以通过参数指定需要排除的事件
"""
from pynput import keyboard, mouse

import callbacks

mouse_events = {
    'on_move': callbacks.on_mouse_move,
    'on_click': callbacks.on_mouse_click,
    'on_scroll': callbacks.on_mouse_scroll
}

keyboard_events = {
    'on_press': callbacks.on_key_press,
    'on_release': callbacks.on_key_release
}


class StopException(Exception):
    pass


def listen(exclude_events=None):
    for exclude_event in exclude_events:
        if exclude_event in mouse_events:
            del mouse_events[exclude_event]
        if exclude_event in keyboard_events:
            del keyboard_events[exclude_event]

    with keyboard.Listener(**keyboard_events) as keyboard_listener:
        with mouse.Listener(**mouse_events) as mouse_listener:
            try:
                keyboard_listener.join()
                mouse_listener.join()
            except StopException as e:
                print('ok?')


if __name__ == '__main__':
    pass