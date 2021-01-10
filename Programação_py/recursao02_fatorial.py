# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 01:03:44 2020

@author: Andre
"""

def fatorial(n):
    if n>0:
        return n*fatorial(n-1)
    else:
        return 1 
    
print(fatorial(5))


""" ou pela definição usando recursão"""

def fati(n):
    if n == 0:
        return 1
    else:
        return n*fati(n-1)
    
print(fati(6))


""" Memoização """"
m = dict()
def	fat(n):
    if n == 0:
        return 1
    elif m.get(n)!=	None:  """ Verifica se o espaço'chave' já foi usado """
        return m[n]
    else:
        m[n] = n * fat(n-1)
        return m[n]

