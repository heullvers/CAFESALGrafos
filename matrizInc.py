# -*- coding: utf-8 -*-
from grafo import *
from funcoes import *
class MatrizInc(object): # Classe que representa Matriz de incidência
	def __init__(self, listaVertices, listaArestas, grafo):
		Grafo.__init__(self,listaVertices, listaArestas)
		self.grafo = grafo
		self.matriz = funcoes.geraMI(grafo)
