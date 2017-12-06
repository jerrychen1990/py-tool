#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/25/17 7:20 PM
# @Author  : xiaowa
# import sys
#
# args = sys.argv[1:]
#
# print("executing python, path = {}, args={}".format(sys.argv[0], args))
#
import sys, os

OLD_PATH = "/logs/binlog/trade_order_bill_create"
NEW_PATH = "/logs/binlog/ntc_order_create"

if __name__ == '__main__':
    tmp = [5856
,24
,45
,51
,65
,31
,7
,95
,35
,17
,99
,95
,94
,57
,57
,26]
    acc = 0
    for e in tmp:
        acc += e
        print(acc)




    # if len(sys.argv) != 2:
    #     print("invalid argv num")
    #     print("usage: order-grep order_no")
    #     sys.exit(-1)
    # order_no = sys.argv[1]
    # day = order_no[1:9]
    # hour = order_no[9:11]
    # day_slash = day[0:4] + "_" + day[4:6] + "_" + day[6:8]
    # old_path = "{base}/{day}/f3_{day_slash}_{hour}*.lzo".format(base=OLD_PATH, day=day, day_slash=day_slash, hour=hour)
    # cmd_pattern = "hadoop fs -cat {path} | lzop -cd | grep {order_no}"
    # old_cmd = cmd_pattern.format(path=old_path, order_no=order_no)
    # print(old_cmd)
    # os.system(old_cmd)
    #
    # new_path = "{base}/{day}/f2_{day_slash}_{hour}*.lzo".format(base=NEW_PATH, day=day, day_slash=day_slash, hour=hour)
    # new_cmd = cmd_pattern.format(path=new_path, order_no=order_no)
    # print(new_cmd)
    # os.system(old_cmd)
