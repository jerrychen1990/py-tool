#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/21/17 6:08 PM
# @Author  : xiaowa

from setuptools import setup, find_packages
import tools

long_description = """ xiaowa's python tools """

setup(
        name='bigdata-tools',
        version=tools.__version__,
        description='history-flush',
        long_description=long_description,
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Topic :: Documentation",
        ],
        keywords='py-tool',
        author='jerrychen',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'history-flush = tools.cmds.history_flush:command_line_runner',
                'kafka-produce = tools.cmds.kafka_produce:command_line_runner'
            ]
        },
        install_requires=[
        ]
)
