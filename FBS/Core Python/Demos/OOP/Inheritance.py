class Student:
    stcount = 0
    def __init__(self, FRN, name, BName):
        self.FRN = FRN
        self.name = name
        self.BName = BName
        Student.stcount += 1

    def display(self):
        print(f"FRN = {self.FRN}\t Name = {self.name}\t BName = {self.BName}")

#EMployee ens here


class PlacedStudent(Student):
    def __init__(self, frn, name, bname, cName):
        super().__init__(frn, name,bname)
        self.cName=cName
    def setCname(self, cName):
        self.cNAme=cName
    def getCName(self):
        return self.cNAme
    def displauy(self):
        print(f"CName=(self.c)")
        super().display    
    
s1 = Student(18, 'Nilesh', 'April')
s2 = Student(19, 'Rohit', 'Jul/Aug')
s3 = Student(20, 'Nitin', 'Jul/Aug')
s4 = PlacedStudent(20, 'Raj', 'Jul/Aug', 'TCS',)
s5 = PlacedStudent(20, 'Ravi', 'Jul/Aug', 'One8')

print(Student.stcount)