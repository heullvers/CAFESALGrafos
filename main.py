# -*- coding: utf-8 -*-
import copy
from funcoes import *
from grafo import *
from matrizAdj import *
#nomeArquivo = ".txt"
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

#print("Arestas: ", grafo.arestas)
print("qnt arestas:", len(grafo.arestas))
print("qnt vertices:", len(grafo.vertices))
matrizAdj = MatrizAdj(grafo.vertices, grafo.arestas,grafo)
#print("Matriz Adjacencia")
#imprimirMatriz(matrizAdj.matriz)
print("Floyd-Warshall Iniciado")
floydWarshall(matrizAdj)
matrizCopia = copy.deepcopy(matrizAdj.matriz)
#Fazer conversão para as outras estruturas antes de modificar
#print()
print("Floyd-Warshall Finalizado")
#imprimirMatriz(matrizAdj.matriz)
print("Escolhendo Depósitos...")
listaDeDepositos = escolherDepositosMA(matrizAdj,qtdDepositos)
print("Depositos: ",listaDeDepositos)
#print("Matriz depois da escolha dos depositos:")
#imprimirMatriz(matrizAdj.matriz)
#print("copiaMatrizOriginal")
#imprimirMatriz(matrizCopia)
resultado = calcularSomatorioTotalMA(matrizAdj,listaDeDepositos)
print("Resultado: ",resultado)