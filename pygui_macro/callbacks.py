import time

from pynput import keyboard


class StopException(Exception):
    pass


class Callbacks:
    """
    不同的监听方式仍然有相同的回调函数
    """
    scripts = []
    current_time = int(time.time())

    @classmethod
    def on_mouse_move(cls, x, y):
        print(x, y)

    @classmethod
    def on_mouse_click(cls, x, y, button, pressed):
        cls.scripts.append(' '.join(['MOUSE_MOVE', cls.get_and_update_time(), str(x), str(y)]))
        if pressed:
            cls.scripts.append(' '.join(['MOUSE_PRESS', '0', button.name]))
        else:
            cls.scripts.append(' '.join(['MOUSE_RELEASE', cls.get_and_update_time(), button.name]))

    @classmethod
    def on_mouse_scroll(cls, x, y, dx, dy):
        cls.scripts.append(' '.join(['MOUSE_SCROLL', cls.get_and_update_time(), str(x), str(y), str(dx), str(dy)]))

    @classmethod
    def on_key_press(cls, key):
        if key == keyboard.Key.esc:
            raise StopException('stop by esc')

        if '_name_' in key.__dict__:
            char = key._name_
        elif 'char' in key.__dict__:
            char = key.char
        else:
            char = None
        cls.scripts.append(' '.join(['KEY_PRESS', cls.get_and_update_time(), 'None' if char is None else char]))

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