# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

math = int(input("Enter a first subject mark"))
Bio = int(input("Enter a second subject mark"))
che = int(input("Enter a third subject mark"))
phy = int(input("Enter a fourth subject mark"))
his = int(input("Enter a fifth subject mark"))

sum = math + Bio + che + phy + his
percentage = sum / 5

if percentage >= 85:
    print("First class")
elif percentage >= 75:
    print("Second class")
elif percentage >= 35:
    print("Third class")
else:
    print("Fail")