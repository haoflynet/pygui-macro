import runner

from pynput import keyboard, mouse


keyboard_controller = keyboard.Controller()
mouse_controller = mouse.Controller()


def mouse_move(x, y):
    _x, _y = runner.get_original()
    mouse_controller.position = (_x + float(x), _y + int(y))


def mouse_click(button, count=1):
    mouse_controller.click(mouse.Button.__dict__[button], count)


def mouse_scroll(x, y, dx, dy):
    pass


def key_press(key):
    if key in keyboard.Key.__dict__:
        keyboard_controller.press(keyboard.Key[key])
    else:
        keyboard_controller.press(key)


def key_release(key):
    if key in keyboard.Key:
        keyboard_controller.release(keyboard.Key[key])
    else:
        keyboard_controller.release(key)
