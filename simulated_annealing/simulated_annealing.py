# Simulated Annealing 
# João Vitor de Oliveira 
# RGM: 38342
# Inteligência Artificial - 4° ano - Ciência da Computação

# importações
import sys
import numpy as np
import matplotlib.pyplot as plt
import math as mt
import time

# constantes
RANDOM_SEED = None
TEMPERATURA_INICIAL = 100
TEMPERATURA_PARADA = 0.00005
NUMERO_ITERACOES = 50
FATOR_REDUCAO = 0.999999

#***********************************************************************#
# funções 

#-----------------------------------------------------------------------#
# gera o conjunto inicial das cidades 
def geraConfiguracaoInicial(numero, eixoX=30, eixoY=30):
 
  listaCidadesX = []
  listaCidadesY = []
  i = 0;
  while (i < numero):
    listaCidadesX.append(np.random.randint(eixoX))
    listaCidadesY.append(np.random.randint(eixoY))
    i = i+1

  return [listaCidadesX, listaCidadesY]

#-----------------------------------------------------------------------#
# Faz o plot das cidades conforme o conjunto passado
def plotCidades(conjuntoCidades, ax, energia, temperatura, fig):
  conjunto = conjuntoCidades.copy()
  listaCidadesX = conjunto[0]
  listaCidadesY = conjunto[1]

  listaCidadesX.append(listaCidadesX[0])
  listaCidadesY.append(listaCidadesY[0])  
  
  ax.clear()
  ax.plot(listaCidadesX , listaCidadesY, color='c', marker='o', linewidth=1, markersize=6, markerfacecolor='r', markeredgecolor='m')
  ax.set_title(f'Energia: {energia} - Temperatura: {temperatura}')

  listaCidadesX.pop(numeroCidades-1)
  listaCidadesY.pop(numeroCidades-1)
  
  fig.canvas.draw()
  fig.canvas.flush_events()
  time.sleep(1.0)


#-----------------------------------------------------------------------#
# Calcula distância euclidiana entre dois pontos (cidades)
def calculaDistancia(x1, y1, x2, y2):
  distancia = mt.sqrt((x1-x2)**2 + (y1-y2)**2)
  return distancia

#-----------------------------------------------------------------------#
# Calcula a energia, ou seja, a distância total entre todas as cidades
def calculaEnergia(conjuntoCidades):
  energia = 0
  conjunto = conjuntoCidades.copy()
  listaCidadesX = conjunto[0]
  listaCidadesY = conjunto[1]

  listaCidadesX.append(listaCidadesX[0])
  listaCidadesY.append(listaCidadesY[0])  

  numeroCidades = len(listaCidadesY)

  for i in range(numeroCidades-1):
    distancia = calculaDistancia(listaCidadesX[i], listaCidadesY[i], listaCidadesX[i+1], listaCidadesY[i+1])
    energia = energia + distancia
  
  energia = energia + calculaDistancia(listaCidadesX[-1], listaCidadesY[-1], listaCidadesX[0], listaCidadesY[0])

  listaCidadesX.pop(numeroCidades-1)
  listaCidadesY.pop(numeroCidades-1)

  return energia

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
  energiaInicial = calculaEnergia(conjuntoCidades)
  axInicial.set_title(f'Configuração Inicial\nEnergia: {energiaInicial}')

  listaCidadesX.pop(numeroCidades-1)
  listaCidadesY.pop(numeroCidades-1)

#-----------------------------------------------------------------------#
# Calcula a probabilidade de testes
def calculaProbabilidade(energiaAntiga, energiaNova, temperatura):
  if (energiaNova < energiaAntiga):
    return 1.0
  
  return mt.exp(((energiaAntiga-energiaNova)*1.0/temperatura))

#-----------------------------------------------------------------------#
# Faz uma inversão de dois valores no conjunto de cidades 
def inversao(conjuntoCidades):
  listaEixoX = conjuntoCidades[0]
  listaEixoY = conjuntoCidades[1]
  tamanho = len(listaEixoX)
  i = np.random.randint(tamanho)

  if (i+4 < tamanho):
    listaEixoX[i:i+4] = listaEixoX[i:i+4][::-1]
    listaEixoY[i:i+4] = listaEixoY[i:i+4][::-1]
  elif (i-4 >= 0):
    listaEixoX[i-4:i] = listaEixoX[i-4:i][::-1]
    listaEixoY[i-4:i] = listaEixoY[i-4:i][::-1]

  return [listaEixoX, listaEixoY]

#-----------------------------------------------------------------------#
# Faz uma translação de dois valores no conjunto de cidades para uma posição aleatória
def transalacao(conjunto):
  conjuntoCidades = conjunto.copy()
  listaEixoX = conjuntoCidades[0]
  listaEixoY = conjuntoCidades[1]
  tamanho = len(listaEixoX)

  posicaoEscolhida = np.random.randint(1, tamanho-1)
  primeiroValorX = listaEixoX.pop(posicaoEscolhida)
  primeiroValorY = listaEixoY.pop(posicaoEscolhida)

  novaPosicao = np.random.randint(1, tamanho-2)
  if (novaPosicao == posicaoEscolhida):
    novaPosicao = novaPosicao - 1

  listaEixoX.insert(novaPosicao, primeiroValorX)
  listaEixoY.insert(novaPosicao, primeiroValorY)

  return [listaEixoX, listaEixoY]

#-----------------------------------------------------------------------#
# Faz uma translação de dois valores no conjunto de cidades para uma posição aleatória
def troca(conjuntoCidades):
  listaEixoX = conjuntoCidades[0]
  listaEixoY = conjuntoCidades[1]
  tamanho = len(listaEixoX)
  
  posicaoParaTroca = np.random.randint(0, tamanho)
  novaPosicao = np.random.randint(0, tamanho)

  listaEixoX[posicaoParaTroca], listaEixoX[novaPosicao] = listaEixoX[novaPosicao], listaEixoX[posicaoParaTroca]

  listaEixoY[posicaoParaTroca], listaEixoY[novaPosicao] = listaEixoY[novaPosicao], listaEixoY[posicaoParaTroca]

  return [listaEixoX, listaEixoY]


#-----------------------------------------------------------------------#
# Executa o algoritmo Simulated Annealing
def simulatedAnnealing(conjuntoCidades, axCorrente, fig):
  temperatura = TEMPERATURA_INICIAL
  energia = calculaEnergia(conjuntoCidades)
  plotCidades(conjuntoCidades, axCorrente, energia, temperatura, fig)
  conjuntoCorrenteCidades = conjuntoCidades.copy()
  novaRotaExiste = True
  iteracoes = 0
  total = 0;
  melhor = conjuntoCidades.copy()
  while (temperatura > TEMPERATURA_PARADA and total < NUMERO_ITERACOES):
    novaRotaExiste = False
   
    energiaCorrente = calculaEnergia(conjuntoCorrenteCidades)

    p = np.random.random()

    novoConjunto = []
    # Pertubações
    if (p < 0.3):
      # print('[LOG]- Realizou Inversão')
      novoConjunto = inversao(conjuntoCorrenteCidades)
    elif (p < 0.6):
      # print('[LOG]- Realizou Translação')
      novoConjunto = transalacao(conjuntoCorrenteCidades)
    else:
      # print('[LOG]- Realizou Troca')
      novoConjunto = troca(conjuntoCorrenteCidades)

    energiaNova = calculaEnergia(novoConjunto)

    prob = calculaProbabilidade(energiaAntiga=energiaCorrente, energiaNova=energiaNova, temperatura=temperatura)

    if (prob >= np.random.random()):
      energiaCorrente = energiaNova
      if (energiaCorrente < energia):
        energia = energiaCorrente
        novaRotaExiste = True

    if (novaRotaExiste):
      iteracoes = iteracoes + 1
      total = total + 1
      melhor = conjuntoCorrenteCidades.copy()
      if (iteracoes == 3):
        plotCidades(melhor, axCorrente, energia, temperatura, fig)
        
        iteracoes = 0

    conjuntoCorrenteCidades = novoConjunto.copy()
    temperatura = temperatura*FATOR_REDUCAO
   
    

  plotCidades(melhor, axCorrente, energia, temperatura, fig)

  print(melhor)
  print(energia)  
  time.sleep(10.0)

#***********************************************************************#
# inicio
#-----------------------------------------------------------------------#

print("* Algoritmo - Simulated Annealing")
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
configInicialCidade = geraConfiguracaoInicial(numeroCidades)

#configurações dos plots
fig, ax = plt.subplots(1, 2, figsize=(5,5))

plotInicial(configInicialCidade, ax[0])


fig.suptitle("Simulated Annealing - Problema do caixeiro viajante\n João Vitor de Oliveira", fontsize=16)
fig.tight_layout()

# Deixar em tela cheia
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

plt.ion()

fig.show()
fig.canvas.draw() 

simulatedAnnealing(configInicialCidade, ax[1], fig)