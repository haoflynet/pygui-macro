"""
主要命令

以后的todo，但是也只能手动编辑
if语句、while语句
"""
import os
import argparse

from listener import listen
from callbacks import get_scripts


scripts = ['tst']

# def write():
#     """
#     写入脚本文件
#     :return:
#     """
#     device_info = 'DEVICE: {} {}'.format(
#         platform.system(), platform.release()
#     )
#     screen_info = 'SCREEN_SIZE: {}'.format(
#         ''  # 我擦，这个都跟系统有关
#     )


def record(start_key, end_key, exclude_events, destination, file, is_continue):
    start_key = None if start_key is None else start_key
    end_key = 'Esc' if end_key is None else end_key
    exclude_events = [] if exclude_events is None else exclude_events
    destination = './' if destination is None else destination
    file = 'script' if file is None else file
    if not os.path.isdir(destination):
        print('destination not exists')
    is_continue = False if is_continue is None else is_continue

    listen(exclude_events)
    print(get_scripts())



def run(start_key, end_key, file):
    start_key = None if start_key is None else start_key
    end_key = 'Esc' if end_key is None else end_key


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', help='打印版本信息')
    subparsers = parser.add_subparsers(dest='subparser')

    parser_record = subparsers.add_parser('record', help='记录脚本')
    parser_record.add_argument('-s', '--start_key', dest='start_key', help='开始记录快捷键 (default: None)')
    parser_record.add_argument('-e', '--end_key', dest='end_key', help='结束记录快捷键 (default: Esc')
    parser_record.add_argument('-ex', '--exclude_events', action='append', dest='exclude_events', help='排除事件 (default: [])')
    parser_record.add_argument('-d', '--destination', dest='destination', help='输出文件夹 (default: ./)')
    parser_record.add_argument('-f', '--file', dest='file', help='输出文件 (default: script')
    parser_record.add_argument('-c', '--continue', action='store_true', dest='is_continue', help='断点续记 (default: false)')

    parser_run = subparsers.add_parser('run', help='执行脚本')
    parser_run.add_argument('-s', '--start_key', dest='start_key', help='开始执行快捷键 (default: None)')
    parser_run.add_argument('-e', '--end_key', dest='end_key', help='结束执行快捷键 (default: Esc')
    parser_run.add_argument('-f', '--file', dest='file', help='指定脚本文件执行 (default: script)')

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