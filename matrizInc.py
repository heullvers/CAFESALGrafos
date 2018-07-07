# -*- coding: utf-8 -*-
from grafo import *
from funcoes import *
class MatrizInc(object): # Classe que representa Matriz de incidência
	def __init__(self, listaVertices, listaArestas, grafo):
		Grafo.__init__(self,listaVertices, listaArestas)
		self.grafo = grafo
		self.matriz = funcoes.geraMI(grafo)

	def ehVizinho(self, vertice1 , vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			ehVizinho = False
			for i in range(len(self.arestas)):
				if (self.matriz[i][indice2] != '0') and (self.matriz[i][indice1] != '0'): # Se a coluna dos dois vertices é não nula na mesma linha, então são vizinhos
					ehVizinho = True		
			return ehVizinho
		else:
			return "O vertice escolhido não pertence ao grafo"

	def verificacaoParametrosEh(self, vertice1, vertice2):
			qntVertices = len(self.vertices)
			if((not vertice1 in self.vertices[0:qntVertices]) or (not vertice2 in self.vertices[0:qntVertices])): #Verifica se os vertices de entrada fazem parte dos vertices do grafo
				return False
			else:
				return True
