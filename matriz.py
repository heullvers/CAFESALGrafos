from grafo import *
import funcoes
class MatrizAdj(Grafo):
	def __init__(self, listaVertices, listaArestas, grafo):
		Grafo.__init__(self,listaVertices, listaArestas)
		self.grafo = grafo
		self.matriz = funcoes.geraMA(grafo)


