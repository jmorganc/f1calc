from nose.tools import *
from f1calc.f1calc import F1Calculator


def setup():
    print "SETUP!"
    points = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)
    drivers = ('Sebastian Vettel', 'Mark Webber', 'Fernando Alonso', 'Felipe Massa', 'Jenson Button', 'Sergio Perez', 'Kimi Raikkonen', 'Romain Grosjean', 'Nico Rosberg', 'Lewis Hamilton', 'Nico Hulkenberg', 'Esteban Gutierrez', 'Paul di Resta', 'Adrian Sutil', 'Pastor Maldonado', 'Valtteri Bottas', 'Jean-Eric Vergne', 'Daniel Ricciardo', 'Charles Pic', 'Giedo van der Garde', 'Jules Bianchi', 'Max Chilton')
    grandsprix = ('Australian GP', 'Malaysian GP', 'Chinese GP', 'Bahrain GP', 'Spanish GP', 'Monaco GP', 'Canadian GP', 'British GP', 'German GP', 'Hungarian GP', 'Belgian GP', 'Italian GP', 'Singapore GP', 'Korean GP', 'Japanese GP', 'Indian GP', 'Abu Dhabi GP', 'United States GP', 'Brazilian GP')
    
    global F1
    F1 = F1Calculator(points, drivers, grandsprix)
    F1.reset_json()
    F1.save_all()


def teardown():
    print "TEAR DOWN!"
    F1.reset_json()


def test_basic():
    assert_equal(len(F1.drivers), 22)
    assert_equal(len(F1.grandsprix), 19)
