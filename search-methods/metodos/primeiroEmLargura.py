# Método de busca primeiro em largura (breadth-first)

# Params :
#   origem -> de onde 
#   destino -> até onde
#   nos -> conjunto de nós da arvóre ou grafo
def primeiroEmLargura(origem, destino, nos):
  visitados = set()  # Conjunto dos nós visitados
  fila = []    # Fila

  fila.insert(0, origem)
  visitados.add(origem) # Visitou o nó

  while (len(fila) != 0):
    noCorrenteChave = fila.pop()

    if (noCorrenteChave == destino):
      print("Cidade encontrada!")      
      return True
      
    noCorrente = next((sub for sub in nos if sub.get(noCorrenteChave)), None)
  
    for vizinho in noCorrente[noCorrenteChave]:
      keys = vizinho.keys()
      vizinhoChave = list(keys)[0]
      if (vizinhoChave not in visitados):
        fila.insert(0, vizinhoChave)
        visitados.add(vizinhoChave)

  print("Cidade não Encontrada")
  return False

