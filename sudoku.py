import numpy as np
import time

from random import choice
from collections import Counter

from sudoku_utils import *
#from solucao_arvore_geral import Posicao_Possibilidades, Trinca, imprime_trincas, imprime_saida, imprime_saida_retorna_tam_lista
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
            #print(mat)
            print('===========================================')
            break
            
    if not achou_solucao:
        print('===========================================')
        print('Em {} interações, não achou a solução: '.format(LOOPS))
        print('===========================================')

        # Analisando Primeira Camada Horizontal   
        print('\nAnalisando Primeira Camada Horizontal: ')
        matrizes_validas_camada1 = analisa_camadas_horizontais(0, 2, 0, 9, matriz_entrada)
        imprime_matriz_matrizes_validas(matrizes_validas_camada1)   

        # Analisando Segunda Camada Horizontal   
        print('\nAnalisando Segunda Camada Horizontal: ')
        matrizes_validas_camada2 = analisa_camadas_horizontais(3, 5, 0, 9, matriz_entrada)
        imprime_matriz_matrizes_validas(matrizes_validas_camada2)   
        
        # Analisando Terceira Camada Horizontal    
        print('\nAnalisando Terceira Camada Horizontal: ')
        matrizes_validas_camada3 = analisa_camadas_horizontais(6, 8, 0, 9, matriz_entrada)
        imprime_matriz_matrizes_validas(matrizes_validas_camada3)   

        print('\nTotal de matrizes válidas: Camada1 * Camada2 * Camada3 = {} * {} * {} = {} '.format(len(matrizes_validas_camada1), len(matrizes_validas_camada2), len(matrizes_validas_camada3), (len(matrizes_validas_camada1)*len(matrizes_validas_camada2)*len(matrizes_validas_camada3))))

        '''
        print('Tratando as matrizes válidas das camadas 1 e 2:')
        matrizes_combinadas_validas_camadas_1e2 = tratando_as_camadas_um_e_dois(matrizes_validas_camada1, matrizes_validas_camada2, matriz_entrada)

        print('Tratando as matrizes válidas do resultado das camadas 1 e 2 e com a camada 3 :')
        tratando_o_resultado_das_camadas_um_e_dois_com_a_tres(matrizes_combinadas_validas_camadas_1e2, matrizes_validas_camada3, matriz_entrada)
        '''

    end = time.time()
    exibe_tempo_processamento(start, end)
# ====================================
def tratando_as_camadas_um_e_dois(matrizes_validas_camada1, matrizes_validas_camada2, matriz_entrada):
    lista_matrizes_combinadas_validas = []
    for lista_camada1 in matrizes_validas_camada1:
        for lista_camada2 in matrizes_validas_camada2:
            lista_matrizes_combinadas_validas.append(lista_camada1+lista_camada2)

    matrizes_combinadas_validas_camadas_1e2 = []
    contador_matrizes_combinadas_validas = 0
    #print(' Tam lista => ',len(lista_matrizes_combinadas_validas))
    for k, item_lista in enumerate(lista_matrizes_combinadas_validas):
        matriz_teste = matriz_entrada.copy()

        if k >= 1000 and k // 1000 == 0:
            print('{} .'.format(k))

        for trinca in item_lista:
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor

        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
        if eh_valida:
            matrizes_combinadas_validas_camadas_1e2.append(item_lista)
            contador_matrizes_combinadas_validas += 1

    print(' Qtd matrizes combinadas validas das camadas 1 e 2: => {}'.format(contador_matrizes_combinadas_validas))
    return matrizes_combinadas_validas_camadas_1e2    
# ====================================
def tratando_o_resultado_das_camadas_um_e_dois_com_a_tres(matrizes_combinadas_validas_camadas_1e2, matrizes_validas_camada3, matriz_entrada):
    lista_matrizes_combinadas_validas = []
    for lista_camada1e2 in matrizes_combinadas_validas_camadas_1e2:
        for lista_camada3 in matrizes_validas_camada3:
            lista_matrizes_combinadas_validas.append(lista_camada1e2+lista_camada3)

    matrizes_combinadas_validas_todas_as_camadas = []
    contador_matrizes_combinadas_validas = 0
    for k, item_lista in enumerate(lista_matrizes_combinadas_validas):
        matriz_teste = matriz_entrada.copy()

        if k >= 1000 and k // 1000 == 0:
            print('{} .'.format(k))

        for trinca in item_lista:
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor

        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
        if eh_valida:
            matrizes_combinadas_validas_todas_as_camadas.append(item_lista)
            contador_matrizes_combinadas_validas += 1

    print(' Qtd matrizes combinadas do resultado das camadas 1 e 2 com a camada 3: => {}'.format(contador_matrizes_combinadas_validas))
    return matrizes_combinadas_validas_todas_as_camadas    
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


    if len(lista_02_possibs) > 0:
        print(' Celulas com 02 possibs : [', end='')
        for k,item in enumerate(lista_02_possibs):                
            if k != len(lista_02_possibs)-1:
                print('({},{}),'.format(item.linha,item.coluna), end='')
            if k == len(lista_02_possibs)-1:
                print('({},{})'.format(item.linha,item.coluna), end='')
        print(']')

    if len(lista_03_possibs) > 0:
        print(' Celulas com 03 possibs : [', end='')
        for k,item in enumerate(lista_03_possibs):                
            if k != len(lista_03_possibs)-1:
                print('({},{}),'.format(item.linha,item.coluna), end='')
            if k == len(lista_03_possibs)-1:
                print('({},{})'.format(item.linha,item.coluna), end='')
        print(']')

    if len(lista_04_possibs) > 0:
        print(' Celulas com 04 possibs : [', end='')
        for k,item in enumerate(lista_04_possibs):                
            if k != len(lista_04_possibs)-1:
                print('({},{}),'.format(item.linha,item.coluna), end='')
            if k == len(lista_04_possibs)-1:
                print('({},{})'.format(item.linha,item.coluna), end='')
        print(']')

    if len(lista_05_possibs) > 0:
        print(' Celulas com 05 possibs : [', end='')
        for k,item in enumerate(lista_05_possibs):                
            if k != len(lista_05_possibs)-1:
                print('({},{}),'.format(item.linha,item.coluna), end='')
            if k == len(lista_05_possibs)-1:
                print('({},{})'.format(item.linha,item.coluna), end='')
        print(']')

    if len(lista_06_possibs) > 0:
        print(' Celulas com 06 possibs : [', end='')
        for k,item in enumerate(lista_06_possibs):                
            if k != len(lista_06_possibs)-1:
                print('({},{}),'.format(item.linha,item.coluna), end='')
            if k == len(lista_06_possibs)-1:
                print('({},{})'.format(item.linha,item.coluna), end='')
        print(']')

    if len(lista_07_possibs) > 0:
        print(' Celulas com 07 possibs : [', end='')
        for k,item in enumerate(lista_07_possibs):                
            if k != len(lista_07_possibs)-1:
                print('({},{}),'.format(item.linha,item.coluna), end='')
            if k == len(lista_07_possibs)-1:
                print('({},{})'.format(item.linha,item.coluna), end='')
        print(']')

    return lista_02_possibs, lista_03_possibs, lista_04_possibs, lista_05_possibs, lista_06_possibs, lista_07_possibs
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

    '''
    a=len(mat_valid_02_possibs)
    b=len(mat_valid_03_possibs)
    c=len(mat_valid_04_possibs)
    d=len(mat_valid_05_possibs)
    e=len(mat_valid_06_possibs)
    f=len(mat_valid_07_possibs)

    total = 1
    if a>0:
        total *= a
    if b>0:
        total *= b
    if c>0:
        total *= c
    if d>0:
        total *= d
    if e>0:
        total *= e
    if f>0:
        total *= f
    '''
    #print(' Qtd total de trincas validas: {} * {} * {} * {} * {} * {} = {}'.format(a,b,c,d,e,f,total))    

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

    #print('tam lista => ',len(lista_matrizes_combinadas_validas))
    
    matrizes_combinadas_validas = []
    contador_matrizes_combinadas_validas = 0
    for k, item_lista in enumerate(lista_matrizes_combinadas_validas):
        matriz_teste = matriz_entrada.copy()

        if k >= 1000 and k // 1000 == 0:
            print('{} .'.format(k))

        for trinca in item_lista:
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor

        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
        if eh_valida:
            matrizes_combinadas_validas.append(item_lista)
            contador_matrizes_combinadas_validas += 1

    nome_camada = retorna_nome_camada(linha_inicio, linha_fim)
    print('Qtd matrizes combinadas validas na {} => {}'.format(nome_camada, contador_matrizes_combinadas_validas))
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
