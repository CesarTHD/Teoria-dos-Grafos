import grafos
import tracemalloc
import time


'''Carregamento do grafo desejado - descomentar apenas a linha do arquivo texto desejado'''
#vertices, arestasL, arestasR, G = grafos.leArquivo("./grafos/grafo.txt")
vertices, arestasL, arestasR, G = grafos.leArquivo("./grafos/as_graph.txt")
#vertices, arestasL, arestasR, G = grafos.leArquivo("./grafos/collaboration_graph.txt")


#ini = time.time()

'''Chamada das funções da biblioteca'''
#grafos.infosGraph(vertices, arestasL, arestasR)
#grafos.listaAdjacencia(arestasL, arestasR)
#grafos.matrizAdjacencia(arestasL, arestasR)
#grafos.buscaLargura(G, 5)
#grafos.buscarComponentes(G)
#grafos.graficoGraus(G)



#fim = time.time()
#print ("tempo: ", fim-ini)
