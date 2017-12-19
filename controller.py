from pynput import keyboard, mouse


class Controller:
    original = (0, 0)
    keyboard_controller = keyboard.Controller()
    mouse_controller = mouse.Controller()

    @classmethod
    def mouse_move(cls, x, y):
        _x, _y = cls.original
        cls.mouse_controller.position = (_x + float(x), _y + float(y))

    @classmethod
    def mouse_click(cls, button, count=1):
        cls.mouse_controller.click(mouse.Button.__dict__[button], count)

    @classmethod
    def mouse_scroll(cls, x, y, dx, dy):
        pass

    @classmethod
    def key_press(cls, key):
        if key in keyboard.Key.__dict__:
            cls.keyboard_controller.press(keyboard.Key[key])
        else:
            cls.keyboard_controller.press(key)

    @classmethod
    def key_release(cls, key):
        if key in keyboard.Key:
            cls.keyboard_controller.release(keyboard.Key[key])
        else:
            cls.keyboard_controller.release(key)