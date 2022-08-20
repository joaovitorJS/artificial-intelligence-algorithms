# Método de busca primeiro na profundidade (DFS - Depth-first search)
# Descrição simples: Expande o nodo mais profundo ainda não expandido

# Params :
#   origin -> de onde 
#   destination -> até onde
#   nodes -> conjunto de nós da arvóre ou grafo
def primeiroNaProfundidade(origemChave, destinoChave, nodes):
  pilha = [] # Pilha
  visitados = set() # Lista com os nó visitados

  pilha.append(origemChave)

  while (len(pilha) > 0):
    noCorrenteChave = pilha.pop()

    noCorrente = next((sub for sub in nodes if sub.get(noCorrenteChave)), None) # Traz toda a estrutura da cidade: {Cidade: [{CidadeVizinha: Custo}]}

    if (noCorrenteChave == destinoChave):
      print('Cidade encontrada!')
      return True

    if (noCorrenteChave not in visitados):
      visitados.add(noCorrenteChave)


      for vizinho in  noCorrente[noCorrenteChave]:
        keys = vizinho.keys()
        vizinhoChave = list(keys)[0] # Nome da cidade
        if (vizinhoChave not in visitados):
          pilha.append(vizinhoChave)
  
  print('Cidade não encontrada!')
  return False
