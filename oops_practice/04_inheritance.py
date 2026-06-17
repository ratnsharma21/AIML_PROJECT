class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"

d = Dog()
print(d.speak())
print(d.bark())
