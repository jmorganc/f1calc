import bottle
import os


@bottle.route('/')
def index():
    print "index"


@bottle.route('/static/<filename:path>')
def static(filename):
    return bottle.static_file(filename, root=os.path.normpath(os.getcwd() + '/static/'))


bottle.run(host = '', port = 8080)
