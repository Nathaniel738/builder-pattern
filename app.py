from airbus380_builder import Airbus380Builder
from aircraft_director import AircraftDirector


def main():
    aircraft_builder = Airbus380Builder()
    aircraft_builder.create_aircraft()
    aircraft_director = AircraftDirector()
    aircraft = aircraft_director.build(aircraft_builder)
    print(get_custom_fields_str(aircraft))


def get_custom_fields_str(obj):
    return '\n'.join(
        '{}: {}'.format(field, obj.__getattribute__(field))
        for field in dir(obj) if not field.startswith('__')
    )


if __name__ == '__main__':
    main()
