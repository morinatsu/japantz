#  -*- coding: utf-8 -*-
"""
japantz : Japan TzimeZone

"""
from datetime import tzinfo, timedelta, datetime


class JapanTZ(tzinfo):
    """Japan TimeZone"""
    def __init__(self):
        self.stdname = "JST"
        self.offset = timedelta(hours=9)
        self.dstoffset = timedelta(0)

    def tzname(self, dat):
        """name of timezone"""
        return self.stdname

    def utcoffset(self, dat):
        """offset from utc"""
        return self.offset

    def dst(self, dat):
        """timedelta of dst offset"""
        return self.dstoffset
