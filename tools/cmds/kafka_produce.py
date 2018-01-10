#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/21/17 6:19 PM
# @Author  : xiaowa


from kafka import KafkaProducer
from kafka.errors import KafkaError
import argparse
import codecs

import numpy as np

np.random


def send_message(topic, message, server):
    if not server:
        server = "127.0.0.1:9092"
    producer = KafkaProducer(bootstrap_servers=[server])
    # print(type(message))
    if type(message) == str:
        message = message.encode("utf8")

    future = producer.send(topic, key=topic.encode("utf8"), value=message)

    try:
        future.get(timeout=10)
        print("message:{} sent".format(message))
    except KafkaError as e:
        print(e)


def do_produce(topic, file, expression, server, **kwargs):
    if not expression:
        content = codecs.open(file, "r", "utf8").read()
        message_list = content.split(u"\n")
        for message in message_list:
            send_message(server=server, topic=topic, message=message)
    else:
        send_message(server=server, topic=topic, message=expression)



def get_parser():
    parser = argparse.ArgumentParser(description='kafka produce')
    # parser.add_argument('cmd', metavar='command', type=str,
    #                     help='the command to execute\nproduce/consume')
    parser.add_argument('-s', '--server', type=str,
                        help='the kafka boot_strap address')

    parser.add_argument('-t', '--topic', type=str,
                        help='the kafka topic')
    parser.add_argument('-f', '--file', type=str,
                        help='the message file')
    parser.add_argument('-e', '--expression', type=str,
                        help='the message')

    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    do_produce(**args)


if __name__ == '__main__':
    command_line_runner()
