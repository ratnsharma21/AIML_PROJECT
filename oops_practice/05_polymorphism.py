class Cat:
    def make_sound(self):
        return "Meow"

class Dog:
    def make_sound(self):
        return "Woof"

def animal_sound(animal):
    print(animal.make_sound())

cat = Cat()
dog = Dog()
animal_sound(cat)
animal_sound(dog)
