"""
!/usr/bin/env python
coding: utf-8
Python 3.7 (or higher)

Author: @Aleph_numbere
Date: 03-Nov-19

video: https://youtu.be/3gZC5763wYk

"""

#You have to install pynput -> pip install pynput
#           |
#          v
import pynput

from pynput.keyboard import Controller         #import all libs that we need
from time import sleep                         #This lib controls the duration of notes

kb = Controller()                              #this Object press the keys

b = 2       #Minims
np = 1.5    #Crotchets & point
n = 1       #Crotchets
cp = 0.75   #Quavers & point
c = 0.5     #Quavers
sc = 0.25   #Semiquavers

#This function really play the piano

def playPiano(notes, time):
    sleep(3)
    for i in range(len(time)):
        kb.press(notes[i])
        sleep(time[i])

#This function get the notes from a txt file, like the video

def getNotes(path):
    file = open(path, 'r')
    data = file.read()
    n = data.split(' ')
    return n

notes = getNotes(r'C:\Users\Whatever')      #The txt file where are the notes, in numbers(1,2,3, ...)

#The duration of each note

time = [c, n, cp, sc, n, c, c, n, cp, sc, n, c, c, n, c,
    c, n, c, c, n, c, c, np, c, n, cp, sc, n, c, c, n, cp,
    sc, n, c, c, n, c, c, n, c, c, n, cp, sc, b, b]

playPiano(notes, t)
