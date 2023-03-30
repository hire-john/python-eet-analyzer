import Units
import Calculations

Metric = Units.Metric()
Fundamentals = Calculations.Fundamentals()
Series = Calculations.Series()
Parallel = Calculations.Parallel()
SeriesParallel = Calculations.SeriesParallel()

voltage = 120
r1 = 1.1
r2 = 2.2
r3 = 3.3
r4 = 4.4
r5 = 5.5
r6 = 6.6
r7 = 7.7
r8 = 8.8

series_resistors = [1, 2]
parallel_resistors = [80, 50]

def resistance_between_nodes_a_b():
    series_resistors = [r1, r2, r7]
    parallel_resistors = [r8]
    resistance_between = SeriesParallel.resistance_between_nodes_a_b(series_resistors, parallel_resistors)
    print(resistance_between)
    print(f"\n")

def resistance_between_nodes_a_c():
    series_resistors_one = [r1, r2]
    series_resistors_two = [r7, r8]
    resistance_between = SeriesParallel.resistance_between_nodes_a_c(series_resistors_one, series_resistors_two)
    print(resistance_between)
    print(f"\n")

def resistance_between_nodes_a_x():
    series_resistors_one = [r1, r2]
    series_resistors_two = [r7, r8]
    resistance_between = SeriesParallel.resistance_between_nodes_a_c(series_resistors_one, series_resistors_two)
    series_resistors = [r3, r4, r5]
    parallel_resistors = [r6]
    resistance_between = resistance_between + SeriesParallel.resistance_between_nodes_a_b(series_resistors, parallel_resistors)
    print(resistance_between)
    print(f"\n")

def resistance_between_nodes_a_e():
    series_resistors_one = [r1, r2]
    series_resistors_two = [r7, r8]
    resistance_between = SeriesParallel.resistance_between_nodes_a_c(series_resistors_one, series_resistors_two)
    series_resistors_one = [r3, r4]
    series_resistors_two = [r5, r6]
    resistance_between = resistance_between + SeriesParallel.resistance_between_nodes_a_c(series_resistors_one, series_resistors_two)
    print(resistance_between)
    print(f"\n")

def resistance_between_nodes_a_e_ground():
    series_resistors = [r1, r2]
    parallel_resistors = [r6]
    resistance_between = SeriesParallel.resistance_between_nodes_a_b(series_resistors, parallel_resistors)
    series_resistors = [r3, r4]
    parallel_resistors = [r5]
    resistance_between = resistance_between + SeriesParallel.resistance_between_nodes_a_b(series_resistors, parallel_resistors)
    print(resistance_between)
    print(f"\n")

def current_between_nodes_a_e_ground():
    series_resistors = [r1, r2]
    parallel_resistors = [r6]
    resistance_between = SeriesParallel.resistance_between_nodes_a_b(series_resistors, parallel_resistors)
    series_resistors = [r3, r4]
    parallel_resistors = [r5]
    resistance_between = resistance_between + SeriesParallel.resistance_between_nodes_a_b(series_resistors, parallel_resistors)
    print(resistance_between)
    print(Fundamentals.ohms_law_current(voltage, resistance_between))
    print(f"\n")

def voltage_in_r1_and_4(resistor):
    series_resistors = [r1, r4]
    parallel_resistors = [r2, r3]
    series_resistance = Series.resistance_total(series_resistors)
    parallel_resistance = Parallel.resistance_total(parallel_resistors)
    series_parallel_resistance = SeriesParallel.resistance_total(series_resistance, parallel_resistance)
    # add metric abbreviations as function argument
    resistance_equivalence = round((Fundamentals.voltage_divider(parallel_resistors) + series_resistance) * Metric.base_ten("kilo"), 2)
    print(Fundamentals.ohms_law_current(voltage, resistance_equivalence) * series_resistors[resistor] * (10 ** -4))
    print(f"\n")

def voltage_in_r2_and_3():
    series_resistors = [r1, r4]
    parallel_resistors = [r2, r3]
    series_resistance = Series.resistance_total(series_resistors)
    parallel_resistance = Parallel.resistance_total(parallel_resistors)
    series_parallel_resistance = SeriesParallel.resistance_total(series_resistance, parallel_resistance)
    # add metric abbreviations for function argument
    resistance_equivalence = Fundamentals.voltage_divider(parallel_resistors)
    current = Fundamentals.ohms_law_current(voltage, resistance_equivalence + series_resistance)
    voltage_resistor_two = current * resistance_equivalence
    print(voltage_resistor_two)
    print(f"\n")

def current_in_circuit_and_r1_r4():
    series_resistors = [r1, r4]
    parallel_resistors = [r2, r3]
    series_resistance = Series.resistance_total(series_resistors)
    parallel_resistance = Parallel.resistance_total(parallel_resistors)
    series_parallel_resistance = SeriesParallel.resistance_total(series_resistance, parallel_resistance)
    # add metric abbreviations for function argument
    resistance_equivalence = Fundamentals.voltage_divider(parallel_resistors)
    current = Fundamentals.ohms_law_current(voltage, series_parallel_resistance)
    voltage_resistor_two = current * resistance_equivalence
    print(current)
    print(f"\n")


#voltage_in_r1_and_4(1)
#voltage_in_r2_and_3()
#resistance_between_nodes_a_b()
#resistance_between_nodes_a_c()
#resistance_between_nodes_a_x()
#resistance_between_nodes_a_e()
#resistance_between_nodes_a_e_ground()
#current_between_nodes_a_e_ground()
#current_in_circuit_and_r1_r4()

#print(Fundamentals.electrical_power(voltage, Fundamentals.ohms_law_current(voltage, 80)))
#print(Parallel.resistance_total(parallel_resistors))

print(Fundamentals.ohms_law_current(voltage, Parallel.resistance_total(parallel_resistors)))