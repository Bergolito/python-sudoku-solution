import numpy as np
import time
import datetime

from random import choice
from collections import Counter

from sudoku_utils import *
from sudoku import *
from solucao_arvore_geral import *
from solucao_arvore_02_possibs import monta_arvore_02_possibilidades
from solucao_arvore_03_possibs import monta_arvore_03_possibilidades
from solucao_arvore_04_possibs import monta_arvore_04_possibilidades
from solucao_arvore_05_possibs import monta_arvore_05_possibilidades
from solucao_arvore_06_possibs import monta_arvore_06_possibilidades
from solucao_arvore_07_possibs import monta_arvore_07_possibilidades

from solucao_arvore_geral import Posicao_Possibilidades, Trinca, retorna_lista_trincas, retorna_trincas, imprime_trincas, imprime_saida


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

        print(f'\n\n PASSO 1 - Analisando a camada horizontal 01') 
        matrizes_validas_camada1 = retorna_analise_camada_horizontal(1, matriz_entrada)
        tam1 = len(matrizes_validas_camada1)
        print(f'TAM camada 1 => {tam1}') # TAM camada 1 => 1328

        print(f'\n\n PASSO 2 - Analisando a camada horizontal 02') 
        matrizes_validas_camada2 = retorna_analise_camada_horizontal(2, matriz_entrada)
        tam2 = len(matrizes_validas_camada2)
        print(f'TAM camada 2 => {tam2}') # TAM camada 2 => 190

        print(f'\n\n PASSO 3 - Analisando as camadas combinadas horizontais 01 e 02') 
        lista_combinada_camada1_camada2 = monta_arvore(matrizes_validas_camada1, matrizes_validas_camada2, False)
        matrizes_validas_camadas_1e2 = retorna_lista_matrizes_validas(lista_combinada_camada1_camada2, matriz_entrada)
        imprime_arvore(matrizes_validas_camadas_1e2) 
        print(f'TAM camadas 1e2 => {len(matrizes_validas_camadas_1e2)}') 

        print(f'\n\n PASSO 3 - Analisando a camada horizontal 03') 
        matrizes_validas_camada3 = retorna_analise_camada_horizontal(3, matriz_entrada)
        tam3 = len(matrizes_validas_camada3)
        print(f'TAM camada 3 => {tam3}') # TAM camada 3 => 1288

        print(f'\n\n PASSO 4 - Analisando as camadas combinadas horizontais 1,2 COM 03') 
        lista_combinada_camadas1e2_camada3 = monta_arvore(matrizes_validas_camadas_1e2, matrizes_validas_camada3, False)
        matrizes_validas_camadas1e2_camada3 = retorna_lista_matrizes_validas(lista_combinada_camadas1e2_camada3, matriz_entrada)
        imprime_arvore(matrizes_validas_camadas1e2_camada3) 
        print(f'TAM camada 0e1 com 3 => {len(matrizes_validas_camadas1e2_camada3)}')

        print(f'Total matrizes validas = {len(matrizes_validas_camadas1e2_camada3)}')
        #Total matrizes validas = 1328 * 190 * 1288 = 324988160

    end = time.time()
    exibe_tempo_processamento(start, end)
# ====================================
def retorna_analise_camada_horizontal(numero_camada, matriz_entrada):
    matrizes_validas_linha0, matrizes_validas_linha1, matrizes_validas_linha2 = retorna_matrizes_validas_camada_horizontal(numero_camada, matriz_entrada)
    
    lista_combinada_mats_linha0_linha1 = monta_arvore(matrizes_validas_linha0, matrizes_validas_linha1, False)
    matrizes_validas_linhas_0e1 = retorna_lista_matrizes_validas(lista_combinada_mats_linha0_linha1, matriz_entrada)
    imprime_arvore(matrizes_validas_linhas_0e1) 

    lista_combinada_mats_0e1_linha2 = monta_arvore(matrizes_validas_linhas_0e1, matrizes_validas_linha2, False)
    matrizes_validas_linhas_0e1_linha2 = retorna_lista_matrizes_validas(lista_combinada_mats_0e1_linha2, matriz_entrada)
    imprime_arvore(matrizes_validas_linhas_0e1_linha2)          

    return matrizes_validas_linhas_0e1_linha2
# ====================================
def retorna_matrizes_validas_camada_horizontal(camada, matriz_entrada):

    if camada == 1:
        indices_linha = [0,1,2]
    elif camada == 2:
        indices_linha = [3,4,5]
    elif camada == 3:
        indices_linha = [6,7,8]

    lista_combinada_linha0 = retorna_arvore_linha(indices_linha[0], matriz_entrada)
    matrizes_validas_linha0 = retorna_lista_matrizes_validas(lista_combinada_linha0, matriz_entrada)
    imprime_arvore(matrizes_validas_linha0)

    lista_combinada_linha1 = retorna_arvore_linha(indices_linha[1], matriz_entrada)
    matrizes_validas_linha1 = retorna_lista_matrizes_validas(lista_combinada_linha1, matriz_entrada)
    imprime_arvore(matrizes_validas_linha1)
    
    lista_combinada_linha2 = retorna_arvore_linha(indices_linha[2], matriz_entrada)
    matrizes_validas_linha2 = retorna_lista_matrizes_validas(lista_combinada_linha2, matriz_entrada)
    imprime_arvore(matrizes_validas_linha2)
    
    tam1 = len(matrizes_validas_linha0)
    tam2 = len(matrizes_validas_linha1)
    tam3 = len(matrizes_validas_linha2)

    print(f'Total de combinacoes da camada {camada} = {tam1} * {tam2} * {tam3} = {(tam1*tam2*tam3)}')
    return matrizes_validas_linha0, matrizes_validas_linha1, matrizes_validas_linha2
# ====================================
def retorna_lista_matrizes_validas(lista_combinada_linha, matriz_entrada):
    matrizes_combinadas_validas = []
    contador_matrizes_combinadas_validas = 0

    for k, item_lista in enumerate(lista_combinada_linha):
        matriz_teste = matriz_entrada.copy()

        if type(item_lista) == str:
            tokens = item_lista.split('(')
            tokens_list = []    
            for tk in tokens:
                tk = tk.replace(')','')
                tokens_list.append(tk)
            
            lista_trincas = []
            for tk in tokens_list:
                if tk != '' and tk != '[]':
                    tokens_ = tk.split(',')
                    trinca = Trinca(int(tokens_[0]),int(tokens_[1]),int(tokens_[2]))
                    lista_trincas.append(trinca)

            for trinca in lista_trincas:
                matriz_teste[trinca.linha][trinca.coluna] = trinca.valor

            eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
            if eh_valida and '[]' not in item_lista:
                matrizes_combinadas_validas.append(item_lista)
                contador_matrizes_combinadas_validas += 1
    return matrizes_combinadas_validas        
# ====================================
def retorna_arvore_linha(numero_linha, matriz_entrada):
    linha = retorna_posicoes_possibilidades_linha(numero_linha, matriz_entrada)
    print(f'\nAnalisando a Linha {numero_linha}\n====================================')

    lista_final = []
    tam = 1
    for index, posicao in enumerate(linha):
        print(f'\n{posicao} ', end='')
        trincas = retorna_lista_trincas(posicao)
        print(f' |=> Trincas {len(trincas)} |=> ', end='')
        tam = tam * len(trincas)
        lista_teste = []
        for t in trincas:
            lista_teste.append(t)
            print(t, end='')
        lista_final.append(lista_teste)    
    
    lista_combinada_1_com2 = []
    lista_combinada_12_com3 = []
    lista_combinada_123_com4 = []
    lista_combinada_1234_com5 = []
    lista_combinada_12345_com6 = []
    lista_combinada_123456_com7 = []

    ultimo = -1
    for k,lista in enumerate(lista_final):
        if k == 0:
            lista_combinada_1_com2 = monta_arvore(lista_final[0], lista_final[1], False)
            ultimo = 0
        if k == 1:
            lista_combinada_12_com3 = monta_arvore(lista_combinada_1_com2, lista_final[2], False)
            ultimo = 1
        if k == 2:
            lista_combinada_123_com4 = monta_arvore(lista_combinada_12_com3, lista_final[3], False)
            ultimo = 2
        if k == 3:
            lista_combinada_1234_com5 = monta_arvore(lista_combinada_123_com4, lista_final[4], False)
            ultimo = 3
        if k == 4 and len(lista_final) > 5:
            lista_combinada_12345_com6 = monta_arvore(lista_combinada_1234_com5, lista_final[5], False)
            ultimo = 4
        if k == 5 and len(lista_final) > 6:
            lista_combinada_123456_com7 = monta_arvore(lista_combinada_12345_com6, lista_final[6], False)
            ultimo = 5

    lista_combinada = []
    if ultimo == 0:
        lista_combinada = lista_combinada_1_com2

    if ultimo == 1:
        lista_combinada = lista_combinada_12_com3

    elif ultimo == 2:
        lista_combinada = lista_combinada_123_com4

    elif ultimo == 3:
        lista_combinada = lista_combinada_1234_com5

    elif ultimo == 4:
        lista_combinada = lista_combinada_12345_com6

    elif ultimo == 5:
        lista_combinada = lista_combinada_123456_com7

    return lista_combinada
# ====================================
def imprime_arvore(lista_combinada):
    print(f'\n\nÁrvore => {len(lista_combinada)} registros: \n====================================')

    for k,it1 in enumerate(lista_combinada):
        concat = ''
        for it2 in it1:
            concat = concat + it2
        print(f'[{k}]->{concat}',end='\n')        
# ====================================
def multiplica_lista(lista):
    lista_combinada = []

    if len(lista) == 2:
        lista_combinada = [[],[]]
    elif len(lista) == 3:
        lista_combinada = [[],[],[]]
    elif len(lista) == 4:
        lista_combinada = [[],[],[],[]]
    elif len(lista) == 5:
        lista_combinada = [[],[],[],[],[]]
    elif len(lista) == 6:
        lista_combinada = [[],[],[],[],[],[]]
    elif len(lista) == 7:
        lista_combinada = [[],[],[],[],[],[],[]]

    return lista_combinada
# ====================================
def monta_arvore(lista1, lista2, flg_imprimir):
    lista_combinada_lista1_lista2 = multiplica_lista(lista2)

    for it1 in lista1:
        for it2 in lista2:
            lista_combinada_lista1_lista2.append(str(it1)+str(it2))

    del lista_combinada_lista1_lista2[0:4]

    if flg_imprimir:
        print('\nTam => ',len(lista_combinada_lista1_lista2))

        print(f'Arvore:',end='\n')
        for k,it1 in enumerate(lista_combinada_lista1_lista2):
            concat = ''
            for it2 in it1:
                concat = concat + it2
            print(f'[{k}]->{concat}',end='\n')        

    return lista_combinada_lista1_lista2
# ====================================
def retorna_lista_saida(lista_global):
    lista_saida = []
    for k, item1 in enumerate(lista_global):
        for item2 in item1:
            lista_saida.append(item2)
    return lista_saida
# ====================================
def retorna_posicoes_possibilidades_linha(linha, matriz):

    lista_possibs = []
    for j in range(9):
        if matriz[linha][j] == 0:
            lista = retorna_qtd_possibs_celula(linha, j, matriz)
            
            if len(lista) >= 2:
                lista_possibs.append(Posicao_Possibilidades(linha,j,lista))
    return lista_possibs
# ====================================


# ====================================


# ====================================
            