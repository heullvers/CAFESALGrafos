# -*- coding: utf-8 -*-
import copy
from grafo import *
from matrizAdj import *
from matrizInc import *
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
				if(int(matriz[i][k]) > 0 and int(matriz[k][j]) > 0 and i != j):
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
	#fazendo uma cópia da matriz
	matriz = copy.deepcopy(matrizAdj.matriz)
	#encontrando menor somatório
	indiceDoMenor = indiceDoMenorSomatorioMA(matriz,n,listaDeDepositos)
	#copiando as distâncias do primeiro depósito para a lista
	listaDasMenoresDistancias = matriz[indiceDoMenor][:]
	#adicionando primeiro depósito à lista
	listaDeDepositos.append(indiceDoMenor)
	#zera a coluna referente ao índice do primeiro depósito
	zerarColuna(matriz,indiceDoMenor,n)
	for k in range(1,p):
		#para cada iteração é feita uma cópia da matriz de distâncias original
		matrizCopia = copy.deepcopy(matrizAdj.matriz)
		for i in range(n):
			#realiza a operação para cada linha que ainda não se encontra na lista de depósitos
			if(i not in listaDeDepositos):
			#percorre toda a linha atribuindo aos valores a diferença entre as distâncias da própria linha e as distâncias do primeiro depósito
				for j in range(n):
					matrizCopia[i][j] = str(int(matrizCopia[i][j]) - int(listaDasMenoresDistancias[j]))
		#refazendo somatório para a nova matriz e encontrando a linha com menor somatório que ainda não é um depósito
		indiceDoMenor = indiceDoMenorSomatorioMA(matriz,n,listaDeDepositos)
		#adicinando próximo depósito
		listaDeDepositos.append(indiceDoMenor)
		#zera a coluna referente ao índice do novo depósito
		zerarColuna(matriz,indiceDoMenor,n)
		#modificando a lista das menores distâncias
		for i in range(n):
			#se o valor da distância do novo depósito for menor que o valor com mesmo índice na lista, o valor da lista é substituído pelo valor 
			#da distância do novo depósito até aquele ponto(representado pelo índice)
			if(int(matriz[indiceDoMenor][i]) < int(listaDasMenoresDistancias[i])):
				listaDasMenoresDistancias[i] = int(matriz[indiceDoMenor][i])
	return listaDeDepositos

#zera coluna da matriz correspondente ao depósito escolhido
def zerarColuna(matriz,indice,n):
	for i in range(n):
		matriz[i][indice] = '0'

def indiceDoMenorSomatorioMA(matriz, n,listaDeDepositos):
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
	#enquanto o indice do menor somatório for de um vértice que já é depósito a distância recebe o maior valor da lista 
	#o loop se mantém até que se tenha o índice do vértice com menor somatório de distâncias para que seja um novo depósito
	while(indiceDoMenor in listaDeDepositos):
		listaSomatorioLinhas[indiceDoMenor] = max(listaSomatorioLinhas)
		indiceDoMenor = listaSomatorioLinhas.index(min(listaSomatorioLinhas))
	return indiceDoMenor

#calcular soma total das distâncias
def calcularSomatorioTotalMA(matrizAdj,listaDeDepositos):
	n = len(matrizAdj.vertices)
	matriz = copy.deepcopy(matrizAdj.matriz)
	soma = 0
	for indice in listaDeDepositos:
			zerarColuna(matriz,indice,n)
	for j in range(n):
		listaMenoresDistanciasCliente = []
		for i in listaDeDepositos:
			if(int(matriz[i][j]) >= 0):
				listaMenoresDistanciasCliente.append(int(matriz[i][j]))
		soma += min(listaMenoresDistanciasCliente)

	return soma


def escolherDepositosMI(matrizInc,p):
	#n -> quantidade de vértices
	n = len(matrizInc.vertices)
	m = len(matrizInc.arestas)
	#lista de depósitos inicialmente vazia
	listaDeDepositos = []
	#fazendo uma cópia da matriz
	matriz = copy.deepcopy(matrizInc.matriz)
	#encontrando menor somatório
	indiceDoMenor = indiceDoMenorSomatorioMI(matriz,n,m,listaDeDepositos)
	#copiando as distâncias do primeiro depósito para a lista
	listaDasMenoresDistancias = matriz[:][indiceDoMenor]
	#adicionando primeiro depósito à lista
	listaDeDepositos.append(indiceDoMenor)
	#zera a linha referente ao índice do primeiro depósito
	zerarLinhas(matriz,indiceDoMenor,n,m)
	for k in range(1,p):
		#para cada iteração é feita uma cópia da matriz de distâncias original
		matrizCopia = copy.deepcopy(matrizInc.matriz)
		for j in range(n):
			#realiza a operação para cada coluna que ainda não se encontra na lista de depósitos
			if(j not in listaDeDepositos):
				#percorre toda a linha atribuindo aos valores a diferença entre as distâncias da própria coluna e as distâncias do primeiro depósito
				for i in range(m):
					matrizCopia[i][j] = str(int(matrizCopia[i][j]) - int(listaDasMenoresDistancias[j]))
		#refazendo somatório para a nova matriz e encontrando a linha com menor somatório que ainda não é um depósito
		indiceDoMenor = indiceDoMenorSomatorioMI(matriz,n,m,listaDeDepositos)
		#adicinando próximo depósito
		listaDeDepositos.append(indiceDoMenor)
		#zera a coluna referente ao índice do novo depósito
		zerarLinhas(matriz,indiceDoMenor,n,m)
		#modificando a lista das menores distâncias
		for j in range(n):
			for i in range(m):
				#se o valor da distância do novo depósito for menor que o valor com mesmo índice na lista, o valor da lista é substituído pelo valor 
				#da distância do novo depósito até aquele ponto(representado pelo índice)
				if(int(matriz[i][indiceDoMenor]) < int(listaDasMenoresDistancias[j])):
					listaDasMenoresDistancias[i] = int(matriz[i][indiceDoMenor])
	return listaDeDepositos

#zera todas as linhas que tem incidência no depósito escolhido
def zerarLinhas(matriz,indice,n,m):
	for i in range(m):
		#se alguma aresta indice no vertice depósito, toda linha recebe valor nulo
		if(int(matriz[i][indice]) > 0):
			for j in range(n):
				matriz[i][j] = '0'


def indiceDoMenorSomatorioMI(matriz,n,m,listaDeDepositos):
	listaSomatorioColunas = []
	#somando as distâncias de cada coluna da matriz (cada coluna representa um vértice)
	for j in range(n):
		if j not in listaDeDepositos:
			soma = 0;
			for i in range(m):
				soma += int(matriz[i][j])
			listaSomatorioColunas.append(soma)
		else:
			listaSomatorioColunas.append(1000*m)
	#encontrando o índice do menor somatório
	indiceDoMenor = listaSomatorioColunas.index(min(listaSomatorioColunas))
	#verificação para não haver repetição de vértices como depósitos
	#enquanto o indice do menor somatório for de um vértice que já é depósito a distância recebe o maior valor da lista 
	#o loop se mantém até que se tenha o índice do vértice com menor somatório de distâncias para que seja um novo depósito
	return indiceDoMenor

#calcular soma total das distâncias
def calcularSomatorioTotalMI(matrizInc,listaDeDepositos):
	n = len(matrizInc.vertices)
	m = len(matrizInc.arestas)
	matriz = copy.deepcopy(matrizInc.matriz)
	soma = 0
	for i in range(n):
		if( i not in listaDeDepositos):
			listaMenoresDistanciasCliente = []
			for j in listaDeDepositos:
				if(matrizInc.ehVizinho(str(j),str(i))):
					listaMenoresDistanciasCliente.append(int(matriz[i][j]))
			if(listaMenoresDistanciasCliente != []):
				soma += min(listaMenoresDistanciasCliente)
	return soma



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
				matriz[i][j] = '-1' 
	return matriz

#Função que gera uma matriz de incidência a partir de um grafo
def geraMI(grafo):
	lin = len(grafo.arestas)
	col = len(grafo.vertices)
	matriz = []
	for i in range(lin): #Percorrendo cada aresta
		linha = []
		for j in range(col): #Percorrendo cada vertice
			if str(j) in grafo.arestas[i][:2]: # Verifica se o vertice pertence àquela ligação(aresta, dois primeiros termos (u,v))
				if str(j) == grafo.arestas[i][0]: #O peso do vértice de saída do arco se mantêm
					linha.append(grafo.arestas[i][2])
				else:
					linha.append('0') # Adiciona sinal negativo ao vértice de chegada do arco
			else:
				linha.append('0') # Insere 0 nas colunas dos vértices que não fazem parte da linha(aresta) analisada
		matriz.append(linha) # Insere cada linha na matriz	
	return matriz
#Função que converte uma Matriz de adjacência em uma Matriz de incidência
def converteMAparaMI(matriz):
	tamanho = len(matriz)
	listaVertices = list(range(tamanho))
	listaArestas = []
	listaJaInseridos = []
	for i in range(tamanho):#Para cada posição da matriz verifica se tem uma ligação entre os vértices da posicção i e j
		for j in range(tamanho):
			if int(matriz[i][j]) > 0 : #Verifica se tem uma ligação entre os vértices da posição i e j
				listaArestas.append([str(i),str(j),matriz[i][j]]) #Insere na lista de arestas no formato (u,v,p), sem verificação se a aresta já foi inserida(grafo direcionado)
	grafo = Grafo(listaVertices, listaArestas) #Cria grafo auxiliar que será a entrada da geraMI
	matrizInc = MatrizInc(listaVertices, listaArestas,grafo)
	return matrizInc

#==========================================================================

def converteMAparaLA(matriz, ehDirecionado, ehPonderado):
	
	qntVertices = len(matriz)
	listaVertices = list(range(qntVertices))
	listaArestas = []
	for i in range(qntVertices):
		for j in range(qntVertices):
			if(matriz[i][j] != '0'): # é percorrida toda matriz e ao final é achada a lista de arestas
				listaArestas.append([str(i),str(j), matriz[i][j]])
	grafo = Grafo(listaVertices, listaArestas, ehDirecionado, ehPonderado)
	
	return geraLA(grafo) #geração da LA por meio do grafo instanciado



def geraLA(grafo):
	
	listaAdjacencia = []
	for i in range (len(grafo.vertices)):
		listaAdjacencia.append([])

	
	dicionario = {}
	for i in range (len(grafo.vertices)):
		dicionario[i] = listaAdjacencia[i]
	
	listinha1 = []
	listinha2 = []
	for i in range(len(grafo.arestas)): #é criado um dicionário, em que cada vértice possui sua chave. Os elementos do dicionário são as arestas
		listinha1.append(grafo.arestas[i][1])
		listinha1.append(grafo.arestas[i][2])
		listaAdjacencia[int(grafo.arestas[i][0])].append(listinha1)
		if(not grafo.direcionado):
			listinha2.append(grafo.arestas[i][0])
			listinha2.append(grafo.arestas[i][2])
			listaAdjacencia[int(grafo.arestas[i][1])].append(listinha2)
		listinha1 = []
		listinha2 = []

	return dicionario
#============================================================================
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
