#WAP to add 
# 1) TWo integer no.
# 2) Two strings
# 3) Two floating number 
# 4) Two list 
# 5) Two time Object 


# 1) Addition of two integer numbers
# a = 50
# b = 40
# print("Addition of integers:", a + b)

# # 2) Addition of two strings
# str1 = "Rahul "
# str2 = "Swarup"
# print("Addition of strings:", str1 + str2)

# # 3) Addition of two floating numbers
# x = 15.7
# y = 25.5
# print("Addition of floats:", x + y)

# # 4) Addition of two lists
# li1 = [4, 5, 6]
# li2 = [7, 8, 9]
# print("Addition of lists:", li1 + li2)

# 5) Addition of two time objects

# class Time:
#     def __init__(self, hr, min, sec):
#         self.hr = hr
#         self.min = min
#         self.sec = sec

#     def gethr(self):
#         return self.hr

#     def sethr(self, nhr):
#         self.hr = nhr

#     def getmin(self):
#         return self.min

#     def setmin(self, nmin):
#         self.min = nmin

#     def getsec(self):
#         return self.sec

#     def setsec(self, nsec):
#         self.sec = nsec

#     def __str__(self):
#         return f"{self.hr}:{self.min}:{self.sec}"
    
#     def __add__(self,other):
#         thr=self.hr+other.hr
#         tmin=self.min+other.min
#         tsec=self.sec+other.sec
#         return Time(thr,tmin,tsec)
           
 


# t1 = Time(12, 33, 55)
# t2 = Time(6, 30, 56)
# print(t1+t2)


# Operator Overloading FinishS






class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def gethr(self):
        return self.hr

    def sethr(self, nhr):
        self.hr = nhr

    def getmin(self):
        return self.min

    def setmin(self, nmin):
        self.min = nmin

    def getsec(self):
        return self.sec

    def setsec(self, nsec):
        self.sec = nsec

    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    
    def __add__(self,other):
        tsec=self.sec+other.sec
        emin=tsec//60
        tsec=tsec%60
        
        tmin=self.min+other.min+emin
        ehr=tmin//60
        tmin=tmin%60
        
        thr=self.hr+other.hr+ehr
        return Time(thr,tmin,tsec)
           
t1 = Time(12, 33, 55)
t2 = Time(6, 30, 56)
a=t1+t2
print(a)

