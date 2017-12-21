import codecs
import platform

import time

from pygui_macro.callbacks import Callbacks
from pygui_macro.listener import Listener


class Recoder:
    delay = 3
    end_key = 'Esc'
    include_events = []
    file = 'script'
    original = (0, 0)
    original_auto = False
    is_continue = False
    auto_release = True

    def __init__(self, delay, end_key, include_events, file, original, original_auto, is_continue, auto_release):
        if delay is not None:
            self.delay = int(delay)
        if end_key is not None:
            self.end_key = end_key
        if include_events is not None:
            self.include_events = include_events
        if file is not None:
            self.file = file
        if original is not None:
            self.original = original
        if original_auto is not None:
            self.original_auto = original_auto
        if is_continue is not None:
            self.is_continue = is_continue
        if auto_release is not None:
            if auto_release in ['0', 'False', 'false']:
                self.auto_release = False

    def handle(self):
        time.sleep(self.delay)
        Listener(self.include_events, self.auto_release).listen()
        self.write()

    def write(self):
        """
        写入脚本文件
        TODO: 加入SCREEN_SIZE
        :return:
        """
        device_info = ':DEVICE: {} {}'.format(
            platform.system(), platform.release()
        )

        scripts = [
                      device_info,
                      ':AUTO_RELEASE ' + ('True' if self.auto_release else 'False'),
                      '',
                      ':START'
                  ] + Callbacks.get_scripts() + [':END', '']

        fp = codecs.open(self.file, 'w', 'utf-8')
        fp.write(' \n'.join(scripts))
        fp.close()
