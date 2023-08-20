#LECTURE 4

'''
1 IF ELSE
a. if
b. else
c. elif
------------------------------------------------
'''

x = int(input("enter an enteger for x:"))
if x > 1:
    print("x is greater than 1")
    # print "x is 1" whenever x is equal to 1
elif x == 1:
    print("x is 1")
else:
    print("x is less than 1")

'''
    greater than >
    less than <
    equals ==
    greater than or equal >=
    less than or equal <=
'''

'''
-------------------------------------------------
EXAMPLES

1. Write a program that takes an user integer as input.
You should write a prompt like this:
"Enter power level:"

and according to the input.

if the input is 0 - 500, the output is "Yamcha"
if the input is 500 - 10,000 the output is "Roshi"
if the input is 10,000 - 20,000 the output is "Gohan"
if the input is is 20, 000 - 50,000 the output is "Vegeta"
if the input is more than 50,000 the output is "Goku"
    
'''
power_level = int(input("Enter power level"))

if power_level >= 0 and power_level < 500:
    print("Yamcha")
elif power_level >= 500 and power_level < 10000:
    print("Master Roshi")
elif power_level >= 10000 and power_level<20000:
    print("Gohan")
elif power_level >= 20000 and power_level < 50000:
    print("Vegeta")
else:
    print("Goku")


#AND and OR
x = 60

if x> 50 or x>60:
    print("huge")


'''
2. STONE PAPER SCISSORS

INPUT                    OUTPUT
player 1: scissors       player 2 wins
player 2: stone
'''