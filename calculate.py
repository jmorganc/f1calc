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
# Testing
# F1.record_race(4, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# F1.record_race(5, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# F1.record_race(6, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# F1.record_race(7, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# F1.record_race(8, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# F1.record_race(9, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# F1.record_race(10, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# F1.record_race(11, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])
# F1.record_race(12, [2, 6, 9, 0, 4, 3, 17, 12, 7, 10])


F1.tally_points()
F1.driver_number_races_in_points(0)
F1.driver_number_races_in_points("Fernando Alonso")
F1.driver_number_races_in_points("Morgan Campbell")
F1.order_drivers()
