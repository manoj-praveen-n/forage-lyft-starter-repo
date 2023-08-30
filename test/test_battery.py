import unittest
from datetime import datetime

from car.battery.nubbin_battery import NubbinBattery
from car.battery.spindler_battery import SpindlerBattery
from car.engine.capulet_engine import CapuletEngine
from car.engine.sternman_engine import SternmanEngine
from car.engine.willoughby_engine import WilloughbyEngine


class TestNubbinBattery(unittest.TestCase):

    def setUp(self) -> None:
        self.today = datetime.now().date()

    def test_nubbin_battery_needs_service(self):
        last_service_date = self.today.replace(year=self.today.year - 5)
        battery = NubbinBattery(current_date=self.today, last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_no_needs_service(self):
        last_service_date = self.today.replace(year=self.today.year - 2)
        battery = NubbinBattery(current_date=self.today, last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):

    def setUp(self) -> None:
        self.today = datetime.now().date()

    def test_spindler_battery_needs_service(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        battery = SpindlerBattery(current_date=self.today, last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_no_needs_service(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        battery = SpindlerBattery(current_date=self.today, last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())


class TestCapuletEngine(unittest.TestCase):

    def test_capulet_engine_needs_service(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_no_needs_service(self):
        current_mileage = 300
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):

    def test_willoughby_engine_needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_no_needs_service(self):
        current_mileage = 300
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):

    def test_sternman_engine_needs_service(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_no_needs_service(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
