# Estrutura de uma cidade
# {                                   {        
#   'Arad': [                           Cidade : [     
#     {'Zerind': 75},                     {CidadeVizinha: Distância entre Cidade e CidadeVizinha}         
#     {'Sibíu': 75},          --->      ]
#     {'Timisoara': 75}               }
#   ]
# }



# Estrutura do conjunto de cidades
cities = [
  {
    'Arad': [
      {'Zerind': 75},
      {'Sibiu': 140},
      {'Timisoara': 118}
    ]
  },
  {
    'Zerind': [
      {'Arad': 75},
      {'Oradea': 71}
    ]
  },
  {
    'Sibiu': [
      {'Arad': 140},
      {'Oradea': 151},
      {'Rimnicu Vilcea': 80},
      {'Fagaras': 99}
    ]
  },
  {
    'Timisoara': [
      {'Arad': 118},
      {'Lugoj': 111}
    ]
  },
  {
    'Oradea': [
      {'Zerind': 71},
      {'Sibiu': 151}
    ]
  },
  {
    'Rimnicu Vilcea': [
      {'Sibiu': 80},
      {'Pitesti': 97},
      {'Craiova': 146}
    ]
  },
  {
    'Fagaras': [
      {'Sibiu': 99},
      {'Bucharest': 211}
    ]
  },
  {
    'Lugoj': [
      {'Timisoara': 111},
      {'Mehadia': 70}
    ]
  },
  {
    'Pitesti': [
      {'Rimnicu Vilcea': 97},
      {'Craiova': 138},
      {'Bucharest': 101}
    ]
  },
  {
    'Craiova': [
      {'Rimnicu Vilcea': 146},
      {'Pitesti': 138},
      {'Dobreta': 120}
    ]
  },
  {
    'Bucharest': [
      {'Pitesti': 101},
      {'Fagaras': 211},
      {'Giurgiu': 90},
      {'Urziceni': 85}
    ]
  },
  {
    'Mehadia': [
      {'Lugoj': 70},
      {'Dobreta': 75}
    ]
  },
  {
    'Giurgiu': [
      {'Bucharest': 90}
    ]
  },
  {
    'Urziceni': [
      {'Bucharest': 85},
      {'Hirsova': 98},
      {'Vaslui': 142}
    ]
  },
  {
    'Dobreta': [
      {'Mehadia': 75},
      {'Craiova': 120}
    ]
  },
  {
    'Hirsova': [
      {'Urziceni': 98},
      {'Eforie': 86}
    ]
  },
  {
    'Vaslui': [
      {'Urziceni': 142},
      {'Iasi': 92}
    ]
  },
  {
    'Eforie': [
      {'Hirsova': 86}
    ]
  },
  {
    'Iasi': [
      {'Vaslui': 92},
      {'Neamt': 87}
    ]
  },
  {
    'Neamt': [
      {'Iasi': 87}
    ]
  }
]
