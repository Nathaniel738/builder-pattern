from aircraft_builder import AircraftBuilder


class Airbus380Builder(AircraftBuilder):

    def build_fuel_capacity(self):
        self.aircraft.fuel_capacity = 32000

    def build_takeoff_speed(self):
        self.aircraft.takeoff_speed = 277.8

    def build_max_speed(self):
        self.aircraft.max_speed = 1020

    def build_passengers_count(self):
        self.aircraft.passengers_count = 538

    def build_mark(self):
        self.aircraft.mark = 'Airbus'

    def build_model(self):
        self.aircraft.model = 'A-380'
