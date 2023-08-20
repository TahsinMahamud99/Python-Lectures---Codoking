#LECTURE 3

'''
Swapping values

1. using 3 veriables
2. using 2 variables
-----------------------------------------
'''
x = 2
y = 3

temp = x
x = y
y = temp

print("x =", x)
print("y =", y)

print()

x = x + y
y = x - y
x = x - y

print("x =", x)
print("y =", y)



'''--------------------------------------
Float to specific decimal places
EXAMPLE
Calculate the area of a rectangle displaying your answer in 2 decimal places
'''
base = 4.3
height = 3.12359

area = base * height

print("area of rectangle =", area)

print(f'area pf rectangle = {area:.2f}')
