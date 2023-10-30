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
    return indice, arestaL, arestaR



indice = 0
arestasL = []
arestasR = []

indice, arestasL, arestasR = leArquivo("grafo.txt")

