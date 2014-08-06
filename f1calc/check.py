#!/usr/bin/python

points = (0, 25, 18, 15, 12, 10, 8, 6, 4, 2, 1)
drivers = {
    #'Nico Rosberg': (1, 2, 2, 2, 2, 1, 2, 1, 0, 1, 4),
    #'Lewis Hamilton': (0, 1, 1, 1, 1, 2, 0, 2, 1, 3, 3),
    #'Daniel Ricciardo': (0, 0, 4, 4, 3, 3, 1, 8, 3, 6, 1)
    'Nico Rosberg': (1, 2, 2, 2, 2, 1, 2, 1, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0),
    'Lewis Hamilton': (0, 1, 1, 1, 1, 2, 0, 2, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
    'Daniel Ricciardo': (0, 0, 4, 4, 3, 3, 1, 8, 3, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1)
}

for driver in drivers:
    print driver
    points_total = 0
    
    race_num = 1
    for place in drivers[driver]:
        multiplier = 1
        if race_num == 19:
            multiplier = 2
        points_total += points[place] * multiplier
        print '\t', race_num, place, points[place], points_total
        race_num += 1
    print ''

