from Horse import Horse
from Pig import Pig
from animal import Animal

if __name__ == "__main__":
    cow = Animal()
    cow.speak()
    horse = Horse("Bill")
    horse.speak()
    horse.get_name()
    horse2 = Horse("Steve")
    horse2.get_name()
    pig = Pig("Pink")
    pig.speak()