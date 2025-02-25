from datetime import date

from car.battery.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, current_date: date, last_service_date: date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days > 1460
