# class Employee:
#     def __init__(self, id, name, sal):
#         self.id = id
#         self.name = name
#         self.sal = sal

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

#     def display(self):
#         print(f"bonus = {self.bonus}")
#         super().display()


# e1 = Employee(101, "Swarup", 30000)

# h1 = HR(103, "Sid", 40000, 5000)

# d1 = Developer(105, "Rohit", 50000, 7000)

# e1.display()
# h1.display()
# d1.display()


# 1)
# class Person:
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"ID = {self.id}\tName = {self.name}\tAge = {self.age}")


# class Student(Person):
#     def __init__(self, id, name, age, marks):
#         super().__init__(id, name, age)
#         self.marks = marks

#     def setMarks(self, marks):
#         self.marks = marks

#     def getMarks(self):
#         return self.marks

#     def display(self):
#         print(f"Marks = {self.marks}")
#         super().display()


# class Teacher(Person):
#     def __init__(self, id, name, age, subject):
#         super().__init__(id, name, age)
#         self.subject = subject

#     def setSubject(self, subject):
#         self.subject = subject

#     def getSubject(self):
#         return self.subject

#     def display(self):
#         print(f"Subject = {self.subject}")
#         super().display()


# p1 = Person(101, "Rahul", 20)
# s1 = Student(102, "Amit", 18, 85)
# t1 = Teacher(103, "Sneha", 35, "Maths")

# p1.display()
# s1.display()
# t1.display()


# 2)
# class Building:
#     def __init__(self, id, name, floors):
#         self.id = id
#         self.name = name
#         self.floors = floors

#     def display(self):
#         print(f"ID = {self.id}\tName = {self.name}\tFloors = {self.floors}")


# class House(Building):
#     def __init__(self, id, name, floors, rooms):
#         super().__init__(id, name, floors)
#         self.rooms = rooms

#     def setRooms(self, rooms):
#         self.rooms = rooms

#     def getRooms(self):
#         return self.rooms

#     def display(self):
#         print(f"Rooms = {self.rooms}")
#         super().display()


# class Office(Building):
#     def __init__(self, id, name, floors, employees):
#         super().__init__(id, name, floors)
#         self.employees = employees

#     def setEmployees(self, employees):
#         self.employees = employees

#     def getEmployees(self):
#         return self.employees

#     def display(self):
#         print(f"Employees = {self.employees}")
#         super().display()


# b1 = Building(101, "Main Building", 5)
# h1 = House(102, "Rahul House", 2, 4)
# o1 = Office(103, "Tech Office", 10, 200)

# b1.display()
# h1.display()
# o1.display()


# # 3)
# class ElectronicDevice:
#     def __init__(self, id, brand, price):
#         self.id = id
#         self.brand = brand
#         self.price = price

#     def display(self):
#         print(f"ID = {self.id}\tBrand = {self.brand}\tPrice = {self.price}")


# class Mobile(ElectronicDevice):
#     def __init__(self, id, brand, price, camera):
#         super().__init__(id, brand, price)
#         self.camera = camera

#     def setCamera(self, camera):
#         self.camera = camera

#     def getCamera(self):
#         return self.camera

#     def display(self):
#         print(f"Camera = {self.camera} MP")
#         super().display()


# class Laptop(ElectronicDevice):
#     def __init__(self, id, brand, price, ram):
#         super().__init__(id, brand, price)
#         self.ram = ram

#     def setRam(self, ram):
#         self.ram = ram

#     def getRam(self):
#         return self.ram

#     def display(self):
#         print(f"RAM = {self.ram} GB")
#         super().display()


# e1 = ElectronicDevice(101, "Sony", 30000)
# m1 = Mobile(102, "Samsung", 25000, 50)
# l1 = Laptop(103, "Dell", 60000, 16)

# e1.display()
# m1.display()
# l1.display()



# 4)
# class Animal:
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"ID = {self.id}\tName = {self.name}\tAge = {self.age}")


# class Dog(Animal):
#     def __init__(self, id, name, age, breed):
#         super().__init__(id, name, age)
#         self.breed = breed

#     def setBreed(self, breed):
#         self.breed = breed

#     def getBreed(self):
#         return self.breed

#     def display(self):
#         print(f"Breed = {self.breed}")
#         super().display()


# class Cat(Animal):
#     def __init__(self, id, name, age, color):
#         super().__init__(id, name, age)
#         self.color = color

#     def setColor(self, color):
#         self.color = color

#     def getColor(self):
#         return self.color

#     def display(self):
#         print(f"Color = {self.color}")
#         super().display()


# a1 = Animal(101, "Animal", 5)
# d1 = Dog(102, "Bruno", 3, "Labrador")
# c1 = Cat(103, "Mimi", 2, "White")

# a1.display()
# d1.display()
# c1.display()



# 5)
class Account:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def display(self):
        print(f"ID = {self.id}\tName = {self.name}\tBalance = {self.balance}")


class SavingsAccount(Account):
    def __init__(self, id, name, balance, interest):
        super().__init__(id, name, balance)
        self.interest = interest

    def setInterest(self, interest):
        self.interest = interest

    def getInterest(self):
        return self.interest

    def display(self):
        print(f"Interest = {self.interest}%")
        super().display()


class CurrentAccount(Account):
    def __init__(self, id, name, balance, overdraft):
        super().__init__(id, name, balance)
        self.overdraft = overdraft

    def setOverdraft(self, overdraft):
        self.overdraft = overdraft

    def getOverdraft(self):
        return self.overdraft

    def display(self):
        print(f"Overdraft Limit = {self.overdraft}")
        super().display()


a1 = Account(101, "Rahul", 50000)

s1 = SavingsAccount(102, "Amit", 75000, 6.5)

c1 = CurrentAccount(103, "Rohit", 100000, 25000)

a1.display()
s1.display()
c1.display() 