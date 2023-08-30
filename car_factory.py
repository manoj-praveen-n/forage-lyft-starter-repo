from datetime import date

from car.battery.nubbin_battery import NubbinBattery
from car.battery.spindler_battery import SpindlerBattery
from car.car import Car
from car.engine.capulet_engine import CapuletEngine
from car.engine.sternman_engine import SternmanEngine
from car.engine.willoughby_engine import WilloughbyEngine


class CarFactory:

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        calliope_engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        calliope_battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine=calliope_engine, battery=calliope_battery)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        glissade_engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        glissade_battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine=glissade_engine, battery=glissade_battery)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        palindrome_engine = SternmanEngine(warning_light_is_on=warning_light_on)
        palindrome_battery = SpindlerBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine=palindrome_engine, battery=palindrome_battery)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int,
                         last_service_mileage: int) -> Car:
        rorschach_engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        rorschach_battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine=rorschach_engine, battery=rorschach_battery)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int,
                      last_service_mileage: int) -> Car:
        thovex_engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        thovex_battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        return Car(engine=thovex_engine, battery=thovex_battery)
