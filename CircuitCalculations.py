from fractions import Fraction
class Fundamentals:

    def ohms_law_current(self, voltage, resistance):
        return voltage / resistance

    def ohms_law_voltage(self, current, resistance):
        return current * resistance

    def ohms_law_resistance(self, current, voltage):
        return voltage / current

    def voltage_divider(self, resistors):
        product = 1
        for i in resistors:
            product = product * i
        return product / sum(resistors)

class Series:

    def resistance_total(self, resistors):
        return sum(resistors)

class Parallel:

    def resistance_total(self, resistors):
        conductance = 0
        for i in resistors:
            conductance = conductance + (1/i)
        return 1 / conductance

class SeriesParallel:

    def resistance_total(self, series_resistance, parallel_resistance):
        return series_resistance + parallel_resistance

    def resistance_between_nodes_a_b(self, series_resistors, parallel_resistors):
        conductance = 0
        for i in parallel_resistors:
            conductance = conductance + (1/i)
        return 1 / (conductance + (1/sum(series_resistors)))

    def resistance_between_nodes_a_c(self, series_resistors_one, series_resistors_two):
        return 1 / ((1/sum(series_resistors_one)) + 1/sum(series_resistors_two))

    def resistance_between_nodes_a_d(self, series_resistors_one, series_resistors_two):
        return 1 / ((1/sum(series_resistors_one)) + 1/sum(series_resistors_two))