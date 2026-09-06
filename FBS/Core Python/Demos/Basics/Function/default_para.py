#1. To make paramemter optional
#2. Assign value to parameter in function definition
#3. If we passs value to default para, it takes passed value 
    # If we don't pass value to default para, ot tales default value
#4. Flow from right to left(why - postioinal parameter concept)

def emp(id, name='', sal=20000, dept='Backoffice'):
    print('ID', id)
    print('Name', name)
    print('SALARY:', sal)
    print('DEPARTMENT', dept)
    
emp(101, 'ABC', 50000, 'IT')
print('#############')
emp(102, 'XYZ', 70000)