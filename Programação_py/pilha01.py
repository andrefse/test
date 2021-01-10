# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:49:50 2020

@author: Andre
"""

class Pilha():
    def __init__(self):
        self.data = []
        
    def push(self, x): """ insere elemento na pilha"""
        self.data.append(x)
        
    def pop(self): """ retira elemento da pilha"""
        if len(self.data) > 0:
            return self.data.pop(-1)
    
    def top(self): """ se tivr elemento consulta"""
        if len(self.data) > 0:
            return self.data[-1]
        
    def empty(self): """ verifica se a pilha está vazia"""
        return not len(self.data) > 0
    
        