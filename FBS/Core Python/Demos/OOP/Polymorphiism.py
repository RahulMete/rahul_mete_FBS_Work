# class Employee:
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

#     def calSal(self):
#             print(f"Final salary of Developer {self.sal+self.bonus}")
            
#     def display(self):
#         print(f"bonus = {self.bonus}")
#         super().display()


# e1 = Employee(101, "Swarup", 30000)

# h1 = HR(103, "Sid", 40000, 5000)

# d1 = Developer(105, "Rohit", 50000, 7000)

# d1.calSal()
# e1.calSal()
# h1.calSal()




# 1) 
# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def getBrand(self):
#         return self.brand
#     def setBrand(self, newbrand):
#         self.brand = newbrand

#     def getModel(self):
#         return self.model
#     def setModel(self, newmodel):
#         self.model = newmodel

#     def getPrice(self):
#         return self.price
#     def setPrice(self, newprice):
#         self.price = newprice

#     def __str__(self):
#         return f"Brand = {self.brand}\t Model = {self.model}\t Price = {self.price}"

#     def display(self):
#         print(f"Brand = {self.brand}\t Model = {self.model}\t Price = {self.price}")

# class GamingLaptop(Laptop):
#     def __init__(self, brand, model, price, gpu):
#         super().__init__(brand, model, price)
#         self.gpu = gpu

#     def getGPU(self):
#         return self.gpu
#     def setGPU(self, newgpu):
#         self.gpu = newgpu

#     def __str__(self):
#         return super().__str__() + f"\t gpu = {self.gpu}"

#     def display(self):
#         super().display()
#         print(f"GPU = {self.gpu}")

# class Ultrabook(Laptop):
#     def __init__(self, brand, model, price, weight):
#         super().__init__(brand, model, price)
#         self.weight = weight

#     def getweight(self):
#         return self.weight 
#     def setweight(self, newweight):
#         self.weight = newweight

#     def __str__(self):
#         return super().__str__() + f"\t weight = {self.weight}"

#     def display(self):
#         super().display()
#         print(f'Weight = {self.weight}')

# l1 = Laptop('Dell', 'Inspiron', 800)
# g1 = GamingLaptop('Asus', 'ROG', 1500, 'NVIDIA RTX 3060')
# u1 = Ultrabook('Apple', 'MacBook Air', 1200, 1.25)

# # l1.display()
# # g1.display()
# # u1.display()

# print(l1)
# print(g1)
# print(u1)



# 2)
# class city:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population

#     def getName(self):
#         return self.name
#     def setName(self, newname):
#         self.name = newname

#     def getPopulation(self):
#         return self.population
#     def setPopulation(self, newpopulation):
#         self.population = newpopulation

#     def __str__(self):
#         return f"Name = {self.name}\t Population = {self.population}"

#     def display(self):
#         print(f"Name = {self.name}\t Population = {self.population}")

# class Dubai(city):
#     def __init__(self, name, population, tourism):
#         super().__init__(name, population)
#         self.tourism = tourism

#     def getTourism(self):
#         return self.tourism
#     def setTourism(self, newtourism):
#         self.tourism = newtourism

#     def __str__(self):
#         return super().__str__() + f"\t tourism = {self.tourism}"

#     def display(self):
#         super().display()
#         print(f"Tourism = {self.tourism}")

# class NewYork(city):
#     def __init__(self, name, population, finance):
#         super().__init__(name, population)
#         self.finance = finance

#     def getFinance(self):
#         return self.finance
#     def setFinance(self, newfinance):
#         self.finance = newfinance

#     def __str__(self):
#         return super().__str__() + f"\t finance = {self.finance}"
 
#     def display(self):
#         super().display()
#         print(f"Finance = {self.finance}")

# c1 = city('Generic City', 1000000)
# d1 = Dubai('Dubai', 3000000, 'High')
# n1 = NewYork('New York', 8000000, 'Very High')

# # c1.display()
# # d1.display()
# # n1.display()

# print(c1)
# print(d1)
# print(n1)


# 3)
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def getmake(self):
#         return self.make
#     def setmake(self, newmake):
#         self.make = newmake

#     def getmodel(self):
#         return self.model
#     def setmodel(self, newmodel):
#         self.model = newmodel

#     def getyear(self):
#         return self.year
#     def setyear(self, newyear):
#         self.year = newyear

#     def __str__(self):
#         return f"Year = {self.year}\t Model = {self.model}\t Make = {self.make}"

#     def display(self):
#         print(f"Year = {self.year}\t Model = {self.model}\t Make = {self.make}")

# class BMW(Car):
#     def __init__(self, make, model, year, series):
#         super().__init__(make, model, year)
#         self.series = series

#     def getseries(self):
#         return self.series
#     def setseries(self, newseries):
#         self.series = newseries

#     def __str__(self):
#         return super().__str__() + f"\t series = {self.series}"

#     def display(self):
#         super().display()
#         print(f"Series = {self.series}")

# class Audi(Car):
#     def __init__(self, make, model, year, trim):
#         super().__init__(make, model, year)
#         self.trim = trim

#     def gettrim(self):
#         return self.trim
#     def settrim(self, newtrim):
#         self.trim = newtrim

#     def __str__(self):
#         return super().__str__() + f"\t trim = {self.trim}"

#     def display(self):
#         super().display()
#         print(f"Trim = {self.trim}")

# c1 = Car('Toyota', 'Camry', 2020)
# b1 = BMW('BMW', 'X5', 2021, 'M')
# a1 = Audi('Audi', 'A4', 2022, 'Premium')

# # c1.display()
# # b1.display()
# # a1.display()

# print(c1)
# print(b1)
# print(a1)


# 4)
# class Bike:
#     def __init__(self, name1,number,speed):
#         self.name = name1
#         self.number = number
#         self.speed = speed

#     def getName(self):
#         return self.name
#     def setName(self,newname):
#         self.name = newname

#     def getNumber(self):
#         return self.number
#     def setNumber(self, newnumber):
#         self.number = newnumber

#     def getSpeed(self):
#         return self.speed
#     def setSpeed(self, newspeed):
#         self.speed = newspeed

#     def __str__(self):
#         return f"Name = {self.name}\t Number = {self.number}\t Speed = {self.speed}"

#     def display(self):
#         print(f"Name = {self.name}\t Number = {self.number}\t Speed = {self.speed}")

# class SportsBike(Bike):
#     def __init__(self, name1, number, speed, turbo):
#         super().__init__(name1, number, speed)
#         self.turbo = turbo

#     def getTurbo(self):
#         return self.turbo
#     def setTurbo(self, newturbo):
#         self.turbo = newturbo

#     def __str__(self):
#         return super().__str__() + f"\t turbo = {self.turbo}"
  

#     def display(self):
#         super().display()
#         print(f"Turbo = {self.turbo}")

# class CruiserBike(Bike):
#     def __init__(self, name1, number, speed, comfort):
#         super().__init__(name1, number, speed)
#         self.comfort = comfort

#     def getComfort(self):
#         return self.comfort
#     def setComfort(self, newcomfort):
#         self.comfort = newcomfort

#     def __str__(self):
#         return super().__str__() + f"\t comfort = {self.comfort}"

#     def display(self):
#         super().display()
#         print(f"Comfort = {self.comfort}")

# b1 = Bike('Yamaha', '1234', 120)
# s1 = SportsBike('Suzuki', '5678', 150, 'Yes')
# c1 = CruiserBike('Honda', '9101', 100, 'High')

# # b1.display()
# # s1.display()
# # c1.display()

# print(b1)
# print(s1)
# print(c1)



# 5)
# class Student:
#     def __init__(self,name1, mark1, department1):
#         self.name = name1
#         self.mark = mark1
#         self.department = department1

#     def getName(self):
#         return self.name
#     def setName(self,newname):
#         self.name = newname

#     def getMark(self):
#         return self.mark
#     def setMark(self, newmark):
#         self.mark = newmark

#     def getDepartment(self):
#         return self.department
#     def setDepartment(self,newdepartment):
#         self.department = newdepartment

#     def __str__(self):
#         return f"Name = {self.name}\t Mark = {self.mark}\t Department = {self.department}" 
    
#     def display(self):
#         print(f"Name = {self.name}\t Mark = {self.mark}\t Department = {self.department}")

# class Science(Student):
#     def __init__(self, name1, mark1, department1, Bio_mark1):
#         super().__init__(name1, mark1, department1)
#         self.Bio_mark = Bio_mark1

#     def getBioMark(self):
#         return self.Bio_mark

#     def setBioMark(self, newBio_mark):
#         self.Bio_mark = newBio_mark

#     def __str__(self):
#         return super().__str__() + f"\t Bio_mark = {self.Bio_mark}"
    
#     def display(self):
#         super().display()
#         print(f"Bio Mark = {self.Bio_mark}")


# class Arts(Student):
#     def __init__(self, name1, mark1, department1, History_mark1):
#         super().__init__(name1, mark1, department1)
#         self.History_mark = History_mark1

#     def getHistoryMark(self):
#         return self.History_mark

#     def setHistoryMark(self, newHistory_mark):
#         self.History_mark = newHistory_mark

#     def __str__(self):
#         return super().__str__() + f"\t History_mark = {self.History_mark}"

#     def display(self):
#         super().display()
#         print(f"History Mark = {self.History_mark}")

# s1 = Student('Alice', 85, 'Science')
# S1 = Science('Alice', 85, 'Science', 90)
# A1 = Arts('Alice', 85, 'Arts', 88)

# # s1.display()
# # S1.display()
# # A1.display()

# print(s1)
# print(S1)
# print(A1)





