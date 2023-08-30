from abc import ABC

from car.tires.tire import Tire


class CarraignTire(Tire, ABC):
    def __init__(self, tires: list[float]):
        self.tires = tires

    def needs_service(self) -> bool:
        return any(tire >= 0.9 for tire in self.tires)
