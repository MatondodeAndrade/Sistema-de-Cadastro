import numpy as np

def carregar_dados(caminho):
    return np.load(caminho)

def media_coluna(dados, indice):
    return np.mean(dados[:, indice])

def maximo_coluna(dados, indice):
    return np.max(dados[:, indice])

def minimo_coluna(dados, indice):
    return np.min(dados[:, indice])
