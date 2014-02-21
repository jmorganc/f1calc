from f1calc.f1calc import F1Calculator
import bottle
import os


@bottle.hook('before_request')
def setup_request():
    points = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)
    drivers = ('Sebastian Vettel', 'Mark Webber', 'Fernando Alonso', 'Felipe Massa', 'Jenson Button', 'Sergio Perez', 'Kimi Raikkonen', 'Romain Grosjean', 'Nico Rosberg', 'Lewis Hamilton', 'Nico Hulkenberg', 'Esteban Gutierrez', 'Paul di Resta', 'Adrian Sutil', 'Pastor Maldonado', 'Valtteri Bottas', 'Jean-Eric Vergne', 'Daniel Ricciardo', 'Charles Pic', 'Giedo van der Garde', 'Jules Bianchi', 'Max Chilton')
    grandsprix = ('Australian GP', 'Malaysian GP', 'Chinese GP', 'Bahrain GP', 'Spanish GP', 'Monaco GP', 'Canadian GP', 'British GP', 'German GP', 'Hungarian GP', 'Belgian GP', 'Italian GP', 'Singapore GP', 'Korean GP', 'Japanese GP', 'Indian GP', 'Abu Dhabi GP', 'United States GP', 'Brazilian GP')

    global F1
    F1 = F1Calculator(points, drivers, grandsprix)

    # Clear out the JSON files of everything
    F1.reset_json()
    # Write out the points, drivers and grands prix to JSON on disk
    F1.save_all()

    # Australia
    # i.e. (first race, [kimi, fernando, sebastian, felipe, lewis, mark, adrian, paul, jenson, romain])
    F1.record_race(0, [6, 2, 0, 3, 9, 1, 13, 12, 4, 7])
    # Malaysia
    F1.record_race(1, [0, 1, 9, 8, 3, 7, 6, 10, 5, 16])
    # China
    F1.record_race(2, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # Bahrain
    F1.record_race(3, [0, 6, 7, 12, 9, 5, 1, 2, 8, 4])
    # Testing a bunch to calculate possibilities at the end of the season easier
    # F1.record_race(4, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(5, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(6, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(7, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(8, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(9, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(10, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(11, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(12, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(13, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(14, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(15, [6, 6, 2, 0, 4, 3, 17, 12, 7, 10])
    # F1.record_race(16, [6, 9, 2, 0, 4, 3, 17, 12, 7, 10])

    # Tally up the points
    F1.tally_points()


@bottle.route('/')
def index():
    return bottle.template('templates/index.tpl', drivers=F1.drivers, grandsprix=F1.grandsprix, drivers_order=F1.order_drivers())


@bottle.route('/static/<filename:path>')
def static(filename):
    return bottle.static_file(filename, root=os.path.normpath(os.getcwd() + '/static/'))


# Favicon
@bottle.route('/favicon.ico')
def favicon():
    return bottle.static_file('favicon.ico', root=os.path.normpath(os.getcwd()))


bottle.run(host = '', port = 8080)
