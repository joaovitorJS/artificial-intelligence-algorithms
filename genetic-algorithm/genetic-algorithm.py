# Algoritmo Genético - Problema do caixeiro viajante 
# João Vitor de Oliveira 
# RGM: 38342
# Inteligência Artificial - 4° ano - Ciência da Computação

# Importações
import sys
import numpy as np 
import matplotlib.pyplot as plt
import time
import random
import pandas as pd # Usado para DataFrame


# Constantes/Parâmetros
RANDOM_SEED = 111

NUMERO_CIDADES = 20
NUMERO_POPULACAO = 100
PROBABILIDADE_MUTACAO = 0.05
CONVERGENCIA = 0.0001
NUMERO_GERACOES = 10

# Funções
#-----------------------------------------------------------------------#
# Calcula a distância euclidiana 
def calculaDistancia(x1, y1, x2, y2):
  distancia = np.sqrt((x1-x2)**2 + (y1-y2)**2)
  return distancia

#-----------------------------------------------------------------------#
# Calcula distância total entre no conjunto de cidades
def calculaDistanciaTotal(conjuntoCidades):
  distanciaTotal = 0
  conjunto = conjuntoCidades.copy()
  listaCidadesX = conjunto[0]
  listaCidadesY = conjunto[1]

  listaCidadesX.append(listaCidadesX[0])
  listaCidadesY.append(listaCidadesY[0])  

  numeroCidades = len(listaCidadesY)

  for i in range(numeroCidades-1):
    distancia = calculaDistancia(listaCidadesX[i], listaCidadesY[i], listaCidadesX[i+1], listaCidadesY[i+1])
    distanciaTotal = distanciaTotal + distancia
  
  distanciaTotal = distanciaTotal + calculaDistancia(listaCidadesX[-1], listaCidadesY[-1], listaCidadesX[0], listaCidadesY[0])

  listaCidadesX.pop(numeroCidades-1)
  listaCidadesY.pop(numeroCidades-1)

  return distanciaTotal

#-----------------------------------------------------------------------#
# Plot da configuração Inicial
def plotInicial(conjuntoCidades, axInicial):
  conjunto = conjuntoCidades.copy()
  listaCidadesX = conjunto[0]
  listaCidadesY = conjunto[1]

  listaCidadesX.append(listaCidadesX[0])
  listaCidadesY.append(listaCidadesY[0])  

  # Plot da configuração inicial
  axInicial.plot(listaCidadesX, listaCidadesY, color='c', marker='o', linewidth=1, markersize=6, markerfacecolor='r', markeredgecolor='m')
  
  distanciaInicial = calculaDistanciaTotal(conjuntoCidades)
  
  axInicial.set_title(f'Configuração Inicial\nDistância: {distanciaInicial} - Geração: {0}')

  listaCidadesX.pop(numeroCidades-1)
  listaCidadesY.pop(numeroCidades-1)

#-----------------------------------------------------------------------#
# Faz o plot das cidades conforme o conjunto passado
def plotCidades(populacao, ax, geracao, fig, isMelhor=False):
    
    listaCidadesX = []
    listaCidadesY = []
    for i in range(0, len(populacao)):
        listaCidadesX.append(populacao[i].x)
        listaCidadesY.append(populacao[i].y)

    conjuntoCidades = [listaCidadesX, listaCidadesY]  
     
    conjunto = conjuntoCidades.copy()
    listaCidadesX = conjunto[0]
    listaCidadesY = conjunto[1]
    
    listaCidadesX.append(listaCidadesX[0])
    listaCidadesY.append(listaCidadesY[0])  
    
    ax.clear()
    ax.plot(listaCidadesX , listaCidadesY, color='c', marker='o', linewidth=1, markersize=6, markerfacecolor='r', markeredgecolor='m')
    
    distancia = calculaDistanciaTotal(conjuntoCidades)
    
    if (geracao == -1):
        ax.set_title(f'Distância: {distancia} - Melhor Solução')
    else:
        ax.set_title(f'Distância: {distancia} - Geração: {geracao}')
    
    listaCidadesX.pop(numeroCidades-1)
    listaCidadesY.pop(numeroCidades-1)
    
    fig.canvas.draw()
    fig.canvas.flush_events()
    if (isMelhor):
      time.sleep(3.0)
    else:
      time.sleep(1.0)


class Coordenadas:
    def __init__(self, eixoX, eixoY):
        self.x = eixoX
        self.y = eixoY
        
    def calcularDistancia(self, coordenada):
        return np.sqrt((self.x - coordenada.x) ** 2 + (self.y - coordenada.y) ** 2)
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class Fitness:
    def __init__(self, rota):
        self.rota = rota
        self.distancia = 0
        self.fitness = 0.0
        
    def distanciaEntreCidades(self):
        if (self.distancia == 0):
            aux = 0
            for i in range(0, len(self.rota)):
                cidade1 = self.rota[i]
                cidade2 = None
                if (i + 1 < len(self.rota)):
                    cidade2 = self.rota[i+1]
                else:
                    cidade2 = self.rota[0]
                
                aux += cidade1.calcularDistancia(cidade2)
            
            self.distancia = aux
        
        return self.distancia
    
    def definirFitness(self):
        if (self.fitness == 0):
            self.fitness = 1/float(self.distanciaEntreCidades())
       
        return self.fitness

#-----------------------------------------------------------------------#
# Criando uma rota
def criarRota(conjuntoCidaddes):
    # random.sample = gera amostra aleatória => (lista, tamanho_amostra)
    return random.sample(conjuntoCidaddes, len(conjuntoCidaddes))

#-----------------------------------------------------------------------#
# Cria uma população inicial para o algorito
def criaPopulacaoInicial(tamPopulacao, conjuntoCidaddes):
    populacao = []
    
    for _ in range(0, tamPopulacao):
        populacao.append(criarRota(conjuntoCidaddes))
        
    return populacao

#-----------------------------------------------------------------------#
# Ordena a população a partir do fitness
def ordernaPopulacao(populacao):
    fitness = {}
    for i in range(0, len(populacao)):
        fitness[i] = Fitness(populacao[i]).definirFitness()
    
    return sorted(fitness.items(), reverse = True)

#-----------------------------------------------------------------------#
# Seleciona população apartir de seu fitness
def selecionaPopulacao(populacaoOrdenada, cromoTamanho):
    populacao = []
    df = pd.DataFrame(np.array(populacaoOrdenada), columns=['Index', 'Fitness'])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cumsum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range (0, cromoTamanho):
        populacao.append(populacaoOrdenada[i][0])
        
    for _ in range (0, len(populacaoOrdenada) - cromoTamanho):
        aux = 100 * random.random()
        for i in range(0, len(populacaoOrdenada)):
            if (aux <= df.iat[i, 3]):
                populacao.append(populacaoOrdenada[i][0])
                break
    
    return populacao

def casamento(populacao, populacaoSelecionada):
    casamentoList = []
    
    for i in range(0, len(populacaoSelecionada)):
        index = populacaoSelecionada[i]
        casamentoList.append(populacao[index])
    
    return casamentoList


def avaliacao(pai1, pai2):
    filho = []
    parteFilho1 = []
    parteFilho2 = []
    
    gene1 = int(random.random() * len(pai1))
    gene2 = int(random.random() * len(pai2))
    
    geneInicio = min(gene1, gene2)
    geneFim = max(gene1, gene2)
    
    for i in range(geneInicio, geneFim):
        parteFilho1.append(pai1[i])
        
    for i in pai2:
        if (i not in    parteFilho1):
            parteFilho2.append(i)
    
    filho = parteFilho1 + parteFilho2
    
    return filho

def cruzamento(cruzamento, cromoTamanho):
    filhos = []
    tam = len(cruzamento) - cromoTamanho
    auxList = random.sample(cruzamento, len(cruzamento))
    for i in range(0, cromoTamanho):
        filhos.append(cruzamento[i])
        
    for i in range(0, tam):
        filhos.append(avaliacao(auxList[i], auxList[len(cruzamento)-i-1]))
        
    return filhos

def mutacao(individual, probabilidadeMutacao):
    for i in range(len(individual)):
        if (random.random() < probabilidadeMutacao):
            index = int(random.random() * len(individual))
            cidade1 = individual[i]
            cidade2 = individual[index]
            
            individual[i] = cidade2
            individual[index] = cidade1
            
    return individual

def mutacaoPopulacional(populacao, probabilidadeMutacao):
    populacaoComMutacao = []
    for individual in range(0, len(populacao)):
        mutacaoDeUm = mutacao(populacao[individual], probabilidadeMutacao)
        populacaoComMutacao.append(mutacaoDeUm)

    return populacaoComMutacao

def criaNovaGeracao(populacaoCorrente, cromoTamanho, probabilidadeMutacao):
    populacaoOrdenada  = ordernaPopulacao(populacaoCorrente)
    populacaoSelecionada = selecionaPopulacao(populacaoOrdenada, cromoTamanho)
    resultadoCasamento = casamento(populacaoCorrente, populacaoSelecionada)
    filhos = cruzamento(resultadoCasamento, cromoTamanho)
    novaGeracao = mutacaoPopulacional(filhos, probabilidadeMutacao)

    return novaGeracao

         
def algoritmoGenetico(populacao, tamanhoPopulacao, cromoTamanho, probabilidadeMutacao, geracoes, fig, axCorrente):
    pop = criaPopulacaoInicial(tamanhoPopulacao, populacao) 
    
    progresso = []
    
    progresso.append(1 / ordernaPopulacao(pop)[0][1])
    
    for i in range(0, geracoes):
        pop  = criaNovaGeracao(pop, cromoTamanho, probabilidadeMutacao)
        progresso.append(1 / ordernaPopulacao(pop)[0][1])
        plotCidades(pop[ordernaPopulacao(pop)[0][0]], axCorrente, i, fig)
    
    
    distancias = ordernaPopulacao(pop)
    distancias = sorted(distancias, key=lambda x: x[1])
    print("Melhor distance: " + str(1 / distancias[len(distancias)-1][1]))
    plotCidades(pop[distancias[len(distancias)-1][0]], axCorrente, -1, fig, True)



print("* Algoritmo - Genético")
print("-"*50);

numeroCidades = 0
# se o número de ciddades foi passado nos argumentos
if (len(sys.argv) > 1) :
  numeroCidades = int(sys.argv[1])

# entrada do número de cidades
if (numeroCidades == 0):
  numeroCidades = int(input("Informe o número de cidades: "))

print(f"\nNúmero de cidades: {numeroCidades}\n")

# gerando configuração inicial
np.random.seed(seed=RANDOM_SEED)

populacaoInicial = []

for i in range(0, numeroCidades):
    populacaoInicial.append(Coordenadas(eixoX=int(random.random()*30), eixoY=int((random.random()*30)) ))

listaCidadesX = []
listaCidadesY = []
for i in range(0, len(populacaoInicial)):
    listaCidadesX.append(populacaoInicial[i].x)
    listaCidadesY.append(populacaoInicial[i].y)

configInicialCidade = [listaCidadesX, listaCidadesY]


#configurações dos plots
fig, ax = plt.subplots(1, 2, figsize=(5,5))

plotInicial(configInicialCidade, ax[0])

fig.suptitle("Algoritmo Genético - Problema do caixeiro viajante\n João Vitor de Oliveira", fontsize=16)
fig.tight_layout()


plt.ion()

fig.show()
fig.canvas.draw() 

algoritmoGenetico(populacao=populacaoInicial, tamanhoPopulacao=100, cromoTamanho=20, probabilidadeMutacao=0.01, geracoes=10, fig=fig,  axCorrente=ax[1])