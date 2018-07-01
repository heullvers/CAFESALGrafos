#Classe que representa um grafo lido do arquivo
class Grafo(object):
	def __init__(self,listaVertices, listaArestas):
		self.vertices = listaVertices
		listaArestas.sort()
		self.arestas = listaArestas
