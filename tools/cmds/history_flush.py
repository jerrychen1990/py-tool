#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/20/17 11:22 AM
# @Author  : xiaowa
import argparse
import tools.lib.dateutil as dateutil
import os
import datetime
import subprocess


def get_parser():
    parser = argparse.ArgumentParser(description='history flush commandline tool')
    parser.add_argument('cmd', metavar='command', type=str,
                        help='the command to execute')
    parser.add_argument('-s', '--start_day', type=str,
                        help='the start day')
    parser.add_argument('-e', '--end_day', type=str,
                        help='the end day')
    parser.add_argument('-t', '--test', help='just print instead of execute cmds', action="store_true")

    parser.add_argument(dest='args', metavar='args', nargs='*', help='args for command except day')

    return parser


def iter_cmd(start_day, end_day, cmd, test, args):
    start_date, start_format = dateutil.str2date(start_day)
    end_date, end_format = dateutil.str2date(end_day)
    if start_format != end_format:
        print(u"different date format between startDay and endDay!")
        return

    iter_date = start_date
    time_step = 1 if start_date < end_date else -1

    while iter_date != end_date:
        iter_day = dateutil.date2str(iter_date, end_format)
        execute_cmd(args=args, day=iter_day, cmd=cmd, test=test)
        iter_date += datetime.timedelta(time_step)


def execute_cmd(args, cmd, day, test=False):
    cmd_list = [cmd, day]
    cmd_list.extend(args)
    print(u'executing {} with day={}, args:{}'.format(cmd, day, list(args)))
    print(" ".join(cmd_list))
    if not test:
        out_put = subprocess.check_output(cmd_list).decode(u'utf8')
        print('output\n{}'.format(out_put.strip()))


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    print(args)
    iter_cmd(**args)


if __name__ == '__main__':
    command_line_runner()
