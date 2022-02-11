class Student:
    def __init__(self, name, age, class_, score1, score2, score3):
        self.name = name
        self.age = age
        self.class_ = class_
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.calc = (self.score1 + self.score2 + self.score3) / 3

    @classmethod
    def from_input(cls):
        return cls(
            input("Name: "),
            int(input("Age: ")),
            int(input("Class: "))
        )

user = Student.from_input()