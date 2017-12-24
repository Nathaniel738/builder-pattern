import abc
from abc import ABCMeta

from aircraft import Aircraft


class AircraftBuilder(metaclass=ABCMeta):

    def __init__(self):
        self.aircraft = None

    def create_aircraft(self):
        self.aircraft = Aircraft()

    @abc.abstractmethod
    def build_mark(self):
        pass

    @abc.abstractmethod
    def build_model(self):
        pass

    @abc.abstractmethod
    def build_max_speed(self):
        pass

    @abc.abstractmethod
    def build_takeoff_speed(self):
        pass

    @abc.abstractmethod
    def build_passengers_count(self):
        pass

    @abc.abstractmethod
    def build_fuel_capacity(self):
        pass
