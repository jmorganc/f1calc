import json

points = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)
drivers = ('Sebastian Vettel', 'Mark Webber', 'Fernando Alonso', 'Felipe Massa', 'Jenson Button', 'Sergio Perez', 'Kimi Raikkonen', 'Romain Grosjean', 'Nico Rosberg', 'Lewis Hamilton', 'Nico Hulkenberg', 'Esteban Gutierrez', 'Paul di Resta', 'Adrian Sutil', 'Pastor Maldonado', 'Valtteri Bottas', 'Jean-Eric Vergne', 'Daniel Ricciardo', 'Charles Pic', 'Giedo van der Garde', 'Jules Bianchi', 'Max Chilton')
grandsprix = ('Australian GP', 'Malaysian GP', 'Chinese GP', 'Bahrain GP', 'Spanish GP', 'Monaco GP', 'Canadian GP', 'British GP', 'German GP', 'Hungarian GP', 'Belgian GP', 'Italian GP', 'Singapore GP', 'Korean GP', 'Japanese GP', 'Indian GP', 'Abu Dhabi GP', 'United States GP', 'Brazilian GP')
# The championship order which should change throughout the season
driver_order = []
# Still in the running for the championship
drivers_eligible = []
# Mathematically impossible to win the championship
drivers_ineligible = []
drivers_json = json.loads(open('drivers.json', 'r').read())
grandsprix_json = json.loads(open('grandsprix.json', 'r').read())


#
def save_drivers(drivers, grandsprix, drivers_json):
    # drivers_json = json.loads(open('drivers.json', 'r').read())
    for driver in drivers:
        if not driver in drivers_json:
            drivers_json[driver] = {}
        for gp in grandsprix:
            if not gp in drivers_json[driver]:
                drivers_json[driver][gp] = 0
    open('drivers.json', 'w').write(json.dumps(drivers_json, indent=4, sort_keys=True))
save_drivers(drivers, grandsprix, drivers_json)


#
def save_grandsprix(grandsprix, drivers, grandsprix_json):
    # grandsprix_json = json.loads(open('grandsprix.json', 'r').read())
    for gp in grandsprix:
        if not gp in grandsprix_json:
            grandsprix_json[gp] = {}
        for driver in drivers:
            if not driver in grandsprix_json[gp]:
                grandsprix_json[gp][driver] = 0
    open('grandsprix.json', 'w').write(json.dumps(grandsprix_json, indent=4, sort_keys=True))
save_grandsprix(grandsprix, drivers, grandsprix_json)


#
def record_race(contest, points_finishers, grandsprix_json, grandsprix, drivers):
    for place, driver_id in enumerate(points_finishers):
        grandsprix_json[grandsprix[contest]][drivers[driver_id]] = points[place]
    save_grandsprix(grandsprix, drivers, grandsprix_json)
record_race(1, [0, 1, 9, 8, 3, 7, 6, 10, 5, 16], grandsprix_json, grandsprix, drivers)


# # Malaysia race results
# calendars_drivers[1] = [0, 1, 9, 8, 3, 7, 6, 10, 5, 16]
# # China race results
# calendars_drivers[2] = [2, 6, 9, 0, 4, 3, 17, 12, 7, 10]

# @TODO: The rare case that <10 drivers finish a race?
# @TODO: Data validation: No duplicate drivers
grandsprix_json = json.loads(open('grandsprix.json', 'r').read())
for gp in grandsprix_json:
    print 'GRAND PRIX: ' + gp
    for driver in grandsprix_json[gp]:
        print driver + ': ' + str(grandsprix_json[gp][driver])

# Initialize the points
# The index of drivers_points matches that of drivers
drivers_points = []
for driver in drivers:
    drivers_points.append(0)

# for gp in calendars_drivers:
#     for index, driver in enumerate(gp):
#         drivers_points[driver] += points[index]
# print 'Driver points: ' + str(drivers_points)






###################################################
###################################################
# First place in every race
max_points_possible = points[0] * len(grandsprix)
# print max_points_possible
# print drivers_points
