# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:16:02 2020

@author: Andre
"""

def f(x, y):  #definição de uma função parâmetros/argumentos de enrada x e y
    'função teste e texto para aparecer como documentação da função chamada pela função help'
    res = x**y + 1
    return res

print (f(3,2))
print (help(f))


