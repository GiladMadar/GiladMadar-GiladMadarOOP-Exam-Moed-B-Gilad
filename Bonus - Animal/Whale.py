from abc import abstractmethod
from WaterAnimal import WaterAnimal


class Whale(WaterAnimal):
    @abstractmethod
    def chase_sailboats():
        print("\n- The Whale is chasing the sailboats!")

    def swim_to():
        print("\n- The Whale is swimming!")

    def eat():
        print("\n- The Whale is eating!")

    def sleep():
        print("\n- The Whale is sleeping!")
