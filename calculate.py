from f1calc.f1calc import F1Calculator


points = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)
drivers = ('Sebastian Vettel', 'Mark Webber', 'Fernando Alonso', 'Felipe Massa', 'Jenson Button', 'Sergio Perez', 'Kimi Raikkonen', 'Romain Grosjean', 'Nico Rosberg', 'Lewis Hamilton', 'Nico Hulkenberg', 'Esteban Gutierrez', 'Paul di Resta', 'Adrian Sutil', 'Pastor Maldonado', 'Valtteri Bottas', 'Jean-Eric Vergne', 'Daniel Ricciardo', 'Charles Pic', 'Giedo van der Garde', 'Jules Bianchi', 'Max Chilton')
grandsprix = ('Australian GP', 'Malaysian GP', 'Chinese GP', 'Bahrain GP', 'Spanish GP', 'Monaco GP', 'Canadian GP', 'British GP', 'German GP', 'Hungarian GP', 'Belgian GP', 'Italian GP', 'Singapore GP', 'Korean GP', 'Japanese GP', 'Indian GP', 'Abu Dhabi GP', 'United States GP', 'Brazilian GP')

F1 = F1Calculator(points, drivers, grandsprix)


# Clear out the JSON files of everything
F1.reset_json()
F1.save_all()


# Australia
F1.record_race(0, [6, 2, 0, 3, 9, 1, 13, 12, 4, 7])
# Malaysia
F1.record_race(1, [0, 1, 9, 8, 3, 7, 6, 10, 5, 16])
# China
F1.record_race(2, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# Bahrain
F1.record_race(3, [0, 6, 7, 12, 9, 5, 1, 2, 8, 4])
# Testing a bunch to calculate possibilities at the end of the season easier
# So obviously Fernando Alonso (2) should win
F1.record_race(4, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(5, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(6, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(7, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(8, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(9, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(10, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(11, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(12, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(13, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(14, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(15, [6, 6, 2, 0, 4, 3, 17, 12, 7, 10])
F1.record_race(16, [6, 9, 2, 0, 4, 3, 17, 12, 7, 10])

# [233, 32, 352, 134, 143, 10, 308, 52, 14, 233, 18, 0, 72, 6, 0, 0, 1, 84, 0, 0, 0, 0]
#   So, just to start thinking about this...
#       Fernando currently has 352 points
#           Let's pretend he doesn't finish the last two races
#               Who is in second place? If they win the last two races, do they have a chance?
#                   Kimi is in second, with 308 points. If he wins the next two, he will have 358, winning
#                       This is just one possible permutation between only two drivers.


F1.tally_points()
F1.driver_number_races_in_points(0)
F1.driver_number_races_in_points("Fernando Alonso")
F1.driver_number_races_in_points("Morgan Campbell")
F1.order_drivers()
# What place is driver 9 (Lewis Hamilton) in?
print F1.driver_place(9)
# Who is in 12th place?
print F1.place_driver(12)
