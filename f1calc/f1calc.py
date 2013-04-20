points = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)
drivers = ('Sebastian Vettel', 'Mark Webber', 'Fernando Alonso', 'Felipe Massa', 'Jenson Button', 'Sergio Perez', 'Kimi Raikkonen', 'Romain Grosjean', 'Nico Rosberg', 'Lewis Hamilton', 'Nico Hulkenberg', 'Esteban Gutierrez', 'Paul di Resta', 'Adrian Sutil', 'Pastor Maldonado', 'Valtteri Bottas', 'Jean-Eric Vergne', 'Daniel Ricciardo', 'Charles Pic', 'Giedo van der Garde', 'Jules Bianchi', 'Max Chilton')
calendar = ('Australian GP', 'Malaysian GP', 'Chinese GP', 'Bahrain GP', 'Spanish GP', 'Monaco GP', 'Canadian GP', 'British GP', 'German GP', 'Hungarian GP', 'Belgian GP', 'Italian GP', 'Singapore GP', 'Korean GP', 'Japanese GP', 'Indian GP', 'Abu Dhabi GP', 'United States GP', 'Brazilian GP')

# The championship order
# This should change throughout the season
driver_order = []

# Initialize the race results for each grand prix
calendars_drivers = []
for gp in calendar:
    calendars_drivers.append([])

# Australia race results
calendars_drivers[0] = [6, 2, 0, 3, 9, 1, 13, 12, 4, 7]
# Malaysia race results
calendars_drivers[1] = [0, 1, 9, 8, 3, 7, 6, 10, 5, 16]
# China race results
calendars_drivers[2] = [2, 6, 9, 0, 4, 3, 17, 12, 7, 10]

# Make sure there are 10 drivers (points finishers)
# @TODO: The rare case that <10 drivers finish a race?
for index, gp in enumerate(calendars_drivers):
    if (len(gp) == 10):
        # Check to make sure there are no duplicates
        if (len(gp) == len(set(gp))):
            print calendar[index] + ': ' + str(gp)
        else:
            print 'Error! There is a duplicate driver'
    else:
        print 'Error! There are too (many|few) drivers'

# Initialize the points
# The index of drivers_points matches that of drivers
drivers_points = []
for driver in drivers:
    drivers_points.append(0)

for gp in calendars_drivers:
    for index, driver in enumerate(gp):
        drivers_points[driver] += points[index]
print 'Driver points: ' + str(drivers_points)






###################################################
###################################################
# First place in every race
max_points_possible = points[0] * len(calendar)
# print max_points_possible
# print drivers_points
