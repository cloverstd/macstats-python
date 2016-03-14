#!/usr/bin/env python
# encoding: utf-8

from . import _smc


class Fan(object):

    @property
    def number(self):
        return _smc.fan_number()

    @property
    def fans(self):
        res = []
        for i in xrange(self.number):
            res.append({
                'id': i,
                'rpm': _smc.fan_RPM(i)
            })

        return res


fan = Fan()
