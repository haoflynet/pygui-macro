import six

from pynput import keyboard, mouse

from pygui_macro.callbacks import Callbacks, StopException


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

    keyboard_listener = None
    mouse_listener = None

    def __init__(self, include_events=None, auto_release=True):
        for include_event in include_events:
            if include_event in self.all_mouse_events:
                self.listen_mouse_events[include_event] = self.all_mouse_events[include_event]
            elif include_event in self.all_keyboard_events:
                self.listen_keyboard_events[include_event] = self.all_keyboard_events[include_event]
            else:
                print('the event not found: ' + include_event)
                exit(0)

        self.keyboard_listener = keyboard.Listener(**self.listen_keyboard_events)
        self.mouse_listener = keyboard.Listener(**self.listen_mouse_events)

    def listen(self):
        try:
            with keyboard.Listener(**self.listen_keyboard_events) as keyboard_listener:
                with mouse.Listener(**self.listen_mouse_events) as mouse_listener:
                    while True:
                        if not keyboard_listener.running:
                            exc_type, exc_value, exc_traceback = keyboard_listener._queue.get()
                            six.reraise(exc_type, exc_value, exc_traceback)
                        if not mouse_listener.running:
                            exc_type, exc_value, exc_traceback = mouse_listener._queue.get()
                            six.reraise(exc_type, exc_value, exc_traceback)
        except StopException as e:
            pass
