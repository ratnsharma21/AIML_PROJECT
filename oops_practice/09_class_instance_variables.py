class Student:
    school_name = "ABC High School"

    def __init__(self, name):
        self.name = name

s1 = Student("John")
s2 = Student("Jane")
print(s1.name, s1.school_name)
print(s2.name, s2.school_name)
