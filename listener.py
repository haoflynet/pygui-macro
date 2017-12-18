
from pynput import keyboard, mouse

from callbacks import Callbacks, StopException


class Listener:
    """
    根据不同的监听组件启用不同的监听方式
    """
    all_mouse_events = {
        'on_move': Callbacks.on_mouse_move,
        'on_click': Callbacks.on_mouse_click,
        'on_scroll': Callbacks.on_mouse_scroll
    }

    all_keyboard_events = {
        'on_press': Callbacks.on_key_press,
        'on_release': Callbacks.on_key_release
    }

    auto_release = True
    listen_mouse_events = {}
    listen_keyboard_events = {}

    def __init__(self, include_events=None, auto_release=True):
        for include_event in include_events:
            if include_event in self.all_mouse_events:
                self.listen_mouse_events[include_event] = self.all_mouse_events[include_event]
            elif include_event in self.all_keyboard_events:
                self.listen_keyboard_events[include_event] = self.all_keyboard_events[include_event]
            else:
                print('the event not found: ' + include_event)
                exit(0)

    def listen(self):
        with keyboard.Listener(**self.listen_keyboard_events) as keyboard_listener:
            with mouse.Listener(**self.listen_mouse_events) as mouse_listener:
                try:
                    keyboard_listener.join()
                    mouse_listener.join()
                except StopException as e:
                    print('stop')
