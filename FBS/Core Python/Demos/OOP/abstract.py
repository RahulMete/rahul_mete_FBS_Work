# from abc import ABC,abstractmethod
# class Employee(ABC):
#     def __init__(self, id, name, sal):
#         self.id = id
#         self.name = name
#         self.sal = sal
        
#     def calSal(self):
#             print(f"Final salary of Employee {self.sal}")

#     def display(self):
#         print(f"ID = {self.id}\tName = {self.name}\tSalary = {self.sal}")


# class HR(Employee):
#     def __init__(self, id, name, sal, commission):
#         super().__init__(id, name, sal)
#         self.commission = commission

#     def setCommission(self, commission):
#         self.commission = commission

#     def getCommission(self):
#         return self.commission

#     def calSal(self):
#         print(f"Final salary of HR {self.sal+self.commission}")
    
#     def display(self):
#         print(f"Commission = {self.commission}")
#         super().display()


# class Developer(Employee):
#     def __init__(self, id, name, sal, bonus):
#         super().__init__(id, name, sal)
#         self.bonus = bonus

#     def setbonus(self, bonus):
#         self.bonus = bonus

#     def getbonus(self):
#         return self.bonus
    
#     @abstractmethod
#     def calSal(self):
#         pass

#     def calSal(self):
#             print(f"Final salary of Developer {self.sal+self.bonus}")
            
#     def display(self):
#         print(f"bonus = {self.bonus}")
#         super().display()


# # e1 = Employee(101, "Swarup", 30000)
# h1 = HR(103, "Sid", 40000, 5000)
# d1 = Developer(105, "Rohit", 50000, 7000)

# d1.calSal()
# # e1.calSal()
# h1.calSal()





# 2)
# class Employee:
#     def __init__(self,id1,name1,sal1):
#         self.id = id1
#         self.name = name1
#         self.sal = sal1

#     def getId(self):
#         return self.id
#     def setId(self,newid):
#         self.id = newid

#     def getName(self):
#         return self.name
#     def setName(self, newname):
#         self.name = newname

#     def getSal(self):
#         return self.sal
#     def setSal(self, newsal):
#         self.sal = newsal

#     def CalSal(self):
#         print(f"Final Sal is EMP = {self.sal}")

#     def __str__(self):
#         return f"Id = {self.id}\tName = {self.name}\tSalary = {self.sal}"
    
#     def display(self):
#         print(f"Id = {self.id}\tName = {self.name}\tSalary = {self.sal}")


# class HR(Employee):
#     def __init__(self, id1, name1, sal1, comission):
#         super().__init__(id1, name1, sal1)
#         self.comission = comission

#     def getcomission(self):
#         return self.comission
#     def setcomission(self, newcomission):
#         self.comission = newcomission

#     def CalSal(self):
#         print(f"final sal of HR = {self.sal+self.comission}")

#     def __str__(self):
#         return super().__str__() + f"\tComission = {self.comission}"
    
#     def display(self):
#         print(f"Comission={self.comission}\t")
#         return super().display()


# #### Hr end here

# class Devloper(Employee):
#     def __init__(self, id1, name1, sal1, bonus):
#         super().__init__(id1, name1, sal1)
#         self.bonus = bonus

#     def getbonus(self):
#         return self.bonus
#     def setbonus(self, newbonus):
#         self.bonus = newbonus

#     def CalSal(self):
#         print(f"Final sal of devloper is = {self.sal+self.bonus}")

#     def __str__(self):
#         return super().__str__() + f"\tBonus = {self.bonus}"

#     def display(self):
#         print(f"Bonus={self.bonus}\t")
#         return super().display()


# e1 = Employee(1, 'Rahul', 3535)
# h1 = HR(7,'hima', 2525, 1500)
# d1 = Devloper(9, 'ram', 1546, 2500)

# # h1.CalSal()
# # e1.CalSal()
# # d1.CalSal()

# print(e1)
# print(h1)
# print(d1)



# 3)
# from abc import ABC,abstractmethod
# class Vehicle(ABC):

#     def __init__(self,cNo,color):   
#         self.cno=cNo
#         self.clolor=color

#     def getCno(self):
#         return self.cno

#     def setCno(self,neno):
#         self.setCno-neno

#     def getColor(self): 
#         return self.clolor
    
#     def setCol(self,nCol):
#         self.clolor=nCol
#     @abstractmethod
    
#     def brake(self):
#         pass

#     def str (self):
#         return f"Che No= (self.cno) Color=(self.clolor)"

# class Car(Vehicle): 
#     def brake(self):
#         print("This is the Brak of Car ")

# c=Car(12,"White")
# print(c)
# c.brake()


# 4)
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    @abstractmethod
    def calSal(self):
        pass

    def display(self):
        print(f"ID = {self.id}\tName = {self.name}\tSalary = {self.sal}")


class HR(Employee):
    def __init__(self, id, name, sal, commission):
        super().__init__(id, name, sal)
        self.commission = commission

    def calSal(self):
        print(f"Final Salary of HR: {self.sal + self.commission}")

    def display(self):
        print(f"Commission = {self.commission}")
        super().display()


class Developer(Employee):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def calSal(self):
        print(f"Final Salary of Developer: {self.sal + self.bonus}")

    def display(self):
        print(f"Bonus = {self.bonus}")
        super().display()


# Storing objects in a Dictionary
employees = {
    103: HR(103, "Sid", 40000, 5000),
    105: Developer(105, "Rohit", 50000, 7000)
}

for emp in employees.values():
    emp.display()
    emp.calSal()
    print()
    
# Employee ID acts as the key.
# You can directly access a specific employee, e.g. employees[103].
# It makes searching, updating, and deleting employee records easier.