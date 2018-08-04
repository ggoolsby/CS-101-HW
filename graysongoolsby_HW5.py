# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 09:44:07 2017

@author: graygoolsby

Name: Grayson Goolsby
Date: 03-22-17
Lab: X
"""
import turtle
    
def binary2decimal(bs):
    """converts a binary string to a decimal number"""
    if bs=='':
        return 0
    else:
        return binary2decimal(bs[:-1])*2+(int(bs[-1]))



def decimal2binary(n):
    """turns a decimal number into a binary string"""
    if n==0:
        return ''
    else:
        return decimal2binary(n//2)+str(n%2)
    
        
    
    
def GCD(a, b):
    """uses remainders to determine the greatest common divisor of two numbers, when a and b are positive integers"""
    rem=a%b
    if rem==0:
        return b
    else:       
        return GCD(b,rem)
    



def stairs(l, g):
    """draws recursive boxes in the pattern of stairs"""
    if g>0:
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
        turtle.left(90)
        
        stairs(l/2, g-1)

        turtle.backward(l)
        turtle.right(90)
        turtle.backward(l)
        turtle.left(90)
 

       
def drawStairsScene():
    """ 
    Moves the turtle to the top left of the screen and draws a staircase.
    """
    # pick up the pen and move the turtle so it starts at the left edge of the canvas 
    turtle.penup()
    turtle.goto(-turtle.window_width()/2 + 20, turtle.window_height()/2 - 20)
    turtle.pendown()    

    # draw the tree by calling your function
    stairs(300,7)

    # finished
    turtle.done()