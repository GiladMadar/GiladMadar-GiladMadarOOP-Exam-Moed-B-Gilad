from abc import ABC, abstractmethod
from overrides import overrides
from Animal import Animal


class WaterAnimal(Animal):
    @abstractmethod
    def swim_to(self):
        pass

    @overrides
    def eat(self):
        pass

    @overrides
    def sleep(self):
        pass
