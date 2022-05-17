# 1) Busca Primeiro na Largura          DONE
# 2) Busca de Custo Uniforme            DONE
# 3) Busca Primeiro na Profundidade     DONE
# 4) Busca de Profundidade Limitada     TO-DO
# 5) Busca de Aprofundamento Iterativo. TO-DO
# 6) Busca Greedy                       TO-DO


from methods.breadthFirst import breadthFirst
from methods.uniformCost import uniformCost
from methods.depthFirst import depthFirst
from methods.limitedDepth import limitedDepth
from methods.iterativeDeepening import iterativeDeepening
from cities import cities

origin = 'Arad'
destination = 'Bucharest'

# breadthFirst(origin, destination, cities)
# uniformCost(origin, destination, cities)
# depthFirst(origin, destination, cities)
# limitedDepth(origin, destination, cities, limit=8)
iterativeDeepening(origin, destination, cities)


