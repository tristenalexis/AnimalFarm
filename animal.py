class Animal:
    def __init__(self, name="Joe"):
        self.name = name
        self.sound = "moo"

    def speak(self):
        print(self.sound)