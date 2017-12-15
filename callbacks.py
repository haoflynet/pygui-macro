import time

from pynput import keyboard

from listener import StopException


class Callbacks:
    """
    不同的监听方式仍然有相同的回调函数
    """
    scripts = []
    current_time = 0

    @classmethod
    def on_mouse_move(cls, x, y):
        print(x, y)

    @classmethod
    def on_mouse_click(cls, x, y, button, pressed):
        cls.scripts.append(' '.join(['MOUSE_MOVE', cls.get_and_update_time(), x, y]))
        cls.scripts.append(' '.join(['MOUSE_CLICK', '0', button]))

    @classmethod
    def on_mouse_scroll(cls, x, y, dx, dy):
        print(x, y, dx, dy)

    @classmethod
    def on_key_press(cls, key):
        if '_name_' in key.__dict__:
            char = key._name_
        elif 'char' in key.__dict__:
            char = key.char
        else:
            char = None
        cls.scripts.append(' '.join(['KEY_PRESS', cls.get_and_update_time(), 'None' if char is None else char]))

        if key == keyboard.Key.ecs:
            raise StopException('stop')

    @classmethod
    def on_key_release(cls, key):
        if '_name_' in key.__dict__:
            char = key._name_
        elif 'char' in key.__dict__:
            char = key.char
        else:
            char = 'None'

        cls.scripts.append(' '.join(['KEY_RELEASE', cls.get_and_update_time(), 'None' if char is None else char]))

    @classmethod
    def get_and_update_time(cls):
        difference = int(time.time()) - cls.current_time
        cls.current_time = int(time.time())
        return str(difference)

    @classmethod
    def get_scripts(cls):
        return cls.scripts