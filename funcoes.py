# -*- coding: utf-8 -*-
def listarArestas(arq):
	#Para cada linha do arquivo cria uma lista com os vértices pertencentes
	#à aresta. Ao final  temos como retorno uma lista de listas 
	#Cada elemento da lista final possui 3 valores(u, v, p) em que
	#u e v são vértices e p representa o peso da aresta.
	caminhoArquivo = arq
	arquivo = open(caminhoArquivo,'r')
	arquivo.readline()
	lista = []
	#percorre arquivo pegando os valor de cada linha (u,v,p)
	for linha in arquivo:
			lista.append(linha.split())
	arquivo.close()
	return lista


def floydWarshall(matrizAdj):
	matriz = matrizAdj.matriz
	#n -> quantidade de vértices
	n = len(matrizAdj.vertices)
	for k in range(n):
		#percorrendo linhas
		for i in range(n):
			#percorrendo colunas
			for j in range(n):
				#para todo intermediário nas posições [i] [k] e [k] [j que sejam diferentes de 0
				if(int(matriz[i][k]) >= 0 and int(matriz[k][j]) >= 0 and i != j):
					#se soma do caminho com os intermediários for menor que seguir uma aresta direta
					# substituir o  valor na posição [i][j]
					if(((int(matriz[i][k]) + int(matriz[k][j])) < int(matriz[i][j])) or (int(matriz[i][j]) <= 0)):
						matriz[i][j] = str((int(matriz[i][k]) + int(matriz[k][j])))
	return matriz


def escolherDepositosMA(matrizAdj,p):
	#n -> quantidade de vértices
	n = len(matrizAdj.vertices)
	#lista de depósitos inicialmente vazia
	listaDeDepositos = []
	matriz = matrizAdj.matriz[:]
	#encontrando menor somatório
	indiceDoMenor = indiceDoMenorSomatorio(matriz,n,listaDeDepositos)
	#copiando as distâncias do primeiro depósito para a lista
	listaDasMenoresDistancias = matriz[indiceDoMenor][:]
	#adicionando primeiro depósito à lista
	listaDeDepositos.append(indiceDoMenor)
	#zera a coluna referente ao índice do primeiro depósito
	zerarColuna(matrizAdj.matriz,indiceDoMenor,n)
	for k in range(1,p):
		#para cada iteração é feita uma cópia da matriz de distâncias original
		matriz = matrizAdj.matriz[:]
		for i in range(n):
			#realiza a operação para cada linha que ainda não se encontra na lista de depósitos
			if(i not in listaDeDepositos):
			#percorre toda a linha atribuindo aos valores a diferença entre as distâncias da própria linha e as distâncias do primeiro depósito
				for j in range(n):
					matriz[i][j] = str(int(matriz[i][j]) - int(listaDasMenoresDistancias[j]))
		#refazendo somatório para a nova matriz e encontrando a linha com menor somatório que ainda não é um depósito
		indiceDoMenor = indiceDoMenorSomatorio(matriz,n,listaDeDepositos)
		#adicinando próximo depósito
		listaDeDepositos.append(indiceDoMenor)
		#zera a coluna referente ao índice do novo depósito
		zerarColuna(matrizAdj.matriz,indiceDoMenor,n)
		#modificando a lista das menores distâncias
		for i in range(n):
			#se o valor da distância do novo depósito for menor que o valor com mesmo índice na lista, o valor da lista é substituído pelo valor 
			#da distância do novo depósito até aquele ponto(representado pelo índice)
			if(int(matriz[indiceDoMenor][i]) < int(listaDasMenoresDistancias[i])):
				listaDasMenoresDistancias[i] = int(matriz[indiceDoMenor][i])
	return listaDeDepositos

def zerarColuna(matriz,indice,n):
	for i in range(n):
		matriz[i][indice] = 0

def indiceDoMenorSomatorio(matriz, n,listaDeDepositos):
	listaSomatorioLinhas = []
	#somando as distâncias de cada linha da matriz
	for i in range(n):
		soma = 0;
		for j in range(n):
			soma += int(matriz[i][j])
		listaSomatorioLinhas.append(soma) 
	#encontrando o índice do menor somatório
	indiceDoMenor = listaSomatorioLinhas.index(min(listaSomatorioLinhas))
	#verificação para não haver repetição de vértices como depósitos
	#enquanto o indice do menor somatório for de um vértice depósito a distância recebe um valor muito alto e não é mais o menor somatório
	#o loop se mantém até que se tenha o índice do vértice com menor somatório de distâncias para que seja um novo depósito
	while(indiceDoMenor in listaDeDepositos):
		listaSomatorioLinhas[indiceDoMenor] = 1000
		indiceDoMenor = listaSomatorioLinhas.index(min(listaSomatorioLinhas))

	return indiceDoMenor


def geraMA(grafo):
	qtdVertices = len(grafo.vertices)
	qtdArestas = len(grafo.arestas)
	matriz = []
	#criação de uma matriz quadrada nula, sendo que seu tamanho (nxn) é estabelecido pela quantidade de vértices
	for i in range(qtdVertices): 
		linha = []
		for j in range(qtdVertices):
			linha.append('0')
		matriz.append(linha)
	#percorrendo lista de vertices
	for i in range(qtdVertices): 
		linha = []
		for j in range(qtdArestas):
			#verifica se o vértice (u) pertence a alguma aresta (u,v)
			if(str(i) == grafo.arestas[j][0]):
				#procura o segundo vertice (v) da aresta (u,v)
				for k in range(qtdVertices):
					#como a posição referente à aresta foi encontrada seu peso é inserido na matriz
					if(str(k) == grafo.arestas[j][1]):
						matriz[i][k] = grafo.arestas[j][2]
	
	#verificando matriz e colocando -1 para arestas que não existem
	for i in range(qtdVertices):
		for j in range(qtdVertices):
			#todas as posições (exceto a diagonal principal) que ficaram com valor nulo mesmo após a inserção
			if((i != j) and (matriz[i][j] == '0')):
				# -1 representa distância infinita, ocorre quando os vértices não possuem ligação diretamente
				matriz[i][j] = -1 
	return matriz

def imprimirMatriz(matriz):
	#percorre linhas e colunas de uma matriz imprimindo seus valores
	linhas = len(matriz)
	if (linhas != 0):
		colunas = len(matriz[0])
		for i in range(linhas):
			for j in range(colunas):
				print(matriz[i][j]," ",end = "")
			print()
	else:
		print("Matriz Vazia")
