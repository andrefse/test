a = eval(input('Digite o lado 1: '))
b = eval(input('Digite o lado 2: '))
c = eval(input('Digite o lado 3: '))

maior_lado = 0
if a > maior_lado:
    maior_lado = a
if b > maior_lado:
    maior_lado = b
if c > maior_lado:
    maior_lado = c


'''
no python pode ser usado a função
maior_lado = max(a, b,c)
'''

if maior_lado < a + b + c - maior_lado:
    print('Os lados formam um triângulo!')
    if a==b and b==c:
        print('O triângulo é equilátero')
    elif a != b and b != c and a != c:
        print('O triângulo é escaleno!')
    else :
        print('O triângulo é isósceles!')
    
else:
    print('Os lados não formam um triângulo')
