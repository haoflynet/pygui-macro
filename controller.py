from pynput import keyboard


keyboard_controller = keyboard.Controller()


def mouse_move(x, y):
    pass


def mouse_click(x, y, button, pressed):
    pass


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
