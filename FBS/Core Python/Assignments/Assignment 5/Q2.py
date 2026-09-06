# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n = int(input("Enter number of student: "))
total_percentage = 0

for i in range(n):
    print('Enters marks for students', i + 1)
    total = 0
    
    for j in range(5):
        marks = float(input('Enter marks of subject' + str(j + 1) + ": " ))
        total = total + marks
        
    percentage = total / 5 
    print("Percentage of Student", i + 1, "=", percentage, "%")


    total_percentage = total_percentage + percentage
    
average = total_percentage / n
print("\nAverage Percentage =", average, "%")


#OR

num = int(input("Enter a number of students: "))
per = 0

for i in range(num):
    physics = int(input("Enter marks of physics: "))
    chemistry = int(input("Enter marks of chemistry: "))
    maths = int(input("Enter marks of maths: "))
    history = int(input("Enter marks of history: "))
    biology = int(input("Enter marks of biology: "))

    total = physics + chemistry + maths + history + biology
    percentage = total / 500 * 100

    print("Percentage of student:", percentage)

    per += percentage

average = per / num
print("Average percentage of all students:", average)