class FCalculator(object):

    # def __init__(self, name, description):
    #     self.name = name
    #     self.description = description
    #     self.paths = {}
    def __init__(self):
        return None


    def go(self, direction):
        return self.paths.get(direction, None)


    def add_paths(self, paths):
        self.paths.update(paths)


    def testing_testing(self):
        print "It works!"