class No:
    def __init__(self):
        self.vemDe = None
        self.custo = 999999999999
    
    def setVemDe(self,vemDe):
        self.vemDe = vemDe
    
    def  setCusto(self,custo):
        self.custo = custo

    def getCusto(self):
        return self.custo
    
    def getVemDe(self):
        return self.vemDe

################################
# ENNERY SIMILIEN 38333
#
# O programa não leva em conta uma 
# origem inexistente no mapa
# fornece sempre uma origem válida
################################

destino = "Urziceni"
origem = ("Oradea", 0)
############ IMPORTANTE #############
# A ESTRUTURA DO DICIONARIO
#   Nome do nó : [ JáExpandido, (OndeVeio, qualCusto), [Seus vizinhos e seus custos]]
#
# A implementação tem base no grafo do livro,
# Para vários casos de testes, só precisa mudar 
# a ORIGEM e o DESTINO
#####################################
arvore = {
    "Arad": [False, No(), [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)]],
    "Zerind": [False, No(), [("Oradea", 71), ("Arad", 75)]],
    "Oradea": [False, No(), [("Sibiu", 151), ("Zerind", 71)]],
    "Sibiu": [False, No(), [("Oradea", 151), ("Fagaras", 99), ("R. Vilcea", 80), ("Arad", 140)]],
    "Timisoara": [False, No(), [("Lugol", 111), ("Arad", 118)]],
    "Lugol": [False, No(), [("Mechadia", 70), ("Timisoara", 111)]],
    "Fagaras": [False, No(), [("Bucharest", 211), ("Sibiu", 99)]],
    "R. Vilcea": [False, No(), [("Pitesti", 97), ("Cralova", 146), ("Sibiu", 80)]],
    "Mechadia": [False, No(), [("Dobreta", 75), ("Lugol", 70)]],
    "Dobreta": [False, No(), [("Cralova", 120), ("Mechadia", 75)]],
    "Bucharest": [False, No(), [("Fagaras", 211), ("Urziceni", 85), ("Glurglu", 90), ("Pitesti", 101)]],
    "Pitesti": [False, No(), [("Bucharest", 101), ("Cralova", 138),("R. Vilcea", 97)]],
    "Cralova": [False, No(), [("Pitesti", 138), ("R. Vilcea", 146), ("Dobreta", 120)]],
    "Urziceni": [False, No(), [("Vaslui", 142), ("Hirsova", 98), ("Bucharest", 85)]],
    "Glurglu": [False, No(), [("Bucharest", 90)]],
    "Vaslui": [False, No(), [("Iasi", 92), ("Urziceni", 142)]],
    "Hirsova": [False, No(), [("Eforie", 86), ("Urziceni", 98)]],
    "Iasi": [False, No(), [("Neamt", 87), ("Vaslui", 92)]],
    "Eforie": [False, No(), [("Hirsova", 86)]],
    "Neamt": [False, No(), [("Iasi", 87)]]
}

arvore[origem[0]][1].setCusto(0)

def orderedInsertion(lista, item):
    lista.append(item)
    index = len(lista) - 1
    while (index > 0) and (lista[index][1] < lista[index-1][1]):
        temp = lista[index]
        lista[index] = lista[index-1]
        lista[index-1] = temp
        index -= 1

def expand(nodos):
    if len(nodos) <= 0:
        return False
    #mostra a lista após cada expansão
    print("FILA: ", nodos) #comentar para evitar imprimir a lista
    noAtual = nodos.pop(0)

    if noAtual[0] == destino:
        return True
  
    custoNoAtual = arvore[noAtual[0]][1].getCusto()
    vizinhosDeNo = arvore[noAtual[0]][2]

    for vizinho in vizinhosDeNo:
        if arvore[vizinho[0]][0] is False:
            custoDoVizinho = arvore[vizinho[0]][1].getCusto()
            if custoDoVizinho > custoNoAtual + vizinho[1]:
                arvore[vizinho[0]][1].setVemDe(noAtual[0])
                arvore[vizinho[0]][1].setCusto(custoNoAtual + vizinho[1])
                orderedInsertion(nodos, (vizinho[0], custoNoAtual + vizinho[1]))

    arvore[noAtual[0]][0] = True
    return expand(nodos)

def otimalPathPrinter():
    node = arvore[destino][1]
    path = []
    path.insert(0, destino)

    while node.getVemDe() != None:
        path.insert(0, node.getVemDe())
        node = arvore[node.getVemDe()][1]

    path.append(arvore[destino][1].getCusto())
    print("DESTINO ENCONTRADO:", ' --> '.join(str(x) for x in path))



if expand([origem]):
    otimalPathPrinter()
else:
    print("Destino não encontrado :)")

