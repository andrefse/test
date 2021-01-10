# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 13:19:00 2020

@author: Andre
Média de notas de um aluno
"""

n1 = input('Entre com a 1ª nota: ')
n2 = input('Entre com a 2ª nota: ')
n1 = eval(n1)
n2 = eval(n2)

media = 0.4*n1 + 0.6*n2

if media >= 5:
    print('\nO aluno foi aprovado com media ', media)
else:
    print('\nO aluno foi reprovado com media ', media)