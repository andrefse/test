
# encontrar o maior valor de n tal que n! < L

def nfat(L):
    n=0
    fat=1
    while (fat<=L):
        n+=1
        fat*=n
    return n-1

valor_L = eval(input('Entre com o valor de L, sendo ele inteiro positivo maior que zero: '))

while valor_L < 0:
    valor_L = eval(input('Entre com o valor de L, sendo ele inteiro positivo maior que zero: '))

print('o maior valor de n é: ', nfat(valor_L))



# criar lista de nomes enquanto ditidar algo diferente de vazio

l=[]
nome = input('Digite um nome: ')

while nome != '':
    l.append(nome)
    nome = input('Digite outro nome: ')

for i in l:
    print(i)

# uso do break e continue

def primo(num):
    i = 2
    while i < num:
        if num % i == 0:
            break
        i+=1
    return i==num

for n in range(2, 100):
    if not primo(n):
        continue
    print (n)
    
