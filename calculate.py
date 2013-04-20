import json

points = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)
drivers = ('Sebastian Vettel', 'Mark Webber', 'Fernando Alonso', 'Felipe Massa', 'Jenson Button', 'Sergio Perez', 'Kimi Raikkonen', 'Romain Grosjean', 'Nico Rosberg', 'Lewis Hamilton', 'Nico Hulkenberg', 'Esteban Gutierrez', 'Paul di Resta', 'Adrian Sutil', 'Pastor Maldonado', 'Valtteri Bottas', 'Jean-Eric Vergne', 'Daniel Ricciardo', 'Charles Pic', 'Giedo van der Garde', 'Jules Bianchi', 'Max Chilton')
grandsprix = ('Australian GP', 'Malaysian GP', 'Chinese GP', 'Bahrain GP', 'Spanish GP', 'Monaco GP', 'Canadian GP', 'British GP', 'German GP', 'Hungarian GP', 'Belgian GP', 'Italian GP', 'Singapore GP', 'Korean GP', 'Japanese GP', 'Indian GP', 'Abu Dhabi GP', 'United States GP', 'Brazilian GP')
# The championship order which should change throughout the season
drivers_order = []
#
drivers_points = []
# Still in the running for the championship
drivers_eligible = []
# Mathematically impossible to win the championship
drivers_ineligible = []
drivers_json = json.loads(open('drivers.json', 'r').read())
grandsprix_json = json.loads(open('grandsprix.json', 'r').read())


#
# def save_drivers():
#     for driver in drivers:
#         if not driver in drivers_json:
#             drivers_json[driver] = {}
#         for gp in grandsprix:
#             if not gp in drivers_json[driver]:
#                 drivers_json[driver][gp] = 0
#     open('drivers.json', 'w').write(json.dumps(drivers_json, indent=4, sort_keys=True))
# save_drivers()
def save_drivers():
    for driver_index, driver in enumerate(drivers):
        while len(drivers_json) < len(drivers):
            drivers_json.append([])
        for gp_index, gp in enumerate(grandsprix):
            while len(drivers_json[driver_index]) < len(grandsprix):
                drivers_json[driver_index].append(0)
    open('drivers.json', 'w').write(json.dumps(drivers_json, indent=4, sort_keys=True))
save_drivers()


#
# def save_grandsprix():
#     for gp in grandsprix:
#         if not gp in grandsprix_json:
#             grandsprix_json[gp] = {}
#         for driver in drivers:
#             if not driver in grandsprix_json[gp]:
#                 grandsprix_json[gp][driver] = 0
#     open('grandsprix.json', 'w').write(json.dumps(grandsprix_json, indent=4, sort_keys=True))
# save_grandsprix()
def save_grandsprix():
    for gp_index, gp in enumerate(grandsprix):
        while len(grandsprix_json) < len(grandsprix):
            grandsprix_json.append([])
        for driver_index, driver in enumerate(drivers):
            while len(grandsprix_json[gp_index]) < len(drivers):
                grandsprix_json[gp_index].append(0)
    open('grandsprix.json', 'w').write(json.dumps(grandsprix_json, indent=4, sort_keys=True))
save_grandsprix()


#
# def record_race(circuit, points_finishers):
#     for place, driver_id in enumerate(points_finishers):
#         grandsprix_json[grandsprix[circuit]][drivers[driver_id]] = points[place]
#         drivers_json[drivers[driver_id]][grandsprix[circuit]] = points[place]
#     save_grandsprix()
#     save_drivers()
# record_race(0, [6, 2, 0, 3, 9, 1, 13, 12, 4, 7])
# record_race(1, [0, 1, 9, 8, 3, 7, 6, 10, 5, 16])
# record_race(2, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
def record_race(circuit, points_finishers):
    for place, driver_id in enumerate(points_finishers):
        drivers_json[driver_id][circuit] = points[place]
        grandsprix_json[circuit][driver_id] = points[place]
    save_drivers()
    save_grandsprix()
record_race(0, [6, 2, 0, 3, 9, 1, 13, 12, 4, 7])
record_race(1, [0, 1, 9, 8, 3, 7, 6, 10, 5, 16])
record_race(2, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])


# Initialize
for driver in drivers:
    drivers_points.append(0)


#
def tally_points():
    for driver_id, driver in enumerate(drivers_json):
        for gp_id, gp in enumerate(drivers_json[driver]):
            drivers_points[driver_id] += gp
tally_points()
print drivers_points










###################################################
###################################################
# First place in every race
max_points_possible = points[0] * len(grandsprix)
# print max_points_possible
# print drivers_points
