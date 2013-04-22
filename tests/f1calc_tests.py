from nose.tools import *
from f1calc.f1calc import FCalculator

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_vettel():
    assert_equal(drivers[0], 77)