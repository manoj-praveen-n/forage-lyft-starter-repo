from abc import ABC

from car.tires.tire import Tire


class OctoprimeTire(Tire, ABC):
    def __init__(self, tires: list[float]):
        self.tires = tires

    def needs_service(self) -> bool:
        return sum(self.tires) >= 3
