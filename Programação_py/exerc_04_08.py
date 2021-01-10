# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 22:26:41 2020

@author: Andre
"""

def palavras(arquivo):
    arq = open(arquivo, 'r')
    conteudo = arq.read()
    arq.close()
    tabela = str.maketrans('?!,.;:', 6*' ')
    conteudo=conteudo.translate(tabela)
    lista_palavras = conteudo.split()
    print(lista_palavras)

    
arquivo = "texto.txt"
palavras(arquivo)