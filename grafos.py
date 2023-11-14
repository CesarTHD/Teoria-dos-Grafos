import numpy as np
import math
import psutil
import tracemalloc
import os
from tqdm import tqdm
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


#leArquivo() -> recebe o caminho do arquivo .txt com dados do grafo e retorna a quantidade vertices e suas arestas
def leArquivo(caminho):
    arestaL = []
    arestaR = []

    with open(caminho, "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            elementos = linha.split()
            indice = linhas.index(linha)
            if(indice == 0):
                vertices = elementos[indice]
            else:
               for i in range(len(elementos)):
                if(i == 0):
                    arestaL.append(int(elementos[i]))
                else:
                    arestaR.append(int(elementos[i]))
    arquivo.close()

    # cria um dataframe PANDAS para armazenar os dados
    df = pd.DataFrame({'node_1': arestaL, 'node_2': arestaR})

    G = nx.from_pandas_edgelist(
        df,
        "node_1",
        "node_2",
        create_using=nx.Graph()
    )

    return vertices, arestaL, arestaR, G

#grauVert() -> recebe os dois vetores de arestas e retorna o grau de cada vértice
def grauVert(arestasL, arestasR):
    graus = np.ones(len(arestasL))

    for i in range(len(arestasL)):
        for j in range(len(arestasL)):
            if(i==j):
                if(arestasL[i] == arestasR[j]):
                    graus[i] += 1
            else:
                if(arestasL[i] == arestasR[j] or arestasL[i] == arestasL[j]):
                    graus[i] += 1
            
    graus = [int(valor) for valor in graus]
    return graus




#printSaida() -> recebe os vertices e as arestas do grafo e gera um .txt com dados do grafo: qtd de vertice, qtd de aresta e o grau de cada vertice
def infosGraph(vertices, arestasL, arestasR):
    graus = grauVert(arestasL, arestasR)

    #with open("dados-grafo.txt", 'w') as arquivo:
    with open("saida.txt", 'w') as arquivo:
    #with open("dados-collaboration_graph.txt", 'w') as arquivo:
        arquivo.write("# n = {}\n".format(vertices))
        arquivo.write("# m = {}\n".format(len(arestasL)))
        for i in range(len(arestasL)):
            arquivo.write("{} {}\n".format(i+1,graus[i]))
    arquivo.close



#função para gerar arquivo .txt com lista de adjacência
def listaAdjacencia(arestasL, arestasR):
    graus = grauVert(arestasL, arestasR)
    adjacencia = []
    
    for i in range(len(arestasL)):
        dentro = []
        for j in range(len(arestasL)):
            if(i==j):
                dentro.append(arestasR[i])
            else:
                if(arestasL[i] == arestasR[j]):
                    dentro.append(arestasL[j])
                elif(arestasL[i] == arestasL[j]):
                    dentro.append(arestasR[j])
        adjacencia.append(dentro)    
    
    with open("lista-adjacencia.txt", 'w') as arquivo:
        for i in range(len(adjacencia)):
            arquivo.write("{} -> {}\n".format(i+1, adjacencia[i]))

    arquivo.close



#função para gerar arquivo .txt com matriz de adjacência
def matrizAdjacencia(arestasL, arestasR):
    graus = grauVert(arestasL, arestasR)
    matriz = []

    for i in range(len(graus)):
        vetor = []
        for j in range(len(graus)):
            vetor.append(0)
        matriz.append(vetor)

    for i in range(len(arestasL)):
        matriz[arestasL[i]-1][arestasR[i]-1] = 1
        matriz[arestasR[i]-1][arestasL[i]-1] = 1

    with open("matriz-adjacencia.txt", 'w') as arquivo:
        for i in range(len(matriz)):
            arquivo.write("{}\n".format(matriz[i]))
    arquivo.close

# busca em largura
def buscaLargura(G, vertice):
    try:
        A = nx.path_graph(G)
        T = nx.dfs_tree(A, source=vertice).reverse().reverse()

        with open('buscaLargura.txt', 'w') as f:
            f.write("vertice - pai - nivel\n\n")
            lista = list(T.nodes)

            for i, node in tqdm(enumerate(T.nodes), total=len(lista)):
                listaAnc = list(nx.ancestors(T, node))
                pai = lista[i-1] if len(listaAnc) > 0 else 0
                nivel = len(listaAnc)
                f.write(f"{node} - {pai} - {nivel}\n")

        # nx.draw_networkx(T)
        # plt.show()

    except Exception as e:
        print(e)
        return False


# busca componentes do grafo
def buscarComponentes(G):
    try:
        qnt = nx.number_connected_components(G)
        minimo = 100000
        maximo = 0
        with open('componentes.txt', 'w') as f:
            f.write(f"Total de componentes: {qnt}\n")
            for i, comp in tqdm(enumerate(nx.connected_components(G)), total=qnt):
                lista = list(comp)
                if (len(lista) > maximo): maximo = len(lista)
                if(len(lista) < minimo): minimo = len(lista)
                f.write(f"\n\nCompontente [{i}] - {len(lista)} vertices\n")
                f.write(str(lista))

            f.write(f"\nMinimo [{minimo}] - maximo [{maximo}]\n")
    except Exception as e:
        print(e)
        return False


def graficoGraus(G):
    try:
        degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
        dmax = max(degree_sequence)
        print(dmax)
        histograma = nx.degree_histogram(G)
        fig, ax = plt.subplots()
        plt.bar([k for k in range(len(histograma))], histograma, color='b')
        plt.title("Distribuição de Graus")
        plt.ylabel("Qnt")
        plt.xlabel("Grau")
        eixos = plt.gca()
        #eixos.set_xlim([-0.5, xmax + 0.5])
        eixos.set_ylim([0, 3000])
        plt.show()
        
    except Exception as e:
        print(e)
        return False