nomeArquivo = input("Digite o nome do arquivo: ")
caminhoArquivo = "problemaB/" + nomeArquivo
arquivo = open(caminhoArquivo,'r')
primeiraLinhaTeste = arquivo.readline()

print(primeiraLinhaTeste)
