#1. ()
#tu = (10,) #use comma for single value
tu = (10, 20, 30, 'a', 3.14, 10)

#2. Hetrogeneous

#3. Ordered

#4. Immutable

#5. Duplication elemnts allowed 

#6. Tuple is faster than list 
#tu[0] = 50 #raise error

import sys 
li = []
tu = ()
print(type(tu))
print(tu)
print(sys.getsizeof(li))
print(sys.getsizeof(tu))