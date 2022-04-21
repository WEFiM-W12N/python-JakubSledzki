from dis import dis


class Student:
    def check(self):
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

student1 = Student("daweed", 85)
student2 = Student("kociiol",30)
did_pass = student1.check()
print(did_pass)
did_pass = student2.check()
print(did_pass)   