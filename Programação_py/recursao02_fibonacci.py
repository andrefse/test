# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 01:03:44 2020

@author: Andre
"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(7))

""" Recursão """
def	fib_rec(n):
    if	n	<	2:
        return	n
    else:
        return	fib_rec(n-1)	+	fib_rec(n-2)

""" Iteração """
def	fib_it(n):
    res = n
    a, b = 0, 1
    for k in range(2, n+1):
        res = a + b
        a, b = b, res
    return res

""" Memoização """
m = dict()
def	fib_mem(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = fib_mem(n-1) + fib_mem(n-2)
        return	m[n]

import time    

n = 35
start = time.time()
print(fib_rec(n))
print('Recursive:{} seconds'.format(time.time() - start))
start = time.time()
print(fib_it(n))
print('Iterative:{} seconds'.format(time.time() - start))
start = time.time()
print(fib_mem(n))
print('Memoização:{} seconds'.format(time.time() - start))


