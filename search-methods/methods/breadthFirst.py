# Método de busca primeiro em largura (breadth-first)

# Params :
#   origin -> de onde 
#   destination -> até onde
#   nodes -> conjunto de nós da arvóre ou grafo
def breadthFirst(origin, destination, nodes):
  visited = set()  # Conjunto dos nós visitados
  queue = []    # Fila

  queue.insert(0, origin)
  visited.add(origin) # Visitou o nó

  while (len(queue) != 0):
    currentNodeKey = queue.pop()

    if (currentNodeKey == destination):
      print("Cidade encontrada!")      
      return True
      
    currentNode = next((sub for sub in nodes if sub.get(currentNodeKey)), None)
  
    for neighbour in currentNode[currentNodeKey]:
      keys = neighbour.keys()
      neighbourKey = list(keys)[0]
      if (neighbourKey not in visited):
        queue.insert(0, neighbourKey)
        visited.add(neighbourKey)

  print("Cidade não Encontrada")
  return False
