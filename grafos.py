import numpy as np
import math

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
    return vertices, arestaL, arestaR

def countArestas(arestasL):
    qtdArestas = len(arestasL)
        
    return qtdArestas

def grauVert(arestasL, arestasR):
    graus = np.ones(len(arestasL))

    for i in range(len(arestasL)):
        for j in range(len(arestasL)):
            if(i!=j):
                if(arestasL[i] == arestasR[j]):
                    graus[i] += 1
            
    graus = [int(valor) for valor in graus]
    return graus

def printSaida(vertices, arestasL, arestasR):
    print("# n = ", vertices)
    print("# m = ", countArestas(arestasL))
    graus = grauVert(arestasL, arestasR)

    for i in range(len(arestasL)):
        print(arestasL[i], " " ,graus[i])

vertices, arestasL, arestasR = leArquivo("grafo.txt")

printSaida(vertices, arestasL, arestasR)
