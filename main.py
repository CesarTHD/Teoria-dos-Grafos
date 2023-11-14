import grafos
import tracemalloc
import time

#vertices, arestasL, arestasR, G = grafos.leArquivo("grafo.txt")
#vertices, arestasL, arestasR, G = grafos.leArquivo("as_graph.txt")
vertices, arestasL, arestasR, G = grafos.leArquivo("collaboration_graph.txt")

#grafos.infosGraph(vertices, arestasL, arestasR)
tracemalloc.start()
ini = time.time()

grafos.listaAdjacencia(arestasL, arestasR)

fim = time.time()
print ("tempo: ", fim-ini)
second_size, consumoMem = tracemalloc.get_traced_memory()
print('Consumo de memória: ', f'{"{:.3f}".format(consumoMem / 10**6)}MB')
#grafos.matrizAdjacencia(arestasL, arestasR)
#grafos.buscaLargura(G, 5)
#grafos.buscarComponentes(G)
#grafos.graficoGraus(G)