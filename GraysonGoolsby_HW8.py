# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 09:50:08 2017

@author: graygoolsby
HW 8
Name: Grayson Goolsby
Date: 4-26-17
Lab: X
"""

def power(l, e):
    """ takes a list of numbers and a exponent and returns a new list of those numbers raised to the exponent""" 
    return [x**e for x in l]
    
def average(l):
    """takes a list and returns the average"""
    a=0
    for x in l:
        a+=x
    return a/len(l)

    
def pigLatin(s):
    """takes a string and returns the pig latin translation"""
    a=[]
    g=s.split()
    v=['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    for x in g:
        if len(x)==1:
            a.append(x)
        elif x[0] in v:
            a.append(x+'yay')
        else:
            a.append(x[1:]+x[0]+'ay')
    return ' '.join(a)
        



from PIL import Image



def justBlue(image):
    """Return a new image containing just the blue values from an image.

    The input should be a PIL image object created using something like
    image = Image.open(filename), where filename is a string.
    """
    # create a copy of the original image so we don't lose the original
    newImage = image.copy()

    # create our 2D structure of pixels from the image so we can work with individual pixels
    pixels = newImage.load()

    # get the bounding box -- this is returned as a tuple and we use some python
    # magic to automatically break the tuple up into four variables
    minX,minY,width,height = image.getbbox()

    # iterate over every pixel in the image
    for y in range(height):
        for x in range(width):
            # get the rgb value of the pixel (as a tuple in the order (red, green, blue))
            rgb = pixels[x,y]

            # set the pixel to a new RGB value (in this instance, we keep the original
            # blue value and set the red and green to 0)
            pixels[x,y] = (0,0, rgb[2])

    # return the new image
    return newImage
    
    
    
def grayScale(image):
    """Return a new image containing a gray scale from an image.

    The input should be a PIL image object created using something like
    image = Image.open(filename), where filename is a string.
    """
    # create a copy of the original image so we don't lose the original
    newImage = image.copy()

    # create our 2D structure of pixels from the image so we can work with individual pixels
    pixels = newImage.load()

    # get the bounding box -- this is returned as a tuple and we use some python
    # magic to automatically break the tuple up into four variables
    minX,minY,width,height = image.getbbox()

    # iterate over every pixel in the image
    for y in range(height):
        for x in range(width):
            # get the rgb value of the pixel (as a tuple in the order (red, green, blue))
            rgb = pixels[x,y]
            # average the red, green, and blue values
            avg=int((rgb[0]+rgb[1]+rgb[2])/3)
            # set the pixel to a RGB avg value
            pixels[x,y] = (avg, avg, avg)

    # return the new image
    return newImage




def mirror(image):
    """Return a new image that reflects the left side of a photo to the right side.

    The input should be a PIL image object created using something like
    image = Image.open(filename), where filename is a string.
    """
    # create a copy of the original image so we don't lose the original
    newImage = image.copy()

    # create our 2D structure of pixels from the image so we can work with individual pixels
    pixels = newImage.load()

    # get the bounding box -- this is returned as a tuple and we use some python
    # magic to automatically break the tuple up into four variables
    minX,minY,width,height = image.getbbox()

    # iterate over every pixel in the image
    for y in range(height):
        for x in range(width):
            # get the rgb value of the pixels for target and source image(as a tuple in the order (red, green, blue))
            rgb = pixels[x,y]
            rgb2 = pixels[(width-x-1)*.5,y]
            # set the pixel to a new target RGB value  
            pixels[x*.5,y] = (rgb2[0], rgb2[1], rgb2[2])
            # set the pixel to a new source RGB value
            pixels[width-x-1,y] = (rgb[0], rgb[1], rgb[2])

    # return the new image
    return newImage


def sepia(image):
    """Return a new image containing gray scale from an image and add a yellow tint to reflect chemical.

    The input should be a PIL image object created using something like
    image = Image.open(filename), where filename is a string.
    """
    # create a copy of the original image so we don't lose the original
    newImage = image.copy()

    # create our 2D structure of pixels from the image so we can work with individual pixels
    pixels = newImage.load()

    # get the bounding box -- this is returned as a tuple and we use some python
    # magic to automatically break the tuple up into four variables
    minX,minY,width,height = image.getbbox()

    # iterate over every pixel in the image
    for y in range(height):
        for x in range(width):
            # get the rgb value of the pixel (as a tuple in the order (red, green, blue))
            rgb = pixels[x,y]
            # average the RGB values
            avg=int((rgb[0]+rgb[1]+rgb[2])/3)
            if avg<63:
            # set the pixel to a new weighted RGB avg
                pixels[x,y] = (int(avg*1.1), avg, int(avg*.9))
            elif 62<avg<193:
            # set the pixel to a new weighted RGB avg
                pixels[x,y] = (int(avg*1.15), avg, int(avg*.85))
            else:
            # set the pixel to a new weighted RGB avg
                pixels[x,y] = (int(avg*1.08), avg, int(avg*.93))

    # return the new image
    return newImage
