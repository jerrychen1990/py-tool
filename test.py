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
    # a = [
    #     26005364,
    #     26007279,
    #     26008308,
    #     26008322,
    #     26008348,
    #     26008364,
    #     26008376,
    #     26008380,
    #     26008427,
    #     26008428,
    #     26008433,
    #     26008444,
    #     26008491,
    #     26008514,
    #     26008532,
    #     26008546,
    #     26008559,
    #     26014294,
    #     26018485,
    #     26025421,
    #     26031138,
    #     26032279]
    #
    #
    # pattern = u'curl https://www.youzan.com/v2/dsp/gg/del.json?id={id}&csrf_token=70286900849083418882278281217843215489591277022955783116166974206776022468802'
    #
    # for tmp in a:
    #     cmd = pattern.format(id=tmp)
    #     print cmd
    #     os.system(cmd)
    #


    import codecs
    import os
    # url_pattern = u"curl -get 10.10.93.195:7001/dsp/agency/add_white_list?kdt_id={kdt_id}&platform=GDT"
    idx = 0
    url_pattern = "insert into white_list(kdt_id, platform) values({kdt_id}, 1);"

    with codecs.open("/Users/jerry/Desktop/test.csv", "r", "utf8") as f:
        for line in f:
            line = line.strip()
            kdt_id, _, _, _, _ = line.split(u",")
            # print kdt_id
            cmd = url_pattern.format(kdt_id=kdt_id)
            print(cmd)
            # os.system(cmd.encode('utf8'))
            idx += 1
            # if idx > 2:
            #     break
            # break


            # print(line)










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
