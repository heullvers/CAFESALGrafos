from funcoes import *
from grafo import *
from matriz import *

nomeArquivo = input("Digite o nome do arquivo: ")
caminhoArquivo = "problemaB/" + nomeArquivo
arquivo = open(caminhoArquivo,'r')
primeiraLinha = arquivo.readline()
primeiraLinha = primeiraLinha.split()

qtdVertices = primeiraLinha[0]
qtdArestas = primeiraLinha[1]
qtdDepositos = primeiraLinha[2]


print(qtdVertices,qtdArestas, qtdDepositos)

listaVertices = list(range(int(qtdVertices)))
listaArestas = listarArestas(caminhoArquivo)
grafo = Grafo(listaVertices,listaArestas)

print("Arestas: ", grafo.arestas)
print("qnt arestas:", len(grafo.arestas))
print("qnt vertices:", len(grafo.vertices))
matrizAdj = MatrizAdj(grafo.vertices, grafo.arestas,grafo)
imprimirMatriz(matrizAdj.matriz)
floydWarshall(matrizAdj)
indice = retornaIndiceDoMenorSomatorio(matrizAdj)
retornaListaDaLinhaDoMenorSomatorio(indice, )

