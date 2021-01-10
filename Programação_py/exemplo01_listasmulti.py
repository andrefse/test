def simetrica(a):
    nlinhas = len(a)
    ncolunas = len(a[0])

    for i in range(nlinhas):
        for j in range(i+1, ncolunas):
            if m[i][j] != m[j][i]:
                return False

    return True

m = [[1,2,3], [2,4,5], [3,2,3]]
print(simetrica(m))


# recebe matriz bidimensional e retorna a transposta

b = [['a','b','c'], ['x','y','z'], ['p','q','r']]

def transposta(b):
    nlinhas = len(b)
    ncolunas= len(b[0])
    transposta = [["","",""],["","",""],["","",""]]
    for i in range(nlinhas):
            for j in range(ncolunas):
                transposta[j][i] = b[i][j]

    print('A transposta da matriz é: ', transposta)
       
transposta(b)
