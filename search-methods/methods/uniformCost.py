# Método de busca de custo uniforme / Caminho mínimo ou Djkstra

import math

# Coloca todos os nós com uma distância infinita e retorna um dicionário com a cidade sendo a chave e a distância o valor
# Param:
#   nodes -> conjunto de nós da arvóre ou grafo
# Return: 
# [(Cidade, DistânciaInfinita),...]
def setAllNodesWithInfiniteDistance(nodes):
  distance = {}
  for node in nodes:
    keys = node.keys()
    nodeKey = list(keys)[0]
    distance[nodeKey] = math.inf
  
  return distance

# Retorna o Nó com a menor distância dentro da fila
def getNodeWithSmallestDistance(queue, distance):
  nodeSmallestDistance = None
  for node in queue: 
      if nodeSmallestDistance == None:
          nodeSmallestDistance = node
      elif distance[node] < distance[nodeSmallestDistance]:
          nodeSmallestDistance = node

  return nodeSmallestDistance

# Retorna o caminho mínimo da origem até os outros nós
# Params:
#   originKey -> de onde 
#   nodes -> conjunto de nós da arvóre ou grafo
# Return:
#   previous -> [{Cidade: CidadeAnterior}, ...]
#   distance -> [{Cidade: Custo até ela partindo da originKey(de onde)}]
def expansionProcess(originKey, nodes):
  visited = set()  # Conjunto dos nós visitados
  queue = []    # Fila
  previous = {}

  distance = setAllNodesWithInfiniteDistance(nodes) 

  distance[originKey] = 0 # Custo da origem até a origem

  queue.insert(0, originKey) # Insere a origem na fila
  visited.add(originKey) # Atualiza o nó como visitado
  while (len(queue) != 0):
    currentNodeKey = getNodeWithSmallestDistance(queue, distance)  

    queue.remove(currentNodeKey)
    
    currentNode = next((sub for sub in nodes if sub.get(currentNodeKey)), None) # Traz toda a estrutura da cidade: {Cidade: [{CidadeVizinha: Custo}]}
  
    for neighbour in currentNode[currentNodeKey]:
      keys = neighbour.keys()
      neighbourKey = list(keys)[0] # Nome da cidade
      costValue = neighbour[neighbourKey] # Distância / Custo entre a CidadeCorrente e sua Vizinha

      cost = distance[currentNodeKey] + costValue
      if (cost < distance[neighbourKey]):
        distance[neighbourKey] = cost
        previous[neighbourKey] = currentNodeKey
      
      if (neighbourKey not in visited):
         queue.insert(0, neighbourKey) # Insere a cidade vizinha na fila
         visited.add(neighbourKey) # Atualiza o nó como visitado

  return previous, distance

# Solução para o método de busca de custo uniforme
# Params:
#   originKey -> de onde 
#   destinationKey -> para onde
#   nodes -> conjunto de nós da arvóre ou grafo
# Informa o custo e caminho mínimo encontradp entre a cidade de origem e a de destino  -OU- Informa um erro 
def uniformCost(originKey, destinationKey, nodes):

  (previous, distance) = expansionProcess(originKey, nodes)

  path = []
  currentNode = destinationKey
  while currentNode != originKey:
      if currentNode not in previous:
          print("Caminho não encontrado! As cidade estão correta?")
          break
      else:
          path.insert(0, currentNode)
          currentNode = previous[currentNode]
  path.insert(0, originKey)

  if destinationKey in distance and distance[destinationKey] != math.inf:
      print('Custo do caminho mínimo ' + str(distance[destinationKey]))
      print('Caminho encontrado: ', end='')
      for p in path:
        print('-> ' + p, end='')
      print(flush=True)


