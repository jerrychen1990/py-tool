#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/21/17 3:41 PM
# @Author  : xiaowa

from datetime import datetime

INT_FORMAT = u'%Y%m%d'
HYPHEN_FORMAT = u'%Y-%m-%d'


def str2date(date_str):
    # try INT_FORMAT
    try:
        rs_date = datetime.strptime(date_str, INT_FORMAT)
        return rs_date, INT_FORMAT
    except ValueError as e:
        try:
            rs_date = datetime.strptime(date_str, HYPHEN_FORMAT)
            return rs_date, HYPHEN_FORMAT

        except ValueError as e:
            raise ValueError(u"can't parse arg {}".format(date_str))



def date2str(d, fmt):
    return datetime.strftime(d, fmt)
