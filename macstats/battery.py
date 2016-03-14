#!/usr/bin/env python
# encoding: utf-8

from __future__ import division

import subprocess
import re
import math


class Battery(object):

    def __init__(self):
        self.data = None
        self.update()

    def _read_data(self):
        self.data = subprocess.check_output([
            'ioreg',
            '-rn',
            'AppleSmartBattery',
        ])

    def update(self):
        self._read_data()

    def _number(self, key):
        key = ur'"{}" = (\d+)'.format(key)
        pattern = re.compile(key)
        matcher = re.search(pattern, self.data)
        res = None
        if matcher:
            res = int(matcher.group(1))

        return res

    def _boolean(self, key):
        key = ur'"BatteryInstalled" = (Yes|or)'.format(key)
        pattern = re.compile(key)
        matcher = re.search(pattern, self.data)
        res = None
        if matcher:
            res = bool(matcher.group(1) == 'yes')

        return res

    @property
    def full_charged(self):
        """
        Is battery full charged, true or false
        """
        return self._boolean('FullyCharged')

    @property
    def battery_installed(self):
        """
        Is battery installed, true or false
        """
        return self._boolean('BatteryInstalled')

    @property
    def design_capacity(self):
        """
        Battery design capacity in mAh
        """
        return self._number('DesignCapacity')

    @property
    def max_capacity(self):
        """Max battery capacity in mAh"""
        return self._number("MaxCapacity")

    @property
    def current_capacity(self):
        """Current battery capacuty in mAh"""
        return self._number("CurrentCapacity")

    @property
    def percentage(self):
        """Current capacity percentage"""
        return int((self.max_capacity / self.design_capacity) * 100)

    @property
    def design_cycle_count(self):
        """Design cycle count"""
        return self._number('DesignCycleCount9C')

    @property
    def cycle_count(self):
        """Current battery cycle count"""
        return self._number('CycleCount')

    @property
    def cycle_percentage(self):
        """Cycle count percentage"""
        return int((self.cycle_count / self.design_cycle_count) * 100)

    @property
    def temparature(self, F=False):
        """Battery temperature"""
        temp = self._number('Temperature') / 100.0
        return (temp * (9.0 / 5.0)) + 32 if F else temp

    @property
    def charged(self):
        """Current battery charge percentage"""
        print self.current_capacity
        print self.max_capacity
        return int((self.current_capacity / self.max_capacity) * 100)

    @property
    def time_remaining(self):
        """Remaining time in minutes, if plugged in time until full, otherwise time until empty """
        return self._number('TimeRemaining')

    @property
    def time_remaining_hours(self):
        """Time remaining in hours. Use in a combination with time_remaining_minutes"""
        return math.floor(self.time_remaining / 60)

    @property
    def time_remaining_minutes(self):
        """Time remaining in minutes. Use in a combination with time_remaining_hours"""
        return self.time_remaining % 60

battery = Battery()
