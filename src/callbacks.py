"""
监听回调函数
"""


scripts = []


def on_mouse_move(x, y):
    pass


def on_mouse_click(x, y, button, pressed):
    pass


def on_mouse_scroll(x, y, dx, dy):
    pass


def on_key_press(key):
    if hasattr(key, 'char'):
        print(key.char)
    else:
        print(key)


def on_key_release(key):
    pass





