"""
监听器，默认监听所有事件，可以通过参数指定需要排除的事件
"""
from pynput import keyboard, mouse

from . import callbacks


mouse_events = {
    'mouse_move': callbacks.on_mouse_move,
    'mouse_click': callbacks.on_mouse_click,
    'mouse_scroll': callbacks.on_mouse_scroll
}

keyboard_events = {
    'key_press': callbacks.on_key_press,
    'key_release': callbacks.on_key_release
}


def listen(exclude_events=None):
    for exclude_event in exclude_events:
        del mouse_events[exclude_event]
        del keyboard_events[exclude_event]

    with keyboard.Listener(**keyboard_events) as keyboard_listener:
        with mouse.Listener(**mouse_events) as mouse_listener:
            keyboard_listener.join()
            mouse_listener.join()


if __name__ == '__main__':
    pass