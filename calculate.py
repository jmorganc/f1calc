import json

points = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)
drivers = ('Sebastian Vettel', 'Mark Webber', 'Fernando Alonso', 'Felipe Massa', 'Jenson Button', 'Sergio Perez', 'Kimi Raikkonen', 'Romain Grosjean', 'Nico Rosberg', 'Lewis Hamilton', 'Nico Hulkenberg', 'Esteban Gutierrez', 'Paul di Resta', 'Adrian Sutil', 'Pastor Maldonado', 'Valtteri Bottas', 'Jean-Eric Vergne', 'Daniel Ricciardo', 'Charles Pic', 'Giedo van der Garde', 'Jules Bianchi', 'Max Chilton')
grandsprix = ('Australian GP', 'Malaysian GP', 'Chinese GP', 'Bahrain GP', 'Spanish GP', 'Monaco GP', 'Canadian GP', 'British GP', 'German GP', 'Hungarian GP', 'Belgian GP', 'Italian GP', 'Singapore GP', 'Korean GP', 'Japanese GP', 'Indian GP', 'Abu Dhabi GP', 'United States GP', 'Brazilian GP')
# The championship order which should change throughout the season
drivers_order = []
for driver in drivers:
    drivers_order.append(-1)
# How many points each driver currently has, unordered
drivers_points = []
# Still in the running for the championship (everyone at the beginning, thinning as the season progresses)
drivers_eligible = []
# Mathematically impossible to win the championship (empty at the beginning, filling as the season progresses)
drivers_ineligible = []
drivers_json = json.loads(open('drivers.json', 'r').read())
grandsprix_json = json.loads(open('grandsprix.json', 'r').read())
drivers_json_associative = json.loads(open('drivers_associative.json', 'r').read())
grandsprix_json_associative = json.loads(open('grandsprix_associative.json', 'r').read())


# Clear the JSON files
# def reset_json():
#     open('drivers.json', 'w').write('[]')
#     open('grandsprix.json', 'w').write('[]')
#     open('drivers_associative.json', 'w').write('{}')
#     open('grandsprix_associative.json', 'w').write('{}')
# reset_json()


# ASSOCIATIVE, NOT PLANNED TO USE
def save_drivers_associative():
    for driver in drivers:
        if not driver in drivers_json_associative:
            drivers_json_associative[driver] = {}
        for gp in grandsprix:
            if not gp in drivers_json_associative[driver]:
                drivers_json_associative[driver][gp] = 0
    open('drivers_associative.json', 'w').write(json.dumps(drivers_json_associative, indent=4, sort_keys=True))
save_drivers_associative()
#
def save_drivers():
    for driver_index, driver in enumerate(drivers):
        while len(drivers_json) < len(drivers):
            drivers_json.append([])
        for gp_index, gp in enumerate(grandsprix):
            while len(drivers_json[driver_index]) < len(grandsprix):
                drivers_json[driver_index].append(0)
    open('drivers.json', 'w').write(json.dumps(drivers_json, indent=4, sort_keys=True))
save_drivers()


# ASSOCIATIVE, NOT PLANNED TO USE
def save_grandsprix_associative():
    for gp in grandsprix:
        if not gp in grandsprix_json_associative:
            grandsprix_json_associative[gp] = {}
        for driver in drivers:
            if not driver in grandsprix_json_associative[gp]:
                grandsprix_json_associative[gp][driver] = 0
    open('grandsprix_associative.json', 'w').write(json.dumps(grandsprix_json_associative, indent=4, sort_keys=True))
save_grandsprix_associative()
#
def save_grandsprix():
    for gp_index, gp in enumerate(grandsprix):
        while len(grandsprix_json) < len(grandsprix):
            grandsprix_json.append([])
        for driver_index, driver in enumerate(drivers):
            while len(grandsprix_json[gp_index]) < len(drivers):
                grandsprix_json[gp_index].append(0)
    open('grandsprix.json', 'w').write(json.dumps(grandsprix_json, indent=4, sort_keys=True))
save_grandsprix()


# ASSOCIATIVE, NOT PLANNED TO USE
def record_race_associative(circuit, points_finishers):
    for place, driver_id in enumerate(points_finishers):
        grandsprix_json_associative[grandsprix[circuit]][drivers[driver_id]] = points[place]
        drivers_json_associative[drivers[driver_id]][grandsprix[circuit]] = points[place]
    save_grandsprix_associative()
    save_drivers_associative()
#
def record_race(circuit, points_finishers):
    for place, driver_id in enumerate(points_finishers):
        drivers_json[driver_id][circuit] = points[place]
        grandsprix_json[circuit][driver_id] = points[place]
    save_drivers()
    save_grandsprix()
    record_race_associative(circuit, points_finishers)
# Australia
record_race(0, [6, 2, 0, 3, 9, 1, 13, 12, 4, 7])
# Malaysia
record_race(1, [0, 1, 9, 8, 3, 7, 6, 10, 5, 16])
# China
record_race(2, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# Testing
# record_race(3, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# record_race(4, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# record_race(5, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# record_race(6, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# record_race(7, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# record_race(8, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# record_race(9, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# record_race(10, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# record_race(11, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# record_race(12, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])


# Initialize
for driver in drivers:
    drivers_points.append(0)


#
def tally_points():
    for driver_id, driver in enumerate(drivers_json):
        for gp_id, gp in enumerate(drivers_json[driver_id]):
            drivers_points[driver_id] += gp
    print drivers_points
tally_points()


#
# def order_drivers():
#     for driver_id, points in enumerate(drivers_points):
#         drivers_order[driver_id] = points
# def order_drivers():
#     drivers_order = drivers_points
#     for driver_id, points in enumerate(drivers_order):
#         lowest_points = min(drivers_order[driver_id:])
#         lowest_index = drivers_order[driver_id:].index(lowest_points)
#         drivers_order[driver_id + lowest_index] = drivers_order[driver_id]
#         drivers_order[driver_id] = lowest_points
#     print drivers_order
def order_drivers(local_drivers_points):
    for i, points in enumerate(local_drivers_points):
        if points > drivers_order[i]:
            pass
order_drivers(drivers_points)


# Return the place in the championship of the provided driver
def driver_place(driver):
    pass


# Return the driver in the provided place in the championship
def place_driver(place):
    pass






###################################################
###################################################
# First place in every race
max_points_possible = points[0] * len(grandsprix)
# print max_points_possible
# print drivers_points
