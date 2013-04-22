import json

class F1Calculator(object):

    points = ()
    drivers = ()
    grandsprix = ()
    max_points_possible = 0

    # The championship order which should change throughout the season
    drivers_order = []
    # How many points each driver currently has, unordered
    drivers_points = []
    #
    drivers_points_finishes = []
    # Still in the running for the championship (everyone at the beginning, thinning as the season progresses)
    drivers_eligible = []
    # Mathematically impossible to win the championship (empty at the beginning, filling as the season progresses)
    drivers_ineligible = []

    drivers_json = []
    grandsprix_json = []
    drivers_json_associative = {}
    grandsprix_json_associative = {}

    # Constructor
    def __init__(self, points, drivers, grandsprix):
        self.points = points
        self.drivers = drivers
        self.grandsprix = grandsprix
        # First place in every race
        self.max_points_possible = points[0] * len(grandsprix)

        self.drivers_json = json.loads(open('drivers.json', 'r').read())
        self.grandsprix_json = json.loads(open('grandsprix.json', 'r').read())
        self.drivers_json_associative = json.loads(open('drivers_associative.json', 'r').read())
        self.grandsprix_json_associative = json.loads(open('grandsprix_associative.json', 'r').read())

        # Initialize
        for driver in self.drivers:
            self.drivers_points.append(0)
            self.drivers_points_finishes.append(0)
            self.drivers_order.append(-1)


    # Clear the JSON files
    def reset_json(self):
        print 'Resetting JSON files... ',
        del(self.drivers_json[:])
        del(self.grandsprix_json[:])
        self.drivers_json_associative.clear()
        self.grandsprix_json_associative.clear()
        open('drivers.json', 'w').write(json.dumps(self.drivers_json))
        open('grandsprix.json', 'w').write(json.dumps(self.grandsprix_json))
        open('drivers_associative.json', 'w').write(json.dumps(self.drivers_json_associative))
        open('grandsprix_associative.json', 'w').write(json.dumps(self.grandsprix_json_associative))
        print 'Reset.'


    # I'm Lazy
    def save_all(self):
        self.save_drivers_associative()
        self.save_drivers()
        self.save_grandsprix_associative()
        self.save_grandsprix()


    # Write each driver and their grands prix to JSON dictionary
    def save_drivers_associative(self):
        for driver in self.drivers:
            if not driver in self.drivers_json_associative:
                self.drivers_json_associative[driver] = {}
            for gp in self.grandsprix:
                if not gp in self.drivers_json_associative[driver]:
                    self.drivers_json_associative[driver][gp] = 0
        open('drivers_associative.json', 'w').write(json.dumps(self.drivers_json_associative, indent=4, sort_keys=True))


    # Write each driver and their grands prix to JSON list
    def save_drivers(self):
        for driver_index, driver in enumerate(self.drivers):
            while len(self.drivers_json) < len(self.drivers):
                self.drivers_json.append([])
            for gp_index, gp in enumerate(self.grandsprix):
                while len(self.drivers_json[driver_index]) < len(self.grandsprix):
                    self.drivers_json[driver_index].append(0)
        open('drivers.json', 'w').write(json.dumps(self.drivers_json, indent=4, sort_keys=True))


    # Write each grand prix and their drivers prix to JSON dictionary
    def save_grandsprix_associative(self):
        for gp in self.grandsprix:
            if not gp in self.grandsprix_json_associative:
                self.grandsprix_json_associative[gp] = {}
            for driver in self.drivers:
                if not driver in self.grandsprix_json_associative[gp]:
                    self.grandsprix_json_associative[gp][driver] = 0
        open('grandsprix_associative.json', 'w').write(json.dumps(self.grandsprix_json_associative, indent=4, sort_keys=True))


    # Write each grand prix and their drivers to JSON list
    def save_grandsprix(self):
        for gp_index, gp in enumerate(self.grandsprix):
            while len(self.grandsprix_json) < len(self.grandsprix):
                self.grandsprix_json.append([])
            for driver_index, driver in enumerate(self.drivers):
                while len(self.grandsprix_json[gp_index]) < len(self.drivers):
                    self.grandsprix_json[gp_index].append(0)
        open('grandsprix.json', 'w').write(json.dumps(self.grandsprix_json, indent=4, sort_keys=True))


    # Record race results to JSON dictionary
    def record_race_associative(self, circuit, points_finishers):
        for place, driver_id in enumerate(points_finishers):
            self.grandsprix_json_associative[self.grandsprix[circuit]][self.drivers[driver_id]] = self.points[place]
            self.drivers_json_associative[self.drivers[driver_id]][self.grandsprix[circuit]] = self.points[place]
        self.save_grandsprix_associative()
        self.save_drivers_associative()


    # Record race results to JSON list
    def record_race(self, circuit, points_finishers):
        for place, driver_id in enumerate(points_finishers):
            self.drivers_json[driver_id][circuit] = self.points[place]
            self.grandsprix_json[circuit][driver_id] = self.points[place]
        self.save_drivers()
        self.save_grandsprix()
        self.record_race_associative(circuit, points_finishers)


    # Tally up the points for each driver
    def tally_points(self):
        print 'tally_points' + "\n\t",
        for driver_id, driver in enumerate(self.drivers_json):
            for gp_id, gp in enumerate(self.drivers_json[driver_id]):
                self.drivers_points[driver_id] += gp
                if gp >= 1:
                    self.drivers_points_finishes[driver_id] += 1
        print str(self.drivers_points)


    # Return how many races the provided driver has scored points in
    def driver_number_races_in_points(self, driver = None):
        print 'driver_number_races_in_points(' + str(driver) + ')' + "\n\t",
        if driver is not None:
            # Check if integer index or string (full name)
            if isinstance(driver, int):
                print self.drivers[driver] + ': ' + str(self.drivers_points_finishes[driver])
                print "\t" + 'Total points: ' + str(self.drivers_points[driver])
            else:
                if driver in self.drivers:
                    print driver + ': ' + str(self.drivers_points_finishes[self.drivers.index(driver)])
                    print "\t" + 'Total points: ' + str(self.drivers_points[self.drivers.index(driver)])
                else:
                    print 'This is an unrecognized driver.'
        else:
            print 'Please specify a driver.'


    #
    # def order_drivers():
    #     for driver_id, points in enumerate(self.drivers_points):
    #         self.drivers_order[driver_id] = points
    # def order_drivers():
    #     drivers_order = self.drivers_points
    #     for driver_id, points in enumerate(self.drivers_order):
    #         lowest_points = min(self.drivers_order[driver_id:])
    #         lowest_index = self.drivers_order[driver_id:].index(lowest_points)
    #         drivers_order[driver_id + lowest_index] = self.drivers_order[driver_id]
    #         drivers_order[driver_id] = lowest_points
    #     print drivers_order
    
    # What I want to be happening here is...
    # Order the drivers_orders list with the id of the driver, from first in the championship to last
    # So a championship order of Alonso, Raikkonen, Vettel, Hamilton, Webber... would look like...
    # [2, 6, 0, 9, 1...]
    def order_drivers(self):
        print 'order_drivers'
        for i, points in enumerate(self.drivers_points):
            if points > self.drivers_order[i]:
                pass


    # Return the place in the championship of the provided driver
    def driver_place(self, driver):
        pass


    # Return the driver in the provided place in the championship
    def place_driver(self, place):
        pass