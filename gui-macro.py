"""
TODO： 手动编辑、if语句、while语句
"""
import codecs
import os
import argparse
import platform

from listener import listen
from runner import run
from callbacks import get_scripts, set_current_time


def write(scripts):
    """
    写入脚本文件
    TODO: 加入SCREEN_SIZE
    :return:
    """
    device_info = ':DEVICE: {} {}'.format(
        platform.system(), platform.release()
    )
    scripts = [device_info, ':START'] + scripts + [':END']

    fp = codecs.open('test', 'w', 'utf-8')
    fp.write(' \n'.join(scripts))
    fp.close()


def record(start_key, end_key, exclude_events, destination, file, original, original_auto, is_continue):
    start_key = None if start_key is None else start_key
    end_key = 'Esc' if end_key is None else end_key
    exclude_events = [] if exclude_events is None else exclude_events
    destination = './' if destination is None else destination
    file = 'script' if file is None else file
    if not os.path.isdir(destination):
        print('destination not exists')
    original = (0, 0) if original is None else original
    original_auto = False if original_auto is None else original_auto
    is_continue = False if is_continue is None else is_continue

    set_current_time()
    listen(exclude_events)
    write(get_scripts())


def exec(start_key, end_key, file, is_auto_release):
    start_key = None if start_key is None else start_key
    end_key = 'Esc' if end_key is None else end_key
    is_auto_release = False if is_auto_release is None else is_auto_release

    fp = codecs.open('test', 'r', 'utf-8')
    scripts = [line.split(' ') for line in fp.readlines()]
    run(scripts)


def main():
    """
    自动release
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', help='打印版本信息')
    subparsers = parser.add_subparsers(dest='subparser')

    parser_record = subparsers.add_parser('record', help='记录脚本')
    parser_record.add_argument('-o', '--original', dest='original', help='初始坐标 (default: 0, 0)')
    parser_record.add_argument('-oa', '--original_auto', action='store_true', dest='original_auto', help='自动记录初始化坐标 (default: False)')
    parser_record.add_argument('-s', '--start_key', dest='start_key', help='开始记录快捷键 (default: None)')
    parser_record.add_argument('-e', '--end_key', dest='end_key', help='结束记录快捷键 (default: Esc')
    parser_record.add_argument('-ex', '--exclude_events', action='append', dest='exclude_events', help='排除事件 (default: [])')
    parser_record.add_argument('-d', '--destination', dest='destination', help='输出文件夹 (default: ./)')
    parser_record.add_argument('-f', '--file', dest='file', help='输出文件 (default: script')
    parser_record.add_argument('-c', '--continue', action='store_true', dest='is_continue', help='断点续记 (default: false)')

    parser_run = subparsers.add_parser('exec', help='执行脚本')
    parser_run.add_argument('-s', '--start_key', dest='start_key', help='开始执行快捷键 (default: None)')
    parser_run.add_argument('-e', '--end_key', dest='end_key', help='结束执行快捷键 (default: Esc')
    parser_run.add_argument('-f', '--file', dest='file', help='指定脚本文件执行 (default: script)')
    parser_run.add_argument('-ar', '--auto_release', action='store_true', dest='is_auto_release', help='自动释放按键 (default: false)')

    kwargs = vars(parser.parse_args())
    command = kwargs.pop('subparser')
    if command is None:
        parser.print_help()
        parser.exit()
    else:
        if os.geteuid() != 0:
            print('You must have the root privileges.')
            parser.exit()
        kwargs.pop('version')
        globals()[command](**kwargs)


if __name__ == '__main__':
    main()