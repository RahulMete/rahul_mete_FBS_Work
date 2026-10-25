class Building:
    def __init__(self,add1,floors1,area1):
        self.add=add1
        self.floors=floors1
        self.area=area1
       
    def getAdd(self):
        return self.add
    def setAdd(self,newadd):
        self.add=newadd
        
    def getFloors(self):
        return self.floors
    def setFloors(self,newfloors):
        self.floors=newfloors
        
    def getArea(self):
        return self.area
    def setArea(self,newarea):
        self.area=newarea
    
    
    def display(self):
        print(f"Add={self.add}\tFloors={self.floors}\tArea={self.area}")
e1=Building("Shivaji Nagar","3",2000)
e2=Building("Katraj", "4", 3000)
print(e1.getAdd())
e1.display()
e2.display()
e2.setFloors(6)
e2.display()