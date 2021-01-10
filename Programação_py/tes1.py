i=1
print('Você irá digitar 3 notas!')
N=3
somatoria=0
X=4
while(i<=N):
    print('Insira a nota ', i)
    nota = eval(input())
    somatoria = somatoria + (1/(nota+X))
    i= i+1
H=(N/somatoria)-X
print(H)
