# -*- coding: utf-8 -*-
import sys
import copy
from funcoes import *
from grafo import *
from matrizAdj import *

arquivo = open("problemaB/" + sys.argv[1],"r")

primeiraLinha = arquivo.readline()
primeiraLinha = primeiraLinha.split()

qtdVertices = int(primeiraLinha[0])
qtdArestas = int(primeiraLinha[1])
qtdDepositos = int(primeiraLinha[2])

listaVertices = list(range(qtdVertices))
listaArestas = listarArestas("problemaB/" + sys.argv[1])
grafo = Grafo(listaVertices,listaArestas)
matrizAdj = MatrizAdj(grafo.vertices, grafo.arestas,grafo)
print("Floyd-Warshall Iniciado")
floydWarshall(matrizAdj)
matrizCopia = copy.deepcopy(matrizAdj.matriz)
print("Floyd-Warshall Finalizado")
print("Escolhendo Depósitos...")
listaDeDepositosMA = escolherDepositosMA(matrizAdj,qtdDepositos)
print("DepositosMA: ",listaDeDepositosMA)
resultadoMA = calcularSomatorioTotalMA(matrizAdj,listaDeDepositosMA)
print("ResultadoMA: ",resultadoMA)
print("Gerando Matriz de Incidência...")
matrizInc = converteMAparaMI(matrizAdj.matriz)
print("Escolhendo Depósitos...")
listaDeDepositosMI = escolherDepositosMI(matrizInc,qtdDepositos)
print("DepositosMI: ",listaDeDepositosMI)
resultadoMI = calcularSomatorioTotalMA(matrizAdj,listaDeDepositosMI)
print("ResultadoMI: ",resultadoMI)