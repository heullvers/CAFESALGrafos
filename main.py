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
print(
matrizAdj = MatrizAdj(grafo.vertices, grafo.arestas,grafo)
print("Floyd-Warshall Iniciado")
floydWarshall(matrizAdj)
matrizCopia = copy.deepcopy(matrizAdj.matriz)
print("Floyd-Warshall Finalizado")
imprimirMatriz(matrizAdj.matriz)
print("Escolhendo Depósitos...")
listaDeDepositosMA = escolherDepositosMA(matrizAdj,qtdDepositos)
print("DepositosMA: ",listaDeDepositosMA)
resultadoMA = calcularSomatorioTotalMA(matrizAdj,listaDeDepositosMA)
print("ResultadoMA: ",resultadoMA)
print("Matriz Adjacência:")
imprimirMatriz(matrizAdj.matriz)
matrizInc = converteMAparaMI(matrizAdj.matriz)
print("Gerando Matriz de Incidência...")
imprimirMatriz(matrizInc.matriz)
print("Escolhendo Depósitos...")
listaDeDepositosMI = escolherDepositosMI(matrizInc,qtdDepositos)
print("DepositosMI: ",listaDeDepositosMI)
resultadoMI = calcularSomatorioTotalMI(matrizInc,listaDeDepositosMI)
print("ResultadoMI: ",resultadoMI)