class Parallel:

    def resistance_total(self, resistors):
        conductance = 0
        for i in resistors:
            conductance = conductance + (1/i)
        return 1 / conductance