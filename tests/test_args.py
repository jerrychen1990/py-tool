#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/26/17 10:58 AM
# @Author  : xiaowa


def sum(**kwargs):
    print(kwargs)

    for k, v in kwargs.items():
        print(k, v)


tmp_dict = {"a": 1,
            "b": "S"}

sum(**tmp_dict)
