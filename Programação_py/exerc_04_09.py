# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 23:28:44 2020

@author: Andre
"""

def meuGrupo(arquivo, alvo):
    arq = open(arquivo, 'r')
    for linha in arq:
        if alvo in linha:
            print(linha, end=" ")

    
arquivo = "texto02.txt"
meuGrupo(arquivo, 'blank')