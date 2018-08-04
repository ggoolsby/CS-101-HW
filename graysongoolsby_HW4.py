# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name: Grayson Goolsby
Date: 03-15-17
Lab: X
"""


        
import turtle 
import random

def drawTree(l, g):
    """Draws a recursive tree with random lengths and angles"""
    m=l+random.randint(-l//3,l//3)
    a=45+random.randint(-30,30)    
    if g>0:
        turtle.forward(m)
        turtle.right(a)
        
        drawTree(l*.5,g-1)
        turtle.left(a*2)
        
        drawTree(l*.5,g-1)
        turtle.right(a)
        turtle.backward(m)
   
        
    
    
def drawTreeScene():
    """ 
    Moves the turtle to the bottom of the screen, points it upward, and draws a tree.
    """
    # turn off drawing animation (too slow otherwise)
    turtle.tracer(False)
        
    # pick up the pen and move the turtle so it starts at the left edge of the canvas 
    turtle.penup()
    turtle.goto(0, -turtle.window_height()/2 + 20)
    turtle.left(90)
    turtle.pendown()    

    # draw the tree by calling your function
    drawTree(250,10)

    # finished
    turtle.update()
    turtle.done()
    
    
def drawTree1(l, g):
    """variation of drawTree function, length reduces less with each recursion"""
    m=l+random.randint(-l//5,l//5)
    a=45+random.randint(-20,20)
    if g>0:
        turtle.forward(m)
        turtle.right(a)
        
        drawTree1(l*.8,g-1)
        turtle.left(a*2)
        
        drawTree1(l*.8,g-1)
        turtle.right(a)
        turtle.backward(m)
        
def drawTree2(l, g):
    """variation of drawTree, "limb" width varies with length"""
    turtle.width(.095*l)
    a=30+random.randint(-10,10)
    b=30+random.randint(-10,10)
    m=l+random.randint(-l//4,l//4)
    if g>0:
        turtle.pencolor('saddle brown')
        turtle.forward(m)
        turtle.right(a)
        
        drawTree2(l*.7,g-1)
        turtle.left(a+b)
        
        turtle.pencolor('lawn green')
        drawTree2(l*.7,g-1)
        turtle.right(b)
        turtle.backward(m)

        
def drawScene():
    """draws a scene with three recursive trees, all of different colors"""
    turtle.tracer(False)
    
    turtle.penup()
    turtle.goto(-200, -turtle.window_height()/2 + 20)
    turtle.left(90)
    turtle.pendown()
    
    drawTree2(170,12)
    
    turtle.penup()
    turtle.goto(300, -turtle.window_height()/2 + 20)
    turtle.pendown()
    
    drawTree2(120,12)
    
    turtle.penup()
    turtle.goto(0, -turtle.window_height()/2 + 20)
    turtle.pendown()
    
    drawTree2(200,12)
    
    turtle.update()
    turtle.done()
        
        
        
        
def sierpinskiTriangle(l,g):
    """draws a sierpinski Triangle recursively for length 'l' and generations 'g'"""
    if g==1:
        turtle.forward(l)
        turtle.left(120)
        turtle.forward(l)
        turtle.left(120)
        turtle.forward(l)
        turtle.left(120)
    else:
        sierpinskiTriangle(l/2,g-1)
        turtle.forward(l/2)
        
        sierpinskiTriangle(l/2,g-1)
        turtle.backward(l/2)
        turtle.left(60)
        turtle.forward(l/2)
        turtle.right(60)
        
        sierpinskiTriangle(l/2,g-1)
        turtle.left(60)
        turtle.backward(l/2)
        turtle.right(60)        
        
        
        
        
        
def drawSierpinski():
    """
    Use this code to call your sierpinskiTriangle() function. This provides
    the functionality of turning off the tracer and running turtle.done().
    """

    # turn off animation (too slow otherwise)
    turtle.tracer(False)
	
    # pick up the pen and move the turtle so it starts at the left edge of the canvas
    turtle.penup()
    turtle.goto(-turtle.window_width()/2 + 20,-turtle.window_height()/2+20)
    turtle.pendown()
	
    sierpinskiTriangle(700, 9)
    
    # finish
    turtle.update()
    turtle.done()
    