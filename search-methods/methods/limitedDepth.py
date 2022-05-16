# Método de busca limitada na profundidade
# Descrição simples: Igual à busca primeiro-na-profundidade, só que há um limite l para expandir

# Params :
#   origin -> de onde 
#   destination -> até onde
#   nodes -> conjunto de nós da arvóre ou grafo
def limitedDepth(originKey, destinationKey, nodes, limit):
  stack = [] # Pilha
  visited = set() # Lista com os nó visitados
  iterator = 0

  stack.append(originKey)

  while (len(stack) > 0):

    if (iterator < limit) :
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

      iterator += 1
    else:
      break
  
  print('Cidade não encontrada!')
  return False
