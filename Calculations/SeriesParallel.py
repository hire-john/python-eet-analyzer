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