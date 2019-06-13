
class Students:
    def __init__(self, name, age, gpa, payed):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.payed = payed

    def classification(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False