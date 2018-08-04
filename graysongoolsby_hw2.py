# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 09:55:36 2017

@author: graygoolsby
"""

"""
Name: Grayson Goolsby
Date: 3/1/17
Lab Section: X


# import error
import purple

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/graygoolsby/Documents/Spyder.app/Contents/Resources/middPython/lib/python3.5/site-packages/spyderlib/widgets/externalshell/sitecustomize.py", line 714, in runfile
    execfile(filename, namespace)
  File "/Users/graygoolsby/Documents/Spyder.app/Contents/Resources/middPython/lib/python3.5/site-packages/spyderlib/widgets/externalshell/sitecustomize.py", line 89, in execfile
    exec(compile(f.read(), filename, 'exec'), namespace)
  File "/Users/graygoolsby/Documents/untitled3.py", line 9, in <module>
    import purple
ImportError: No module named 'purple'


# index error
str1='bird dog'
print(str1[10])

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/graygoolsby/Documents/Spyder.app/Contents/Resources/middPython/lib/python3.5/site-packages/spyderlib/widgets/externalshell/sitecustomize.py", line 714, in runfile
    execfile(filename, namespace)
  File "/Users/graygoolsby/Documents/Spyder.app/Contents/Resources/middPython/lib/python3.5/site-packages/spyderlib/widgets/externalshell/sitecustomize.py", line 89, in execfile
    exec(compile(f.read(), filename, 'exec'), namespace)
  File "/Users/graygoolsby/Documents/untitled3.py", line 22, in <module>
    print(str1[10])
IndexError: string index out of range


# name error
hsadfhue

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/graygoolsby/Documents/Spyder.app/Contents/Resources/middPython/lib/python3.5/site-packages/spyderlib/widgets/externalshell/sitecustomize.py", line 714, in runfile
    execfile(filename, namespace)
  File "/Users/graygoolsby/Documents/Spyder.app/Contents/Resources/middPython/lib/python3.5/site-packages/spyderlib/widgets/externalshell/sitecustomize.py", line 89, in execfile
    exec(compile(f.read(), filename, 'exec'), namespace)
  File "/Users/graygoolsby/Documents/untitled3.py", line 37, in <module>
    hsadfhue
NameError: name 'hsadfhue' is not defined


# syntax error
def f(x)
    return 2*x

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/graygoolsby/Documents/Spyder.app/Contents/Resources/middPython/lib/python3.5/site-packages/spyderlib/widgets/externalshell/sitecustomize.py", line 714, in runfile
    execfile(filename, namespace)
  File "/Users/graygoolsby/Documents/Spyder.app/Contents/Resources/middPython/lib/python3.5/site-packages/spyderlib/widgets/externalshell/sitecustomize.py", line 89, in execfile
    exec(compile(f.read(), filename, 'exec'), namespace)
  File "/Users/graygoolsby/Documents/untitled3.py", line 51
    def f(x)
           ^
SyntaxError: invalid syntax


# type error
import math
a='dog'
math.sin(a)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/graygoolsby/Documents/Spyder.app/Contents/Resources/middPython/lib/python3.5/site-packages/spyderlib/widgets/externalshell/sitecustomize.py", line 714, in runfile
    execfile(filename, namespace)
  File "/Users/graygoolsby/Documents/Spyder.app/Contents/Resources/middPython/lib/python3.5/site-packages/spyderlib/widgets/externalshell/sitecustomize.py", line 89, in execfile
    exec(compile(f.read(), filename, 'exec'), namespace)
  File "/Users/graygoolsby/Documents/untitled3.py", line 69, in <module>
    math.sin(a)
TypeError: a float is required


# zero division error
def f(g):
    c=2/(g-g)
    return g

f(8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/graygoolsby/Documents/untitled3.py", line 84, in f
    c=2/(g-g)
ZeroDivisionError: division by zero
"""
    
    
def aspectRatio(width,height):
    """returns the ratio of width to height of a rectangle"""
    return 0 if height==0 else width/height

def flip(number):
    """takes a number, converts it to a string, flips it, and returns the flipped integer"""
    return int(str(number)[::-1])
    
def lastWord(s):
    """extracts the last word of a string"""
    import string
    for y in string.punctuation:
        s=s.replace(y,"")
    r=s.rstrip()
    t=r.rfind(' ')
    return r[(t+1):]
    