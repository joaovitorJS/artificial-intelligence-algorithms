# Método de busca primeiro na profundidade (DFS - Depth-first search)
# Descrição simples: Expande o nodo mais profundo ainda não expandido

import os
import sys


script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..')
sys.path.append( mymodule_dir )
import cities

def depthFirst(originKey, destinationKey, nodes):
    

