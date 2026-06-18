class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

    def display(self):
        print(self.name, self.roll, self.calculate_grade())

s = Student("Alice", 101, 85)
s.display()
