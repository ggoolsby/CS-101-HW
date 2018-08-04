# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:13:47 2017

@author: graygoolsby
"""

import string
import urllib


def analyze_file(filename):
    """analyzes a text file for most and least common words, as well as longest and shortest words
    however, the clean(s) function has trouble with '-' that occur between words"""
    fileData = open(filename, encoding="utf-8") 
    counts=dict()
    
    for line in fileData:
        line=clean(line)
        words = line.split()
        for word in words:
            word=word.lower()
            counts[word]=counts.get(word,0)+1
    mostCommon=word
    leastCommon=word
    shortest=word
    longest=word
    for word in counts:
        if counts[word]>counts[mostCommon]:
            mostCommon=word
        if counts[word]<counts[leastCommon]:
            leastCommon=word
        if len(word)<len(shortest):
            shortest=word
        if len(word)>len(longest):
            longest=word
    print(counts)
    return (mostCommon, leastCommon, shortest, longest)

def clean(s):
    """strips punctuation and whitespace from a word
    as noted in analyze_file doc string, this function has trouble with '-' within words"""
    for p in string.punctuation:
        s=s.replace(p,' ')
    s=s.strip()
    return s
    
    
    
def weather(zipcode):
    """returns the temp in farenheit at a zipcode"""
    URL = 'http://api.openweathermap.org/data/2.5/weather?zip='\
    + zipcode \
    +',us&appid=4bd44e422bc37d9761411c9efe4c1112&units=imperial'
    webpage = urllib.request.urlopen(URL)    
    contents = webpage.read()
    contents = contents.decode('ascii')
    d=eval(contents)
    temp=d['main']['temp']
    return temp
    
    

    