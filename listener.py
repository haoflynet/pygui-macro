
from pynput import keyboard, mouse

from callbacks import Callbacks, StopException


class Listener:
    """
    根据不同的监听组件启用不同的监听方式
    """
    mouse_events = {
        'on_move': Callbacks.on_mouse_move,
        'on_click': Callbacks.on_mouse_click,
        'on_scroll': Callbacks.on_mouse_scroll
    }

    keyboard_events = {
        'on_press': Callbacks.on_key_press,
        'on_release': Callbacks.on_key_release
    }

    def __init__(self, excludes_events=None):
        for exclude_event in excludes_events:
            if exclude_event in self.mouse_events:
                del self.mouse_events[exclude_event]
            if exclude_event in self.keyboard_events:
                del self.keyboard_events[exclude_event]

    def listen(self):
        with keyboard.Listener(**self.keyboard_events) as keyboard_listener:
            with mouse.Listener(**self.mouse_events) as mouse_listener:
                try:
                    keyboard_listener.join()
                    mouse_listener.join()
                except StopException as e:
                    print('stop')
