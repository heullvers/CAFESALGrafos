def listarArestas(arq):
	caminhoArquivo = arq
	arquivo = open(caminhoArquivo,'r')
	arquivo.readline()
	lista = []
	#Para cada linha do arquivo cria uma lista com os vértices pertencentes
	#à aresta. Ao final  temos como retorno uma lista de listas 
	#Cada elemento da lista final possui 3 valores(u, v, p) em que
	#u e v são vértices e p representa o peso da aresta.
	for linha in arquivo:
			lista.append(linha.split())
	arquivo.close()
	return lista

def floydWarshall(matrizAdj):
	matriz = matrizAdj.matriz
	n = len(matrizAdj.vertices)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if(int(matriz[i][k]) >= 0 and int(matriz[k][j]) >= 0 and i != j):
					if(((int(matriz[i][k]) + int(matriz[k][j])) < int(matriz[i][j])) or (int(matriz[i][j]) <= 0)):
						matriz[i][j] = str((int(matriz[i][k]) + int(matriz[k][j])))
	return matriz


def escolheDepositos(matrizAdj,p):
	matriz = matrizAdj.matriz[:]
	imprimirMatriz(matriz)
	n = len(matrizAdj.vertices)
	#Algoritmo
	for i in range(p-1):
		for i in range(n):
			if(i not in listaDeDepositos):
				for j in range(n):
					matriz[i][j] = matriz[i][j] - listaDasMenoresDistancias[j]
		#refazer somatório
		#menor índice
		listaDeDepositos.append(indiceDoMenor)
					
def geraMA(grafo):
	tamanhoListaVertices = len(grafo.vertices)
	tamanhoListaArestas = len(grafo.arestas)
	matriz = []
	#criação de uma matriz quadrada nula, sendo que seu tamanho é estabelecido pela quantidade de vértices
	for i in range(tamanhoListaVertices): 
		linha = []
		for j in range(tamanhoListaVertices):
			linha.append('0')
		matriz.append(linha)
	for i in range(tamanhoListaVertices): #percorrendo lista de vértices
		linha = []
		for j in range(tamanhoListaArestas): #percorrendo lista de arestas 
			if(str(i) == grafo.arestas[j][0]): #verifica se o vértice pertence a uma ligação de arestas
				for k in range(tamanhoListaVertices): #caso a afirmativa anterior seja verdadeira é feito um for para achar o segundo vértice da ligação
					if(str(k) == grafo.arestas[j][1]): #se k é igual segundo vértice da ligação
					#achado os vértices da ligação, em que "i" é a linha da matriz e "k" a coluna, insere-se o peso da aresta na matriz
						matriz[i][k] = grafo.arestas[j][2]
	
	#verificando matriz e colocando -1 para arestas que não existem
	for i in range(tamanhoListaVertices):
		for j in range(tamanhoListaVertices):
			if((i != j) and (matriz[i][j] == '0')):
				matriz[i][j] = -1 # -1 representa distância infinita, ocorre quando os vértices não possuem ligação diretamente
	return matriz

def imprimirMatriz(matriz):
	linhas = len(matriz)
	if (linhas != 0):
		colunas = len(matriz[0])
		for i in range(linhas):
			for j in range(colunas):
				print(matriz[i][j]," ",end = "")
			print()
	else:
		print("Matriz Vazia")

