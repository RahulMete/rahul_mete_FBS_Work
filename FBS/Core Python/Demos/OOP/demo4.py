class Person:
    def __init__(self,name1,age1,gender1):
        self.name=name1
        self.age=age1
        self.gender=gender1
       
    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname
        
    def getAge(self):
        return self.age
    def setAge(self,newage):
        self.age=newage
        
    def geGender(self):
        return self.gender
    def setGender(self,newgender):
        self.gender=newgender
    
    
    def display(self):
        print(f"Name={self.name}\tAge={self.age}\tGender={self.gender}")
e1=Person("Rahul",20,"Male")
e2=Person("Pradnya",22,"Female")
print(e1.getName())
e1.display()
e2.display()
e2.setAge(20)
e2.display()