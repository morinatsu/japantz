from nose.tools import *
from japantz import JapanTZ

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    jst = JapanTZ()
    
