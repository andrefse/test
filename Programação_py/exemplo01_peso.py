# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:54:59 2020

@author: Andre
"""

altura = input('Digite sua altura: ')
sexo = input('Digite h para homem ou m para mulher: ')
altura = eval(altura)

if sexo == 'h' :
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7
    
print('\nO peso ideal é: ', peso)