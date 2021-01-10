l = ['cão','gato', 'coelho']
for i in l:
    print(i)

print('\n')

s = 'algoritmos'
for i in s:
    if i in 'aeiou':
        print(i)

print('\n')
        
for x in range(10):
    print(x)

print('\n')

l = ['a', 'b', 'c']
for i in range(len(l)):
    print(l[i])

print('\n')

for y in range(1, 20, 2):
    print(y)

print('\n')
# como calcular soma dos números pares de 1 a 100

soma=0
for i in range(2, 101, 2):
    soma = soma + i
print(soma)
    

print('\n')
# outra forma d calcular
acum=0
for i in range(1, 101):
    if i%2 == 0:
        acum = acum + i
print(soma)
    
print('\n')

str_list = ['João','Roberto', 'Rafael']
for nome in str_list:
    for c in nome:
        if c in 'aeiou':
            print(c)
        
