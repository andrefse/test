x=input('Digite uma palavra')

def vogais(x):
    for i in range(len(x)):
        if(x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u' or x[i]=='A' or x[i]=='E' or x[i]=='I' or x[i]=='O' or x[i]=='U'):
            print(x[i])

vogais(x)
        
