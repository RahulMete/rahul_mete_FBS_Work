class Employee:
    def __init__(self,id1,name1,sal1):
        self.id=id1
        self.name=name1
        self.sal=sal1
       
    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid
        
    def getName(self):
        return self.name
    def setName(self,newname):
        self.id=newname
        
    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal=newsal
        
    def display(self):
      print(f"ID={self.id}\tName={self.name}\tSal={self.sal}")
e1=Employee(10,"sachin",121212)
e2=Employee(7,"Mahi", 212121)
print(e1.getName())
e1.display()
e2.display()
e2.setSal(1563498)
e2.display()