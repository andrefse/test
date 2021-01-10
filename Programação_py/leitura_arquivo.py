# leitura de arquivo
def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.seek(0)  # volta o poneiro para o início do arquivo
    l = infile.readlines()
    infile.close()
    print("O texto do arquivo é: \n", content)
    wordList = content.split()
    print("As palavras do arquivo são: \n", wordList)
    print('Linha 1: ', l[3])
    return len(wordList), len(content)

n_words, n_chars = readFile('teste.txt')
print("O número de palavras e o comero de caracteres são respectivamente: \n" , n_words, n_chars)


outfile = open('teste.txt', 'a') # substitui w por a
outfile.write('Olá classe!\n')  
outfile.close()
