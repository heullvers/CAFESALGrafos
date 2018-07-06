# -*- coding: utf-8 -*-
import copy
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
	indiceDoMenor = indiceDoMenorSomatorio(matriz,n,listaDeDepositos)
	#copiando as distâncias do primeiro depósito para a lista
	listaDasMenoresDistancias = matriz[indiceDoMenor][:]
	#adicionando primeiro depósito à lista
	listaDeDepositos.append(indiceDoMenor)
	#zera a coluna referente ao índice do primeiro depósito
	zerarColuna(matriz,indiceDoMenor,n)
	for k in range(1,p):
		#para cada iteração é feita uma cópia da matriz de distâncias original
		matrizCopia = copy.deepcopy(matrizAdj.matriz)
		#print("ORIGINAL")
		#imprimirMatriz(matrizAdj.matriz)
		for i in range(n):
			#realiza a operação para cada linha que ainda não se encontra na lista de depósitos
			if(i not in listaDeDepositos):
			#percorre toda a linha atribuindo aos valores a diferença entre as distâncias da própria linha e as distâncias do primeiro depósito
				for j in range(n):
					matrizCopia[i][j] = str(int(matrizCopia[i][j]) - int(listaDasMenoresDistancias[j]))
		#print("copia")
		#imprimirMatriz(matrizCopia)
		#refazendo somatório para a nova matriz e encontrando a linha com menor somatório que ainda não é um depósito
		indiceDoMenor = indiceDoMenorSomatorio(matriz,n,listaDeDepositos)
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
	#enquanto o indice do menor somatório for de um vértice que já é depósito a distância recebe o maior valor da lista 
	#o loop se mantém até que se tenha o índice do vértice com menor somatório de distâncias para que seja um novo depósito
	while(indiceDoMenor in listaDeDepositos):
		listaSomatorioLinhas[indiceDoMenor] = max(listaSomatorioLinhas)
		#print(indiceDoMenor)
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
		
		print("Menor distância até",j,": ",min(listaMenoresDistanciasCliente))
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
#===================================================Adaptar funções de conversão e criação das estruturas===========================================
#PRECISA VER SE É NECESSARIO MODIFICAR
#Função que gera uma matriz de incidência a partir de um grafo
def geraMI(grafo):
	#FAZER CASO DO LOOP
	lin = len(grafo.arestas)
	col = len(grafo.vertices)
	matriz = []
	for i in range(lin): #Percorrendo cada aresta
		linha = []
		for j in range(col): #Percorrendo cada vertice
			if str(j) in grafo.arestas[i][:2]: # Verifica se o vertice pertence àquela ligação(aresta, dois primeiros termos (u,v))
				if grafo.direcionado == False: # Se o grafo for não direcionado os pesos são simplesmente inseridos na matriz
					linha.append(grafo.arestas[i][2])
				elif str(j) == grafo.arestas[i][0]: #O peso do vértice de saída do arco se mantêm
					linha.append(grafo.arestas[i][2])
				else:
					linha.append('-' + grafo.arestas[i][2]) # Adiciona sinal negativo ao vértice de chegada do arco
			else:
				linha.append('0') # Insere 0 nas colunas dos vértices que não fazem parte da linha(aresta) analisada
		matriz.append(linha) # Insere cada linha na matriz	
	return matriz
#Função que converte uma Matriz de adjacência em uma Matriz de incidência
def converteMAparaMI(matriz,ehDirecionado, ehPonderado):
	tamanho = len(matriz)
	listaVertices = list(range(tamanho))
	listaArestas = []
	listaJaInseridos = []
	for i in range(tamanho):#Para cada posição da matriz verifica se tem uma ligação entre os vértices da posicção i e j
		for j in range(tamanho):
			if not ehDirecionado:#Verifica se o grafo é não direcionado
				if matriz[i][j] != '0' and [str(j),str(i),matriz[i][j]] not in listaJaInseridos:#Verifica se há uma ligação entre os vértices i e j, e se já foi inserida anteriormente 					
					listaArestas.append([str(i),str(j),matriz[i][j]]) #Insere na lista de arestas no formato (u,v,p)
					listaJaInseridos.append([str(i),str(j),matriz[i][j]])#Insere na lista as arestas já inseridas, para evitar a repetição de arestas
			elif matriz[i][j] != '0': #Verifica se tem uma ligação entre os vértices da posição i e j
					listaArestas.append([str(i),str(j),matriz[i][j]]) #Insere na lista de arestas no formato (u,v,p), sem verificação se a aresta já foi inserida(grafo direcionado)
	grafo = Grafo(listaVertices, listaArestas, ehDirecionado, ehPonderado) #Cria grafo auxiliar que será a entrada da geraMI
	return geraMI(grafo)


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



#PRECISA VER SE É NECESSARIO MODIFICAR
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
