class AircraftDirector:
    def __init__(self):
        self._builder = None

    def build(self, aircraft_builder):
        self._builder = aircraft_builder
        self._builder.build_fuel_capacity()
        self._builder.build_takeoff_speed()
        self._builder.build_max_speed()
        self._builder.build_passengers_count()
        self._builder.build_mark()
        self._builder.build_model()
        return self._builder.aircraft
