import codecs
import os

import time

from controller import Controller


class Runner:
    start_key = None
    end_key = 'Esc'
    file = 'script'
    is_auto_release = None
    scripts = []
    original = (0, 0)
    actions = {
        'KEY_PRESS': Controller.key_press,
        'KEY_RELEASE': Controller.key_release,
        'MOUSE_MOVE': Controller.mouse_move,
        'MOUSE_CLICK': Controller.mouse_click,
        'MOUSE_SCROLL': Controller.mouse_scroll,
    }

    def __init__(self, start_key, end_key, file, is_auto_release):
        if start_key is not None:
            self.start_key = start_key
        if end_key is not None:
            self.end_key = end_key
        if is_auto_release is not None:
            self.is_auto_release = is_auto_release
        if file is not None:
            self.file = file
            if not os.path.isfile(file):
                print('file not found')
                exit(0)

        fp = codecs.open(self.file, 'r', 'utf-8')
        self.scripts = [line.split(' ') for line in fp.readlines()]

    def handle(self):
        start = False
        for script in self.scripts:
            print(' '.join(script))
            if script[0] == ':ORIGINAL':
                global original
                original = (script[1], self.scripts[2])
            if start is False and script[0] == ':START':
                start = True
            if start is False or len(script) <= 2:
                continue
            if script[0] == ':END':
                break
            if script[0] == ':AUTO_RELEASE':
                self.is_auto_release = bool(script[1]) if self.is_auto_release is None else self.is_auto_release
            if script[0][0] != ':':
                time.sleep(int(script[1]))
                if script[-1] == '\n':
                    script = script[:-1]

                if (script[0] == 'KEY_PRESS' or script[0] == 'MOUSE_CLICK') and self.is_auto_release is True:
                    self.actions[script[0]](*script[2:], self.is_auto_release)
                else:
                    self.actions[script[0]](*script[2:])
