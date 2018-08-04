# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:06:59 2017

@author: graygoolsby
Name: Gray Goolsby
Lab: X
Date: 5-5-17
"""

def mailbox(n):
    """returns a list of mailbox numbers that are closed after every 2nd is opened, /
    then every 3rd, up to every nth box is opened"""
    boxes=[0]*(n+1)
    list=[]
    start=0
    every=1
    for j in range(0, len(boxes)):
        start+=1
        every+=1
        for x in range(start, len(boxes), every):
            if boxes[x]==0:
                boxes[x]=1
            else:
                boxes[x]=0
    for m,h in enumerate(boxes):
        if h==0:
            list.append(m)
    return list[1:]