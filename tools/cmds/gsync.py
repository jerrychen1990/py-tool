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


def get_parser():
    parser = argparse.ArgumentParser(description='git sync current commits to remote repository')
    parser.add_argument('-m', '--message', type=str,
                        help='commit messages')
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    status_cmd = "git status"
    os.system(status_cmd)
    answer = input(["are you sure to commit all the changed files? [Y/N]"])
    if not answer.upper() == 'Y':
        return
    message = args.get("message", None)
    if not message:
        print("no commit message! use -m argument to input commit message")
        return
    add_cmd = "git add ."
    print("git adding")
    os.system(add_cmd)

    cmt_cmd = 'git commit -m "{}"'.format(message)
    print("git committing")
    os.system(cmt_cmd)

    push_cmd = "git push"
    print("git pushing")
    os.system(push_cmd)
    print("git sync finished")


if __name__ == '__main__':
    command_line_runner()
