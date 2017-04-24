#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/20/17 11:22 AM
# @Author  : xiaowa
import argparse
import app.lib.dateutil as dateutil
import os
import datetime
import subprocess


def get_parser():
    parser = argparse.ArgumentParser(description='history flush commandline tool')
    parser.add_argument('cmd', metavar='COMMAND', type=str,
                        help='the command to execute')
    parser.add_argument('start_day', metavar='START_DAY', type=str,
                        help='the start day')
    parser.add_argument('end_day', metavar='END_DAY', type=str,
                        help='the end day')

    return parser


def iter_cmd(start_day, end_day, cmd):
    print(start_day, end_day, cmd)
    start_date, start_format = dateutil.str2date(start_day)
    end_date, end_format = dateutil.str2date(end_day)
    if start_format != end_format:
        print(u"different date format between startDay and endDay!")
        return

    iter_date = start_date
    time_step = 1 if start_date < end_date else -1

    while iter_date != end_date:
        iter_day = dateutil.date2str(iter_date, end_format)
        execute_cmd(cmd, iter_day)
        iter_date += datetime.timedelta(time_step)


def execute_cmd(cmd, *args):
    cmd_list = [cmd]
    cmd_list.extend(args)
    print (u'executing "{} {}"'.format(cmd, args))
    out_put = subprocess.check_output(cmd_list).decode(u'utf8')
    print u'output\n{}'.format(out_put.strip())


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    print(args)
    iter_cmd(**args)


if __name__ == '__main__':
    command_line_runner()
