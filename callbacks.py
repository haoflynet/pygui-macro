from pynput import keyboard, mouse

scripts = []


def on_mouse_move(x, y):
    print(x, y)


def on_mouse_click(x, y, button, pressed):
    print(x, y, button, pressed)


def on_mouse_scroll(x, y, dx, dy):
    print(x, y, dx, dy)


def on_key_press(key):
    global scripts
    if '_name_' in key.__dict__:
        char = key._name_
    elif 'char' in key.__dict__:
        char = key.char
    else:
        char = None

    scripts.append(' '.join(['KEY_PRESS', 'None' if char is None else char]))

    if key == keyboard.Key.esc:
        return False


def on_key_release(key):
    global scripts
    if '_name_' in key.__dict__:
        char = key._name_
    elif 'char' in key.__dict__:
        char = key.char
    else:
        char = 'None'

    scripts.append(' '.join(['KEY_RELEASE', 'None' if char is None else char]))


def get_scripts():
    global scripts
    return scripts

