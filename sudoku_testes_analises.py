import numpy as np
import time
import datetime

from random import choice
from collections import Counter

from sudoku_utils import *
from solucao_arvore_geral import *
from solucao_arvore_02_possibs import monta_arvore_02_possibilidades
from solucao_arvore_03_possibs import monta_arvore_03_possibilidades
from solucao_arvore_04_possibs import monta_arvore_04_possibilidades
from solucao_arvore_05_possibs import monta_arvore_05_possibilidades
from solucao_arvore_06_possibs import monta_arvore_06_possibilidades
from solucao_arvore_07_possibs import monta_arvore_07_possibilidades

CONJUNTO_COMPLETO = {1, 2, 3, 4, 5, 6, 7, 8, 9}

MATRIZ_ENTRADA_01 = np.array([
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 1, 7, 3, 6, 0],
    [0, 2, 0, 0, 9, 3, 0, 0, 8],
    [0, 5, 2, 0, 0, 0, 0, 0, 0],
    [0, 6, 4, 0, 0, 0, 1, 3, 0],
    [0, 0, 0, 0, 0, 0, 5, 4, 0],
    [1, 0, 0, 5, 7, 0, 0, 8, 0],
    [0, 7, 6, 1, 4, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
])

MATRIZ_ENTRADA_02 = np.array([
    [6, 1, 8,  0, 0, 0,  4, 0, 0],
    [0, 0, 0,  0, 9, 6,  0, 0, 0],
    [0, 0, 0,  8, 0, 0,  0, 0, 7],
    [0, 0, 0,  6, 8, 9,  0, 0, 3],
    [4, 0, 0,  1, 0, 0,  0, 0, 0],
    [9, 0, 0,  0, 4, 0,  0, 0, 8],
    [0, 0, 0,  0, 0, 0,  7, 0, 0],
    [0, 7, 0,  0, 0, 3,  0, 0, 6],
    [0, 4, 0,  2, 0, 0,  0, 0, 5]
])
MATRIZ_ENTRADA_02_RESOLVIDA = np.array([
    [6, 1, 8,  7, 2, 5,  4, 3, 9],
    [7, 5, 4,  3, 9, 6,  2, 8, 1],
    [3, 9, 2,  8, 1, 4,  6, 5, 7],
    [1, 2, 7,  6, 8, 9,  5, 4, 3],
    [4, 8, 5,  1, 3, 7,  9, 6, 2],
    [9, 6, 3,  5, 4, 2,  1, 7, 8],
    [5, 3, 1,  9, 6, 8,  7, 2, 4],
    [2, 7, 9,  4, 5, 3,  8, 1, 6],
    [8, 4, 6,  2, 7, 1,  3, 9, 5]
])

def inicio():
    start = time.time()
    achou_solucao = False
    LOOPS = 1000
    for i in range(LOOPS):
        matriz_entrada = MATRIZ_ENTRADA_02
        mat, eh_valida = validacao(matriz_entrada)
        if eh_valida:
            achou_solucao = True
            print('===========================================')
            print(' Achou uma matriz válida na {}ª interação: {}'.format(i+1,mat))
            print('===========================================')
            break
            
    if not achou_solucao:
        print('===========================================')
        print('Em {} interações, não achou a solução: '.format(LOOPS))
        print('===========================================')

        teste(matriz_entrada)

    end = time.time()
    exibe_tempo_processamento(start, end)
# ====================================
def teste(matriz_entrada):

    posicoes_possibs = retorna_posicoes_possibilidades_camada_horizontal(0, 0, 0, 9, matriz_entrada)

    print('Tam => ',len(posicoes_possibs))
    lista_possibilidades = []
    for pos in posicoes_possibs:
        lista_possibilidades.append(pos)
    
    imprime_trincas(lista_possibilidades)

    '''
    if num_possibs == 2:
        arvore_possibilidades = monta_arvore_02_possibilidades(lista_possibilidades)
    elif num_possibs == 3:
        arvore_possibilidades = monta_arvore_03_possibilidades(lista_possibilidades)
    elif num_possibs == 4:
        arvore_possibilidades = monta_arvore_04_possibilidades(lista_possibilidades)
    elif num_possibs == 5:
        arvore_possibilidades = monta_arvore_05_possibilidades(lista_possibilidades)
    elif num_possibs == 6:
        arvore_possibilidades = monta_arvore_06_possibilidades(lista_possibilidades)
    elif num_possibs == 7:
        arvore_possibilidades = monta_arvore_07_possibilidades(lista_possibilidades)
    '''

# ====================================
def retorna_posicoes_possibilidades_camada_horizontal(
    linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz):

    lista_possibs = []
    for i in range(linha_inicio, linha_fim):
        for j in range(coluna_inicio, coluna_fim):
            if matriz[i][j] == 0:
                lista = retorna_qtd_possibs_celula(i, j, matriz)
                
                if len(lista) >= 2:
                    lista_possibs.append(Posicao_Possibilidades(i,j,lista))
    return lista_possibs
# ====================================
