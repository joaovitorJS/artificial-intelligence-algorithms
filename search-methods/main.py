# 1) Busca Primeiro na Largura          DOING 
# 2) Busca de Custo Uniforme            DONE
# 3) Busca Primeiro na Profundidade     TO-DO
# 4) Busca de Profundidade Limitada     TO-DO
# 5) Busca de Aprofundamento Iterativo. TO-DO
# 6) Busca Greedy                       TO-DO


from methods.breadthFirst import breadthFirst
from methods.uniformCost import uniformCost
from methods.depthFirst import depthFirst
from cities import cities


origin = 'Arad'
destination = 'Bucharest'

# breadthFirst(origin, destination, cities)
# uniformCost(origin, destination, cities)
depthFirst(origin, destination, cities)


