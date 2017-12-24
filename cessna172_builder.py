from aircraft_builder import AircraftBuilder


class Cessna172Builder(AircraftBuilder):

    def build_fuel_capacity(self):
        self.aircraft.fuel_capacity = 249.837

    def build_takeoff_speed(self):
        self.aircraft.takeoff_speed = 277.8

    def build_max_speed(self):
        self.aircraft.max_speed = 302

    def build_passengers_count(self):
        self.aircraft.passengers_count = 1

    def build_mark(self):
        self.aircraft.mark = 'Cessna'

    def build_model(self):
        self.aircraft.model = '172'
