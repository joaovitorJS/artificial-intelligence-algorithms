# Método de busca limitada na profundidade
# Descrição simples: Igual à busca primeiro-na-profundidade, só que há um limite l para expandir

# Params :
#   origem -> de onde 
#   destination -> até onde
#   nos -> conjunto de nós da arvóre ou grafo
def limitadaNaProfundidade(origemChave, destinoChave, nos, limite):
  pilha = [] # Pilha
  visitados = set() # Lista com os nó visitados
  iterator = 0

  pilha.append(origemChave)

  while (len(pilha) > 0):

    if (iterator < limite) :
      noCorrenteChave = pilha.pop()

      noCorrente = next((sub for sub in nos if sub.get(noCorrenteChave)), None) # Traz toda a estrutura da cidade: {Cidade: [{CidadeVizinha: Custo}]}

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

      iterator += 1
    else:
      break
  
  print('Cidade não encontrada!')
  return False
