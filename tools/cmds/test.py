#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/28/17 11:56 AM
# @Author  : xiaowa

import platform

version_str = platform.python_version()


def safe_print(msg, origin=False):
    to_print = safe_str(msg, origin=origin)
    print(to_print)


def safe_unicode(element):
    if version_str.startswith(u'3'):
        return safe_unicode_v3(element)


def safe_unicode_v3(element):
    if version_str.startswith(u'3'):
        return


def safe_str(element, origin=False, quote=False):
    version = platform.python_version()
    rs_str = "fail to safe_str"

    if version.startswith('3'):
        rs_str = str(element)
    else:
        if isinstance(element, unicode):
            rs_str = element.encode('utf8')
            if quotes:
                rs_str = "'" + rs_str + "'"
        elif isinstance(element, str):
            rs_str = element
            if quotes:
                rs_str = "'" + element + "'"
        elif isinstance(element, list):
            rs_str = "[" + ", ".join([safe_str(e, True) for e in element]) + "]"
        elif isinstance(element, tuple):
            rs_str = "(" + ", ".join([safe_str(e, True) for e in element]) + ")"
        elif isinstance(element, dict):
            def safe_str_kv(k, v):
                return ": ".join([safe_str(k, True), safe_str(v, True)])

            rs_str = "{" + ', '.join([safe_str_kv(k, v) for k, v in element.items()]) + "}"
        else:
            rs_str = str(element)

    return rs_str


def safe_unicode(element, quotes=False):
    version = platform.python_version()
    rs_str = "fail to safe_str"

    if version.startswith('3'):
        rs_str = str(element)
    else:
        if isinstance(element, unicode):
            rs_str = element.encode('utf8')
            if quotes:
                rs_str = "'" + rs_str + "'"
        elif isinstance(element, str):
            rs_str = element
            if quotes:
                rs_str = "'" + element + "'"
        elif isinstance(element, list):
            rs_str = "[" + ", ".join([safe_str(e, True) for e in element]) + "]"
        elif isinstance(element, tuple):
            rs_str = "(" + ", ".join([safe_str(e, True) for e in element]) + ")"
        elif isinstance(element, dict):
            def safe_str_kv(k, v):
                return ": ".join([safe_str(k, True), safe_str(v, True)])

            rs_str = "{" + ', '.join([safe_str_kv(k, v) for k, v in element.items()]) + "}"
        else:
            rs_str = str(element)

    return rs_str


def safe_format(msg, **kwargs):
    version = platform.python_version()
    if version.startswith('3'):
        str_dict = dict([(str(k), str(v)) for k, v in kwargs.items()])
        msg = str(msg).format(**kwargs)
        return msg
    else:
        if isinstance(msg, unicode):
            print(msg.encode('utf8'))
        else:
            print(msg)


a = '喆'
b = u'喆'
c = 1
d = [a, b, c]
e = {a: a, 1: b, "adfa": d}
f = (a, b, c)

safe_print(a)
safe_print(b)
safe_print(c)
safe_print(d)
safe_print(e)
safe_print(f)
