import os
import argparse

from pygui_macro.recoder import Recoder
from pygui_macro.runner import Runner


def main():
    """
    自动release
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', help='print version info')
    subparsers = parser.add_subparsers(dest='subparser')

    parser_record = subparsers.add_parser('record', help='record and generate macro script')
    parser_record.add_argument('-d', '--delay', dest='delay', help='delay time to record (default: 3)')
    parser_record.add_argument('-o', '--original', dest='original', help='original coordinate (default: 0, 0)')
    parser_record.add_argument('-oa', '--original_auto', action='store_true', dest='original_auto', help='set original coordinate automatically (default: False)')
    parser_record.add_argument('-e', '--end_key', dest='end_key', help='end record hot key (default: Esc')
    parser_record.add_argument('-ie', '--include_events', action='append', dest='include_events', help='which event be recorded (default: [])')
    parser_record.add_argument('-f', '--file', dest='file', help='macro script filename (default: script')
    parser_record.add_argument('-c', '--continue', action='store_true', dest='is_continue', help='continuee (default: false)')
    parser_record.add_argument('-ar', '--auto_release', action='store_true', dest='auto_release', help='whether auto release the key (default: true)')

    parser_run = subparsers.add_parser('run', help='run the macro script')
    parser_run.add_argument('-d', '--delay', dest='delay', help='delay time to run (default: 3)')
    parser_run.add_argument('-f', '--file', dest='file', help='specify the macro script filename (default: script)')

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
        elif command == 'run':
            Runner(**kwargs).handle()


if __name__ == '__main__':
    main()