#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup, Extension
setup(
    name='macstats',
    version='0.1',
    packages=['macstats'],
    ext_modules=[
        Extension(
            'macstats._smc',
            sources=['macstats/_smc.c'],
            extra_link_args=['-framework', 'IOKit']
        )
    ]
)
