# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:40:52 2017

@author: graygoolsby
Name: Grayson Goolsby
Date: 04/18/17
Lab Section: X
"""

import hmmmAssembler 

# Greatest Common Divisor 
# inputs: integers n and m
# outputs: the greatest common divisor of n and m

# Register usage
# r1- integer n from user
# r2- integer m from user
# r3- temporary accumulator

GCD=""" 
00 read r1          # input integer n
01 read r2          # input integer m
02 copy r3 r1       # copy r1, n, to r3
03 copy r1 r2       # copy r2, m, to r1
04 mod r2 r3 r2     # find remainder of n/m, and place in r2
05 jeqzn r2 07      # if r2==0 jump to line 07
06 jgtzn r2 02      # if r2>0 jump to line 02
07 write r1         # print r1
08 halt             # stop
"""


# Least Common Multiple
# inputs: integers n and m
# output: the least common multiple of n and m

# Register usage
# r1- integer n from user
# r2- integer m from user
# r3- temporary accumulator
# r4- product of n and m

LCM="""
00 read r1          # input integer n
01 read r2          # input integer m
02 mul r4 r1 r2     # sets r4 to product of n and m
03 copy r3 r1       # copy r1, n, to r3
04 copy r1 r2       # copy r2, m, to r1
05 mod r2 r3 r2     # find remainder of n/m, and places in r2
06 jeqzn r2 08      # if m==0 jump to line 08
07 jgtzn r2 03      # if m>0 jump to line 03
08 div r3 r4 r1     # divides product of n and m by GCD of n and m
09 write r3         # prints least common multiple
10 halt             # stop
"""

# Power
# inputs: positive integers n and m
# output: n raised to m power

# Register usage
# r1- integer n from user
# r2- integer m from user
# r3- temporary accumulator
# r4- integer 1

Power="""
00 read r1       # input integer n
01 read r2       # input integer m
02 setn r4 1     # set r4 to 1
03 copy r3 r1    # set r3 equal to n
04 jeqzn r2 06   # if m==0 jump to line 06
05 jgtzn r2 08   # if m>0 jump to line 08
06 write r4      # print 1
07 halt          # stop
08 addn r2 -1    # subtract 1 from m
09 mul r1 r1 r3  # multiply r1 by n
10 addn r2 -1    # subtract 1 from m
11 jeqzn r2 12   # if m==0 jump to line 12
12 jgtzn r2 07   # if m>0 jump to line 07
13 write r1      # print r1
14 halt          # stop
"""


# Average
# inputs: integers
# output: average of inputs

# Register usage
# r1- number of integers to input from user
# r2- input accumulator 
# r3- temporary accumulator for sum
# r4- sum of inputs
# r5- temporary accumulator for number of inputs

Average="""
00 read r1             # input number of inputs
01 setn r4 0           # set r4 to 0
02 jeqzn r1 13         # if r1==0 jump to line 13
03 jgtzn r1 04         # if r1>0 jump to line 04
04 copy r5 r1          # copy number of inputs to r5
05 read r2             # input number
06 copy r3 r2          # copy input to r3
07 add r4 r3 r4        # add input to sum of inputs
08 addn r5 -1          # subtract 1 from remaining number of inputs
09 jeqzn r5 11         # if r5== 0 jump to line 11
10 jgtzn r5 05         # if r5>0 jump to line 05
11 div r3 r4 r1        # divides sum of inputs by number of inputs 
12 write r3            # prints average of inputs
13 halt                # stop
"""


# Fibonacci
# input: interger, n
# outputs: the first n Fibonacci numbers

# Register usage
# r1- interger n from user
# r2- n-1 Fibonacci number
# r3- n-2 Fibonacci number
# r4- temporary accumulator 


Fibonacci="""
00 read r1             # input number of Fibonacci's number
01 setn r2 1           # set r2 to 1
02 setn r3 1           # set r3 to 1
03 write r2            # print first Fibonacci number
04 write r3            # print second Fibonacci numbers
05 addn r1 -2          # subtract 1 from countdown
06 add r4 r3 r2        # sum next Fibonacci number
07 write r4            # print next Fibonacci number
08 copy r3 r2          # copy r2 to r3
09 copy r2 r4          # copy r4 to r2
10 addn r1 -1          # subtract one from countdown
11 jeqzn r1 13         # if r1==0 jump to line 13
12 jgtzn r1 06         # if r1>0 jump to line 06
13 halt                # stop
"""










hmmmAssembler.main(Fibonacci)