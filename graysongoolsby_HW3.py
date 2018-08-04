# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 09:34:06 2017

@author: graygoolsby
Name: Grayson Goolsby
Homework 3
Date: 2/28/17
Lab Section: X
"""

#HW3 prelab
import turtle
def drawSquare(length):
    """Draw square with side length= 'length'"""
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    

def drawSquareScene():
    """helper function to call drawSquare function"""
    drawSquare(100)
    turtle.done()
    
    
def drawKoch(length, generation):
    """draws the Koch curve"""
    if generation==0:
        turtle.forward(length)
    else:
        drawKoch((length/3),(generation-1))
        turtle.left(60)
        drawKoch((length/3),(generation-1))
        turtle.right(120)
        drawKoch((length/3),(generation-1))
        turtle.left(60)
        drawKoch((length/3),(generation-1))
            
    
    
def drawKochScene():
    """ Helper function to draw a preset Koch cure."""
	
    # pick up the pen and move the turtle so it starts at the left edge of the canvas 
    turtle.penup()
    turtle.goto(-turtle.window_width()/2 + 20,0)
    turtle.pendown()    
    
    # draw the curve by calling your function
    drawKoch(200, 3)
    
    # finished
    turtle.done()

#HW3
    
def drawSnowflake(length, generation):
    """draws a fractle of an equilateral triangle""" 
    drawKoch(length, generation)
    turtle.right(120)
    drawKoch(length, generation)
    turtle.right(120)
    drawKoch(length, generation)
    turtle.right(120)

        
def drawSnowflakeScene():
    """draws three different snowflakes of different sizes and with different colors"""
    turtle.tracer(False)    
    turtle.penup()
    turtle.goto(-300,225)
    turtle.pendown()
   
    turtle.pencolor("navy")
    turtle.fillcolor("cyan")
    turtle.begin_fill()
    drawSnowflake(200,3)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(100,-175)
    turtle.pendown()
    
    turtle.pencolor("midnight blue")
    turtle.fillcolor("dark slate gray")
    turtle.begin_fill()
    drawSnowflake(150,2)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(-300,-225)
    turtle.pendown()
    
    turtle.pencolor("firebrick")
    turtle.fillcolor("DeepPink2")
    turtle.begin_fill()
    drawSnowflake(75,1)
    turtle.end_fill()
    
    turtle.update()
 
   
def reverse(text):
    """reverses the string input"""
    if text=='':
        return ''
    else:
        return text[-1]+reverse(text[:-1])
 
   
def spiral(iL, a, m):
    """draw a loop with length iL that either collapses in to a fixed point or grows depending on the angle, a, until the line length exceeds 10000 or is smaller than 1"""       
    if iL>1 and iL<1000:
        turtle.forward(iL)
        turtle.right(a)
        spiral((iL*m), a, (m))
        turtle.right(a)
    
    
    
def drawSpiralScene():
    """draws two spirals of different shapes and sizes with different colors"""
    turtle.tracer(False)
    turtle.penup()
    turtle.goto(-250,250)
    turtle.pendown()
    
    turtle.pencolor("lawn green")
    turtle.fillcolor("light goldenrod")
    turtle.begin_fill()
    spiral(200,90,.9)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(45,0)
    turtle.pendown()
    
    turtle.pencolor("hot pink")
    turtle.fillcolor("maroon")
    turtle.left(180)
    turtle.begin_fill()
    spiral(300,92,.945)
    turtle.end_fill()
    
    turtle.update()
    