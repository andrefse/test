# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:44:55 2020

@author: Andre
"""



def olimpiadas(t):
    t.circle(50)
    t.penup()
    t.setx(110)
    t.pendown()
    t.circle(50)
    t.penup()
    t.setx(-110)
    t.pendown()
    t.circle(50)
    t.penup()
    t.goto(-55, -50)
    t.pendown()
    t.circle(50)
    t.penup()
    t.goto(55, -50)
    t.pendown()
    t.circle(50)

import turtle
s = turtle.Screen()
t = turtle.Turtle()
olimpiadas(t)