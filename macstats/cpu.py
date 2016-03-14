#!/usr/bin/env python
# encoding: utf-8

from . import _smc


class CPU(object):

    @property
    def temp(self, F=False):
        _temp = _smc.temp()
        return (_temp * (9.0 / 5.0)) + 32.0 if F else _temp


cpu = CPU()
