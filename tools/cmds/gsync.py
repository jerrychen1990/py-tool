#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/22/17 11:09 AM
# @Author  : xiaowa


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/17 6:19 PM
# @Author  : xiaowa


import argparse
import os
import sys

DEFAULT_MESSAGE = u'sync'

def get_parser():
    parser = argparse.ArgumentParser(description='git sync current commits to remote repository')
    parser.add_argument('-m', '--message', type=str,
                        help='commit messages')
    parser.add_argument('-f', '--force', type=str,
                        help='force commit, use default message=sync')
    return parser


def do_execute(cmd):
    rs = os.system(cmd)
    if rs != 0:
        print("fail to execute {}".format(cmd))
        sys.exit(-1)


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    status_cmd = "git status"
    do_execute(status_cmd)

    is_force = args.get("force", None)
    if not is_force:
        answer = input(["are you sure to commit all the changed files? [Y/N]"])
        if not answer.upper() == 'Y':
            return
        message = args.get("message", None)
        if not message:
            print("no commit message! use -m argument to input commit message")
            return
    message = args.get("message", DEFAULT_MESSAGE)

    add_cmd = "git add ."
    print("git adding")
    do_execute(add_cmd)


    cmt_cmd = 'git commit -m "{}"'.format(message)
    print("git committing")
    do_execute(cmt_cmd)


    push_cmd = "git push"
    print("git pushing")
    do_execute(push_cmd)


    print("git sync finished")


if __name__ == '__main__':
    command_line_runner()

    # rs = os.system("git push")
    # print(rs)