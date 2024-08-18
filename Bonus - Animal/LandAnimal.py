from abc import ABC, abstractmethod
from Animal import Animal
from overrides import overrides


class LandAnimal(Animal):
    @abstractmethod
    def move_to(self):
        pass

    @overrides
    def eat(self):
        pass

    @overrides
    def sleep(self):
        pass
