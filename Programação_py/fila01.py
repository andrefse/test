# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:40:30 2020

@author: Andre
"""

class Fila():
    def __init__(self):
        self.data = []
        
    def inserir(self, x):
        self.data.append(x)
        
    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        
    def empty(self):
        return not len(self.data) > 0
    
