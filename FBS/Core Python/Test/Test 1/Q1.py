l = float(input('Enter Length: '))
b = float(input('Enter breadth: '))
r = float(input('Enter radius: '))

area = (l * b) + (0.5 * 3.14 * r ** 2)

perimeter = ( 2 * l) + b + (3.14 * r)

print('area =', round(area, 2))
print('Perimeter =', round(perimeter, 2))