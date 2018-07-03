from animal import Animal


class Pig(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.sound = "oink"

    def get_name(self):
        print(self.name)

    def speak(self):
        print("Pigs say", self.sound)