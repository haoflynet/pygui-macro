import codecs
import os
import platform

from callbacks import Callbacks
from listener import Listener


class Recoder:
    start_key = None
    end_key = 'Esc'
    include_events = []
    destination = './'
    file = 'script'
    original = (0, 0)
    original_auto = False
    is_continue = False
    auto_release = True

    def __init__(self, start_key, end_key, include_events, destination, file, original, original_auto, is_continue, auto_release):
        if start_key is not None:
            self.start_key = start_key
        if end_key is not None:
            self.end_key = end_key
        if include_events is not None:
            self.include_events = include_events
        if destination is not None:
            self.destination = destination
            if not os.path.isdir(destination):
                print('the destination not exists: ' + destination)
                exit(0)
        if file is not None:
            self.file = file
        if original is not None:
            self.original = original
        if original_auto is not None:
            self.original_auto = original_auto
        if is_continue is not None:
            self.is_continue = is_continue
        if auto_release is not None:
            self.auto_release = auto_release

    def handle(self):
        Listener(self.include_events, self.auto_release).listen()

    def write(self):
        """
        写入脚本文件
        TODO: 加入SCREEN_SIZE
        :return:
        """
        device_info = ':DEVICE: {} {}'.format(
            platform.system(), platform.release()
        )

        scripts = [device_info, 'True' if self.auto_release else 'False', ':START'] + Callbacks.get_scripts() + [':END']

        fp = codecs.open(os.path.join(self.destination, self.file), 'w', 'utf-8')
        fp.write(' \n'.join(scripts))
        fp.close()
