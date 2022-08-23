# Estrutura de uma cidade
# {                                   {        
#   'Arad': [                           Cidade : [     
#     {'Zerind': 75},                     {CidadeVizinha: Distância entre Cidade e CidadeVizinha}         
#     {'Sibíu': 75},          --->      ]
#     {'Timisoara': 75}               }
#   ]
# }

import json

arquivoCidades = open('cidades.json', 'r')
cidades = json.load(arquivoCidades)
arquivoCidades.close()

arquivoHeuristicaAradBuscharest = open('heuristicaAradBuscharest.json', 'r')
heuristicaAradBuscharest = json.load(arquivoHeuristicaAradBuscharest)
arquivoHeuristicaAradBuscharest.close()
