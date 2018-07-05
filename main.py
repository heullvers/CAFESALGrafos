# -*- coding: utf-8 -*-
from funcoes import *
from grafo import *
from matriz import *

nomeArquivo = input("Digite o nome do arquivo: ")
caminhoArquivo = "problemaB/" + nomeArquivo
arquivo = open(caminhoArquivo,'r')
primeiraLinha = arquivo.readline()
primeiraLinha = primeiraLinha.split()

qtdVertices = int(primeiraLinha[0])
qtdArestas = int(primeiraLinha[1])
qtdDepositos = int(primeiraLinha[2])


print(qtdVertices,qtdArestas, qtdDepositos)

listaVertices = list(range(qtdVertices))
listaArestas = listarArestas(caminhoArquivo)
grafo = Grafo(listaVertices,listaArestas)

print("Arestas: ", grafo.arestas)
print("qnt arestas:", len(grafo.arestas))
print("qnt vertices:", len(grafo.vertices))
matrizAdj = MatrizAdj(grafo.vertices, grafo.arestas,grafo)
imprimirMatriz(matrizAdj.matriz)
floydWarshall(matrizAdj)
#Fazer conversão para as outras estruturas antes de modificar
print()
imprimirMatriz(matrizAdj.matriz)
print(escolherDepositosMA(matrizAdj,qtdDepositos))
imprimirMatriz(matrizAdj.matriz)
