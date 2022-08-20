# Método de busca por aprofundamento iterativo (IDS – Iterative Deepening Search)
# Descrição:
#  - Combinação com a busca em profundidade em árvore, que encontra o melhor limite de profundidade
#  - Ela faz isso aumentando gradualmente o limite — primeiro 0, depois 1, depois 2, e assim por diante
#    até encontrar um objetivo.
from metodos.limitadaNaProfundidade import limitadaNaProfundidade

# IDS baseado no DSF e usando o limitadaNaProfundidade
def aprofundamentoIterativo(origemChave, destinoChave, nos):
  cidadeEncontrada = False
  limite = 0
  while (not cidadeEncontrada):
    resultadoBusca = limitadaNaProfundidade(origemChave, destinoChave, nos, limite)
    if (resultadoBusca):
      print('Cidade encontrada na profundidade: ' + str(limite))
      return True
    else: 
      limite += 1

  return False
