# Método de busca primeiro na profundidade (DFS - Depth-first search)
# Descrição simples: Expande o nodo mais profundo ainda não expandido

# Params :
#   origin -> de onde 
#   destination -> até onde
#   nodes -> conjunto de nós da arvóre ou grafo
def depthFirst(originKey, destinationKey, nodes):
  stack = [] # Pilha
  visited = set() # Lista com os nó visitados

  stack.append(originKey)

  while (len(stack) > 0):
    currentNodeKey = stack.pop()

    currentNode = next((sub for sub in nodes if sub.get(currentNodeKey)), None) # Traz toda a estrutura da cidade: {Cidade: [{CidadeVizinha: Custo}]}

    if (currentNodeKey == destinationKey):
      print('Cidade encontrada!')
      return True

    if (currentNodeKey not in visited):
      visited.add(currentNodeKey)


      for neighbour in  currentNode[currentNodeKey]:
        keys = neighbour.keys()
        neighbourKey = list(keys)[0] # Nome da cidade
        if (neighbourKey not in visited):
          stack.append(neighbourKey)
  
  print('Cidade não encontrada!')
  return False
