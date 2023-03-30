class Fundamentals:

    def ohms_law_current(self, voltage, resistance):
        #returns amps
        return voltage / resistance

    def ohms_law_voltage(self, current, resistance):
        #returns volts
        return current * resistance

    def ohms_law_resistance(self, current, voltage):
        #returns ohms
        return voltage / current

    def voltage_divider(self, resistors):
        product = 1
        for i in resistors:
            product = product * i
        return product / sum(resistors)

    def electrical_power(self, voltage, current):
        #returns wattage
        return voltage * current