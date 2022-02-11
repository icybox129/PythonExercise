class Student:
    def __init__(self, name, age, class_, score1, score2, score3):
        self.name = name
        self.age = age
        self.class_ = class_
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.calc = (self.score1 + self.score2 + self.score3) / 3

    def output(self):
         print(f"Hello", self.name, "your average test score is:", round(self.calc))

s1 = Student("Nick", 31, "DFESW13", 100, 75, 81)
s1.output()