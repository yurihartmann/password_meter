from abc import ABC, abstractmethod


class Rate(ABC):
    _weight = 0

    def __init__(self, weight: int):
        self._weight = weight

    def get_weight(self):
        return self._weight

    @abstractmethod
    def calculate(self, requirement):
        pass
