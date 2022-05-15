# Método de busca primeiro em largura (breadth-first)

# Params :
#   origin -> de onde 
#   destination -> até onde
#   nodes -> conjunto de nós da arvóre ou grafo
def breadthFirst(origin, destination, nodes):
  visited = set()  # Conjunto dos nós visitados
  queue = []    # Fila
  pathTraveled = [origin]

  queue.insert(0, origin)
  visited.add(origin) # Visitou o nó

  while (len(queue) != 0):
    currentNodeKey = queue.pop()

    if (currentNodeKey == destination):
      if (neighbourKey not in pathTraveled):
          pathTraveled.append(neighbourKey)
      return pathTraveled
      
    currentNode = next((sub for sub in nodes if sub.get(currentNodeKey)), None)
  
    for neighbour in currentNode[currentNodeKey]:
      keys = neighbour.keys()
      neighbourKey = list(keys)[0]
      if (neighbourKey not in visited):
        queue.insert(0, neighbourKey)
        visited.add(neighbourKey)
        if (neighbourKey not in pathTraveled):
          pathTraveled.append(neighbourKey)

        # print(neighbour)
    # print('\n')
  return []
