#LECTURE 2

'''---Data types---------------------------------
1. integers 5, 6, 99, 7
2. float 5.4, 77.0, 8.99
3. strings 'My name is Vegeta'
4. characters a, b, c, d, -, >, /
5. booleans

    Input/output
'''
#---------------------------------------------------
x = 10
word = 'Goku'

x = '10'

print(x)



'''---Basic Operations----------------------------
1.addition
2.subtraction
3.multiplication
4.division

*string concatenation

USE BODMAS: Brackets, ()
            Order, 
            Division, /
            Multiplication, * 
            Addition, +
            Subtraction -

____
|   |
|   |
|___| 

|*
| *
|___*            
'''

base = int(input("Enter base:"))
height = int(input("Enter height:"))

area = (base * height) / 2

print("The area of the rectangle is:", area)


radius = float(input("Enter radius:"))
#area = radius squared * pi
area_circle = radius ** 2 * 3.14

print("The area of the circle is:", area_circle)


#String concatanation?

age_1 = '10 '
age_2 = '1'

print("Their combined age is:", age_1 + age_2)


word1 = 'pikachu'
word2 = 'nidoking'
print(word1 + ' ' + word2)




























