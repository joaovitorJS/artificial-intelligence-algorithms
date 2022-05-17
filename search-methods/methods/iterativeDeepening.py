# Método de busca por aprofundamento iterativo (IDS – Iterative Deepening Search)
# Descrição:
#  - Combinação com a busca em profundidade em árvore, que encontra o melhor limite de profundidade
#  - Ela faz isso aumentando gradualmente o limite — primeiro 0, depois 1, depois 2, e assim por diante
#    até encontrar um objetivo.
from methods.limitedDepth import limitedDepth

# IDS baseado no DSF e usando o limitedDepth
def iterativeDeepening(originKey, destinationKey, nodes):
  hasFoundCity = False
  limit = 0
  while (not hasFoundCity):
    resultSearch = limitedDepth(originKey, destinationKey, nodes, limit)
    if (resultSearch):
      print('Cidade encontrada na profundidade: ' + str(limit))
      return True
    else: 
      limit += 1

  return False
