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

        # Analisando Primeira Camada Horizontal   
        print('\nAnalisando Primeira Camada Horizontal: ')
        matrizes_validas_camada1 = analisa_camadas_horizontais(0, 3, 0, 9, matriz_entrada)
        imprime_matriz_matrizes_validas(matrizes_validas_camada1)   
            
        # Analisando Segunda Camada Horizontal   
        print('\nAnalisando Segunda Camada Horizontal: ')
        matrizes_validas_camada2 = analisa_camadas_horizontais(3, 6, 0, 9, matriz_entrada)
        imprime_matriz_matrizes_validas(matrizes_validas_camada2)   
        
        # Analisando Terceira Camada Horizontal    
        print('\nAnalisando Terceira Camada Horizontal: ')
        matrizes_validas_camada3 = analisa_camadas_horizontais(6, 9, 0, 9, matriz_entrada)
        imprime_matriz_matrizes_validas(matrizes_validas_camada3)   

        print('\nTotal de matrizes válidas: Camada1 * Camada2 * Camada3 = {} * {} * {} = {} '.format(len(matrizes_validas_camada1), len(matrizes_validas_camada2), len(matrizes_validas_camada3), (len(matrizes_validas_camada1)*len(matrizes_validas_camada2)*len(matrizes_validas_camada3))))

        print('Tratando as matrizes válidas das camadas 1 e 2:')
        matrizes_combinadas_validas_camadas_1e2 = tratando_as_camadas_um_e_dois(matrizes_validas_camada1, matrizes_validas_camada2, matriz_entrada)

        gera_arquivo_trincas(matrizes_combinadas_validas_camadas_1e2, '/home/03795871492/sudoku/sudoku_saida_parte01_')

    end = time.time()
    exibe_tempo_processamento(start, end)
# ====================================
def gera_arquivo_trincas(matrizes_combinadas_validas_camadas_1e2, nome_arquivo):
    lista_salvar_arquivo = retorna_str_lista_trincas(matrizes_combinadas_validas_camadas_1e2)
    nome_arquivo = nome_arquivo+retorna_date_time_string()+'.txt'
    with open(nome_arquivo, 'w') as f:
        for item_lista in lista_salvar_arquivo:            
            f.write(str(item_lista))
    f.close()
# ====================================
def retorna_str_lista_trincas(matrizes_validas):
    lista_retorno = []
    for k, item1 in enumerate(matrizes_validas):
        str1 = "\n["+str(k)+"]->"
        lista_retorno.append(str1)
        for item2 in item1:
            lista_retorno.append(item2)
        #lista_retorno.append("]")
    return lista_retorno
# ====================================
def tratando_as_camadas_um_e_dois(matrizes_validas_camada1, matrizes_validas_camada2, matriz_entrada):
    lista_matrizes_combinadas_validas = []
    matrizes_combinadas_validas_camadas_1e2 = []

    for lista_camada1 in matrizes_validas_camada1:
        for lista_camada2 in matrizes_validas_camada2:
            lista_matrizes_combinadas_validas.append(lista_camada1+lista_camada2)

    print('Len camada 1 => ',len(matrizes_validas_camada1))
    print('Len camada 2 => ',len(matrizes_validas_camada2))
    print('Len camadas 1 e 2 combinadas => ',len(lista_matrizes_combinadas_validas))

    for k, item_lista in enumerate(lista_matrizes_combinadas_validas):
        matriz_teste = matriz_entrada.copy()

        for trinca in item_lista:
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor

        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
        if eh_valida:
            print('.',end='')
            matrizes_combinadas_validas_camadas_1e2.append(item_lista)            

    print('\nQtd matrizes combinadas validas das camadas 1 e 2: => {}'.format(len(matrizes_combinadas_validas_camadas_1e2)))
    return matrizes_combinadas_validas_camadas_1e2    
# ====================================
def retorna_listas_camadas_horizontais(linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz_entrada):
    lista_02_possibs = []
    lista_03_possibs = []
    lista_04_possibs = []
    lista_05_possibs = []
    lista_06_possibs = []
    lista_07_possibs = []
    trinca = None

    for i in range(linha_inicio, linha_fim):
        for j in range(coluna_inicio, coluna_fim):
            if matriz_entrada[i][j] == 0:
                lista = retorna_qtd_possibs_celula(i, j, matriz_entrada)
                if len(lista) == 2:
                    trinca = Trinca(i,j,0)
                    lista_02_possibs.append(trinca)
                elif len(lista) == 3:   
                    trinca = Trinca(i,j,0)
                    lista_03_possibs.append(trinca)
                elif len(lista) == 4:   
                    trinca = Trinca(i,j,0)
                    lista_04_possibs.append(trinca)
                elif len(lista) == 5:   
                    trinca = Trinca(i,j,0)
                    lista_05_possibs.append(trinca)
                elif len(lista) == 6:   
                    trinca = Trinca(i,j,0)
                    lista_06_possibs.append(trinca)
                elif len(lista) == 7:   
                    trinca = Trinca(i,j,0)
                    lista_07_possibs.append(trinca)

    trata_lista_possibilidades(lista_02_possibs, 2)
    trata_lista_possibilidades(lista_03_possibs, 3)
    trata_lista_possibilidades(lista_04_possibs, 4)
    trata_lista_possibilidades(lista_05_possibs, 5)
    trata_lista_possibilidades(lista_06_possibs, 6)
    trata_lista_possibilidades(lista_07_possibs, 7)

    return lista_02_possibs, lista_03_possibs, lista_04_possibs, lista_05_possibs, lista_06_possibs, lista_07_possibs
# ====================================
def trata_lista_possibilidades(lista_possibs, num_possibs):
    if len(lista_possibs) > 0:
        print(' Celulas com {} possibs : ['.format(num_possibs), end='')
        for k,item in enumerate(lista_possibs):                
            if k != len(lista_possibs)-1:
                print('({},{}),'.format(item.linha,item.coluna), end='')
            if k == len(lista_possibs)-1:
                print('({},{})'.format(item.linha,item.coluna), end='')
        print(']')
# ====================================

def analisa_camadas_horizontais(linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz_entrada):
    posicoes_02_possibs = []
    posicoes_03_possibs = []
    posicoes_04_possibs = []
    posicoes_05_possibs = []
    posicoes_06_possibs = []
    posicoes_07_possibs = []

    lista_02_possibs = []
    lista_03_possibs = []
    lista_04_possibs = []
    lista_05_possibs = []
    lista_06_possibs = []
    lista_07_possibs = []

    arvore_02_possibs = [[],[]]
    arvore_03_possibs = [[],[],[]]
    arvore_04_possibs = [[],[],[],[]]
    arvore_05_possibs = [[],[],[],[],[]]
    arvore_06_possibs = [[],[],[],[],[],[]]
    arvore_07_possibs = [[],[],[],[],[],[],[]]

    lista_02_possibs, lista_03_possibs, lista_04_possibs, lista_05_possibs, lista_06_possibs, lista_07_possibs = retorna_listas_camadas_horizontais(linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz_entrada)     

    mat_valid_02_possibs = []
    mat_valid_03_possibs = []
    mat_valid_04_possibs = []
    mat_valid_05_possibs = []
    mat_valid_06_possibs = []
    mat_valid_07_possibs = []

    if len(lista_02_possibs) > 0:
        mat_valid_02_possibs = retorna_matrizes_validas(linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz_entrada, 2)

    if len(lista_03_possibs) > 0:
        mat_valid_03_possibs = retorna_matrizes_validas(linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz_entrada, 3)

    if len(lista_04_possibs) > 0:
        mat_valid_04_possibs = retorna_matrizes_validas(linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz_entrada, 4)

    if len(lista_05_possibs) > 0:
        mat_valid_05_possibs = retorna_matrizes_validas(linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz_entrada, 5)

    if len(lista_06_possibs) > 0:
        mat_valid_06_possibs = retorna_matrizes_validas(linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz_entrada, 6)

    if len(lista_07_possibs) > 0:
        mat_valid_07_possibs = retorna_matrizes_validas(linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz_entrada, 7)

    lista_matrizes_combinadas_validas = []
    for lista_02 in mat_valid_02_possibs:
        for lista_03 in mat_valid_03_possibs:
            lista_matrizes_combinadas_validas.append(lista_02+lista_03)
    for lista_04 in mat_valid_04_possibs:
        for lista_05 in mat_valid_05_possibs:
            lista_matrizes_combinadas_validas.append(lista_04+lista_05)
    for lista_06 in mat_valid_06_possibs:
        for lista_07 in mat_valid_07_possibs:
            lista_matrizes_combinadas_validas.append(lista_06+lista_07)

    matrizes_combinadas_validas = []
    contador_matrizes_combinadas_validas = 0
    for k, item_lista in enumerate(lista_matrizes_combinadas_validas):
        matriz_teste = matriz_entrada.copy()

        if k >= 1000 and k%1000 == 0:
            print('.'.format(k),end='')

        for trinca in item_lista:
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor

        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
        if eh_valida:
            matrizes_combinadas_validas.append(item_lista)
            contador_matrizes_combinadas_validas += 1

    nome_camada = retorna_nome_camada(linha_inicio, linha_fim)
    print('\nQtd matrizes combinadas validas na {} => {}'.format(nome_camada, contador_matrizes_combinadas_validas))
    return matrizes_combinadas_validas
# ====================================
def retorna_nome_camada(linha_inicio, linha_fim):
    nome_camada = ''
    if linha_inicio == 0 and linha_fim == 2:
        nome_camada = 'CAMADA 01'
    elif linha_inicio == 3 and linha_fim == 5:
        nome_camada = 'CAMADA 02'
    elif linha_inicio == 6 and linha_fim == 8:
        nome_camada = 'CAMADA 03'

    return nome_camada
# ====================================
def retorna_matrizes_validas(linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz_entrada, num_possibs):
    print('\nAnalisando trincas com {} possibilidades:'.format(num_possibs))

    posicoes_possibs = retorna_posicoes_possibilidades_camada_horizontal(
        linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz_entrada, num_possibs)
    lista_possibilidades = []
    for pos in posicoes_possibs:
        lista_possibilidades.append(pos)
    
    imprime_trincas(lista_possibilidades)

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

    tamanho = imprime_saida_retorna_tam_lista(arvore_possibilidades)
    print('\nQtd de árvores de {} possibs => {} '.format(num_possibs, tamanho))        

    matriz_matrizes_validas = []
    cont_matrizes_validas = 0
    for k,item_arvore in enumerate(arvore_possibilidades):
        matriz_teste = matriz_entrada.copy()
        lista_trincas = []

        for trinca in item_arvore:
            lista_trincas.append(trinca)
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor
        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
        if eh_valida:
            matriz_matrizes_validas.append(lista_trincas)
            cont_matrizes_validas +=1

    return matriz_matrizes_validas
# ====================================
def retorna_posicoes_possibilidades_camada_horizontal(
    linha_inicio, linha_fim, coluna_inicio, coluna_fim, matriz, num_possibs):

    lista_possibs = []
    for i in range(linha_inicio, linha_fim):
        for j in range(coluna_inicio, coluna_fim):
            if matriz[i][j] == 0:
                lista = retorna_qtd_possibs_celula(i, j, matriz)
                
                if len(lista) == num_possibs:
                    lista_possibs.append(Posicao_Possibilidades(i,j,lista))
    return lista_possibs
# ====================================
