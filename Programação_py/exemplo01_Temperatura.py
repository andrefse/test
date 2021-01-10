# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:34:09 2020

@author: Andre
"""

temp_Cel = input('Informe a temperatura em Celsius: ')
print(type(temp_Cel))
temp_Cel = eval(temp_Cel)
print(type(temp_Cel))
temp_Fa = 1.8 * temp_Cel + 32.0
print('A temperatura em Fahrenheit é: ', temp_Fa)
