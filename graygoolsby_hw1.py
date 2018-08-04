# -*- coding: utf-8 -*-
"""
CS 101 - Homework 1
@author: Grayson Goolsby
Lab: X
"""


"""
1. Python code to produce the following output:

0: 0
1: 1
2: 2
3: 3
4: 4
5: 5

The initial number and colon can be text (i.e., in quotes), but the second
copy of the number must be the result of an evaluated Python expression. 
This expression can use any of the arithmetic operators and parentheses. 
The challenge is that the only number we can use is the number 4. 
In addition, we use 4 (and only 4) of them.

The first line is given as an example.

"""
print("0:", 4 + 4 - 4 - 4)
print("1:", (4//4)*(4//4))
print("2:", (4*4)//(4+4))
print("3:", (4+4+4)//4)
print("4:", (4-4)*4+4)
print("5:", 4+(4**(4-4)))

"""
2. According to xkcd (https://xkcd.com/314/), the 'standard
creepiness rule' states that it is creepy to date someone under half
your age plus seven.  We calculate the youngest and oldest one could date
without violating this rule, and store these ages in variables lowerAge
and upperAge respectively. Some initial code and a print statement to
report the result is given.

"""

# the float() function here converts the string input to a floating point number
age = float(input('Enter your age: '))
lowerAge=.5*age+7
upperAge=2*(age-7)
print('Your dating pool stretches from',lowerAge,'to',upperAge)

"""
3. We are given a quantity of cups. We want to distribute
these to have the fewest number of containers, but we do not want to
waste space by not filling a container. The containers we have come in
gallon, quart, pint, and cup size. The last line (provided
below) will print out the contents of variables named gallons, quarts,
pints and cups.

Example: the user has entered 5 as the number of cups. We would report
0 gallons, 1 quarts, 0 pints, 1 cups

Challenge: The extra 's' on the end of the labels look weird when a
quantity is 1.  Can you fix this?  [It cannot be fixed using just what
we have seen in class so far so this will take some research]

[Hint: integer division and the % operator will be very useful in this problem.]
"""
# note we use the int() function to convert the string input to an integer so we can treat it as a number
userCups = int(input('Enter the number of cups: '))
gallons=userCups//16
a=userCups%16
quarts=a//4
b=userCups%4
pints=b//2
c=userCups%2
cups=c
if gallons==1: 
    print(gallons, 'gallon')
else:
    print(gallons, 'gallons')
if quarts==1:
    print(quarts, 'quart')
else:
    print(quarts, 'quarts')
if pints==1:
    print(pints, 'pint')
else:
    print(pints, 'pints')
if cups==1:
    print(cups, 'cup')
else:
    print(cups, 'cups')
print(" ")

"""
4. Practice with strings

The strings to print are:

fireman
banana
romana
time lord
man down
to be or not to be

"""

str1 = 'gallifrey'
str2 = 'cyberman'
str3 = 'doctor who'

# fireman
print(str1[5] + str1[4] + str1[6:8] + str2[5:])
# banana
print(str2[2]+str2[6:]+str2[6:]+str1[1])
# romana
print(str1[-3]+str3[-1]+str2[5:]+str1[1])
# time lord
print(str3[3]+str1[4]+str2[-3]+str1[7]+str3[6]+str1[2]+str3[1]+str1[-3]+str3[0])
# man down
print(str2[5:]+str3[6]+str3[0:2]+str3[-3]+str2[-1])
# to be or not to be
print(str3[3:5]+str3[6]+str2[2:4]+str3[6]+str3[4:6]+str3[6]+str2[-1]+str3[1]+str3[3]+str3[6]+str3[3:5]+str3[6]+str2[2:4])
