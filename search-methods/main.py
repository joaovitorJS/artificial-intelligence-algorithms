# 1) Busca Primeiro na Largura          DONE
# 2) Busca de Custo Uniforme            DONE
# 3) Busca Primeiro na Profundidade     DONE
# 4) Busca de Profundidade Limitada     DONE
# 5) Busca de Aprofundamento Iterativo. DONE
# 6) Busca Greedy                       DONE


from metodos.primeiroEmLargura import primeiroEmLargura
from metodos.custoUniforme import custoUniforme
from metodos.primeiroNaProfundidade import primeiroNaProfundidade
from metodos.limitadaNaProfundidade import limitadaNaProfundidade
from metodos.aprofundamentoIterativo import aprofundamentoIterativo
from metodos.buscaGreedy import buscaGreedy
from cidades import cidades, heuristicaAradBuscharest


import sys

algoritmo = sys.argv[1]

origem = 'Arad'
destino = 'Bucharest'

if (algoritmo == '1'):
  print('Busca Primeiro na Largura\n\n')
  primeiroEmLargura(origem, destino, cidades)
elif (algoritmo == '2'):
  print('Busca de Custo Uniforme\n\n')
  custoUniforme(origem, destino, cidades)
elif (algoritmo == '3'):
  print('Busca Primeiro na Profundidade\n\n')
  primeiroNaProfundidade(origem, destino, cidades)
elif (algoritmo == '4'):
  print('Busca de Profundidade Limitada\n\n')
  limite = int(input('Entre com um limite de profundidade: '))
  limitadaNaProfundidade(origem, destino, cidades, limite)
elif (algoritmo == '5'):
  print('Busca de Aprofundamento Iterativo\n\n')
  aprofundamentoIterativo(origem, destino, cidades)
elif (algoritmo == '6'):
  print('Busca Greedy\n\n')
  buscaGreedy(origem, destino, cidades, heuristica=heuristicaAradBuscharest)
else:
  print("Algoritmo não encontrado")
  print('Escolha um número entre 1 a 6')

