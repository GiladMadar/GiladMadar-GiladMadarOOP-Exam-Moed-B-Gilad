from GoldFish import GoldFish
from Whale import Whale
from Hamster import Hamster
from Dog import Dog
from Cat import Cat


#   Classes Tests : Animal: { WaterAnimal: [GoldFish, Whale], LandAnimal: [Hamster, Dog, Cat] }
def main():
    # Test Water Animals
    print("\n************* Start ****************\n")
    print("\nGoldFish Class Tests:\n")
    goldfish = GoldFish
    goldfish.swim_to()
    goldfish.eat()
    goldfish.sleep()
    goldfish.hide_from_cat()

    print("\n***********************************\n")
    print("Whale Class Tests:\n")
    whale = Whale
    whale.swim_to()
    whale.eat()
    whale.sleep()
    whale.chase_sailboats()

    # Test Land Animals
    print("\n***********************************\n")
    print("Cat Class Tests:\n")
    cat = Cat
    cat.move_to()
    cat.eat()
    cat.sleep()
    cat.overthrow_humans()
    cat.cough_up_furballs()

    print("\n***********************************\n")
    print("Dog Class Tests:\n")
    dog = Dog
    dog.move_to()
    dog.eat()
    dog.sleep()
    dog.chase_cars()
    dog.droll()

    print("\n***********************************\n")
    print("Hamster Class Tests:\n")
    hamster = Hamster
    hamster.move_to()
    hamster.eat()
    hamster.sleep()
    hamster.plan_escape()
    print("\n************** End ***************\n")


#   Performing main Classes Tests
if __name__ == "__main__":
    main()
