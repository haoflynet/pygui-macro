import codecs
import os

import time

from controller import Controller


class Runner:
    delay = 3
    file = 'script'
    is_auto_release = False
    scripts = []
    original = (0, 0)
    actions = {
        'KEY_PRESS': Controller.key_press,
        'KEY_RELEASE': Controller.key_release,
        'MOUSE_MOVE': Controller.mouse_move,
        'MOUSE_CLICK': Controller.mouse_click,
        'MOUSE_SCROLL': Controller.mouse_scroll,
    }

    def __init__(self, delay, file):
        if delay is not None:
            self.delay = int(delay)
        if file is not None:
            self.file = file
            if not os.path.isfile(file):
                print('file not found')
                exit(0)

        fp = codecs.open(self.file, 'r', 'utf-8')
        self.scripts = [line.split(' ') for line in fp.readlines()]

    def handle(self):
        time.sleep(self.delay)
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
                self.is_auto_release = True if script[1] == 'True' else 'False'
            if script[0][0] != ':':
                time.sleep(int(script[1]))
                if script[-1] == '\n':
                    script = script[:-1]

                if (script[0] == 'KEY_PRESS' or script[0] == 'MOUSE_CLICK') and self.is_auto_release is True:
                    self.actions[script[0]](*script[2:], self.is_auto_release)
                else:
                    self.actions[script[0]](*script[2:])
