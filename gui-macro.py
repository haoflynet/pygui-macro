"""
TODO： 手动编辑、if语句、while语句
"""
import os
import argparse

from recoder import Recoder
from runner import Runner


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
    parser_record.add_argument('-ex', '--include_events', action='append', dest='include_events', help='需要记录事件 (default: [])')
    parser_record.add_argument('-d', '--destination', dest='destination', help='输出文件夹 (default: ./)')
    parser_record.add_argument('-f', '--file', dest='file', help='输出文件 (default: script')
    parser_record.add_argument('-c', '--continue', action='store_true', dest='is_continue', help='断点续记 (default: false)')

    parser_run = subparsers.add_parser('exec', help='执行脚本')
    parser_run.add_argument('-s', '--start_key', dest='start_key', help='开始执行快捷键 (default: None)')
    parser_run.add_argument('-e', '--end_key', dest='end_key', help='结束执行快捷键 (default: Esc')
    parser_run.add_argument('-f', '--file', dest='file', help='指定脚本文件执行 (default: script)')
    parser_run.add_argument('-ar', '--auto_release', action='store_true', dest='is_auto_release', help='自动释放按键 (default: true)')

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
        if command == 'record':
            Recoder(**kwargs).handle()
        elif command == 'exec':
            Runner(**kwargs).handle()


if __name__ == '__main__':
    main()