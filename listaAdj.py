# -*- coding: utf-8 -*-
from grafo import *
from funcoes import *
class ListaAdj(Grafo):
	def __init__(self, listaVertices, listaArestas,grafo):
		Grafo.__init__(self,listaVertices, listaArestas)
		self.grafo = grafo
		self.lista = funcoes.geraLA(grafo)
