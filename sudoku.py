import numpy as np
import time
import datetime

from random import choice
from collections import Counter

from sudoku_utils import *

#CONJUNTO_COMPLETO = {1, 2, 3, 4, 5, 6, 7, 8, 9}

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

#   618725439 
#   754396281
#   392814657
#   127689543
#   485137962
#   963542178
#   531968724
#   279453816
#   846271395
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
    imprime_matriz_numerica(MATRIZ_ENTRADA_02,' MATRIZ ENTRADA ')
    for i in range(LOOPS):
        matriz_entrada = MATRIZ_ENTRADA_02

        mat, eh_valida = validacao(matriz_entrada)
        if eh_valida:
            achou_solucao = True
            
            print('===========================================')
            print(f' Achou uma matriz válida na {(i+1)}ª interação: ')
            print('===========================================')

            imprime_matriz_numerica(mat,' MATRIZ RESULTANTE ')
            break
            
    if not achou_solucao:
        print('===========================================')
        print('Em {} interações, não achou a solução: '.format(LOOPS))
        print('===========================================')

        cam_hor_01 = analise_cam_horinzontal_01(matriz_entrada)
        cam_hor_02 = analise_cam_horinzontal_02(matriz_entrada)
        cam_hor_03 = analise_cam_horinzontal_03(matriz_entrada)
        
        lista_comb_camadas1e2 = monta_arvore(cam_hor_01, cam_hor_02, False)
        matrizes_validas_cams_1e2 = retorna_lista_matrizes_validas(lista_comb_camadas1e2, matriz_entrada)
        
        lista_comb_camadas1e2_cam3 = monta_arvore(matrizes_validas_cams_1e2, cam_hor_03, False)
        matrizes_validas_cams1e2_cam3 = retorna_lista_matrizes_validas(lista_comb_camadas1e2_cam3, matriz_entrada)
        imprime_matriz_resultante(matrizes_validas_cams1e2_cam3, matriz_entrada)    

    end = time.time()
    exibe_tempo_processamento(start, end)
# ====================================
def imprime_matriz_resultante(matriz, matriz_entrada):

    item_lista = matriz[0]    

    imprime_matriz_numerica(matriz_entrada,' MATRIZ ENTRADA ')
    matriz_teste = matriz_entrada.copy()
    if type(item_lista) == str:
        lista_trincas = recebe_lista_retorna_trincas(item_lista)
        for item in lista_trincas:
            trinca = str(item)
            trinca = trinca.replace('(','')
            trinca = trinca.replace(')','')            
            tokens_ = trinca.split(',')
            trinca = Trinca(int(tokens_[0]),int(tokens_[1]),int(tokens_[2]))
            matriz_teste[trinca.linha][trinca.coluna] = trinca.valor

        eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)        

        if eh_valida:
            imprime_matriz_numerica(matriz_teste,' MATRIZ RESULTANTE ')
    return matriz_teste    
# ====================================
def imprime_matriz_numerica(matriz, mensagem):
    print(f'\n================================== \n\n {mensagem} \n================================== \n ')
    for i in range(0,9):
        print('[ ',end='')
        for j in range(0, 9):
            if matriz[i][j] != 0:
                print(f'{matriz[i][j]} ', end='')
            if matriz[i][j] == 0:
                print(f'_ ', end='')
        print(']')    
# ====================================
def analise_cam_horinzontal_01(matriz_entrada):
    print(f'\nAnalisando a camada horizontal 01 => \n')

    linha0 = retorno_linha_numero(0, matriz_entrada)
    matrizes_validas_linha0 = retorna_lista_matrizes_validas(linha0, matriz_entrada)

    linha1 = retorno_linha_numero(1, matriz_entrada)
    matrizes_validas_linha1 = retorna_lista_matrizes_validas(linha1, matriz_entrada)
    
    linha2 = retorno_linha_numero(2, matriz_entrada)
    matrizes_validas_linha2 = retorna_lista_matrizes_validas(linha2, matriz_entrada)

    lista_combinada_mats_linha0_linha1 = monta_arvore(matrizes_validas_linha0, matrizes_validas_linha1, False)
    matrizes_validas_linhas_0e1 = retorna_lista_matrizes_validas(lista_combinada_mats_linha0_linha1, matriz_entrada)

    lista_combinada_mats_0e1_linha2 = monta_arvore(matrizes_validas_linhas_0e1, matrizes_validas_linha2, False)
    matrizes_validas_linhas_0e1_linha2 = retorna_lista_matrizes_validas(lista_combinada_mats_0e1_linha2, matriz_entrada)

    print(f'Camada Horizontal 01 => {len(matrizes_validas_linhas_0e1_linha2)} Matrizes Válidas')

    return matrizes_validas_linhas_0e1_linha2
# ====================================
def analise_cam_horinzontal_02(matriz_entrada):
    print(f'\nAnalisando a camada horizontal 02 => \n')

    linha3 = retorno_linha_numero(3, matriz_entrada)
    matrizes_validas_linha3 = retorna_lista_matrizes_validas(linha3, matriz_entrada)

    linha4 = retorno_linha_numero(4, matriz_entrada)
    matrizes_validas_linha4 = retorna_lista_matrizes_validas(linha4, matriz_entrada)
    
    linha5 = retorno_linha_numero(5, matriz_entrada)

    matrizes_validas_linha5 = retorna_lista_matrizes_validas(linha5, matriz_entrada)

    lista_combinada_mats_linha3_linha4 = monta_arvore(matrizes_validas_linha3, matrizes_validas_linha4, False)
    matrizes_validas_linhas_3e4 = retorna_lista_matrizes_validas(lista_combinada_mats_linha3_linha4, matriz_entrada)

    lista_combinada_mats_3e4_linha5 = monta_arvore(matrizes_validas_linhas_3e4, matrizes_validas_linha5, False)
    matrizes_validas_linhas_3e4_linha5 = retorna_lista_matrizes_validas(lista_combinada_mats_3e4_linha5, matriz_entrada)

    print(f'Camada Horizontal 02 => {len(matrizes_validas_linhas_3e4_linha5)} Matrizes Válidas')

    return matrizes_validas_linhas_3e4_linha5
# ====================================
def analise_cam_horinzontal_03(matriz_entrada):
    print(f'\nAnalisando a camada horizontal 03 => \n')

    linha6 = retorno_linha_numero(6, matriz_entrada)
    matrizes_validas_linha6 = retorna_lista_matrizes_validas(linha6, matriz_entrada)

    linha7 = retorno_linha_numero(7, matriz_entrada)
    matrizes_validas_linha7 = retorna_lista_matrizes_validas(linha7, matriz_entrada)
    
    linha8 = retorno_linha_numero(8, matriz_entrada)
    matrizes_validas_linha8 = retorna_lista_matrizes_validas(linha8, matriz_entrada)

    lista_combinada_mats_linha6_linha7 = monta_arvore(matrizes_validas_linha6, matrizes_validas_linha7, False)
    matrizes_validas_linhas_6e7 = retorna_lista_matrizes_validas(lista_combinada_mats_linha6_linha7, matriz_entrada)

    lista_combinada_mats_6e7_linha8 = monta_arvore(matrizes_validas_linhas_6e7, matrizes_validas_linha8, False)
    matrizes_validas_linhas_6e7_linha8 = retorna_lista_matrizes_validas(lista_combinada_mats_6e7_linha8, matriz_entrada)

    print(f'Camada Horizontal 03 => {len(matrizes_validas_linhas_6e7_linha8)} Matrizes Válidas')

    return matrizes_validas_linhas_6e7_linha8
# ====================================
def retorno_linha_numero(numero_linha, matriz_entrada):
    print(f'\nAnalisando a Linha {numero_linha}: ', end='')
    lista_posicao_linha = retorna_posicoes_possibilidades_linha(numero_linha, matriz_entrada)

    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    lista6 = []
    lista7 = []
    lista8 = []

    lista_final = multiplica_lista(lista_posicao_linha)
    for k,posicao in enumerate(lista_posicao_linha):
        lista_trincas = retorna_lista_trincas(posicao)

        if k == 0:
            for tr in lista_trincas:
                lista1.append(tr)                                
        if k == 1:
            for tr in lista_trincas:
                lista2.append(tr)
        if k == 2:
            for tr in lista_trincas:
                lista3.append(tr)
        if k == 3:
            for tr in lista_trincas:
                lista4.append(tr)
        if k == 4:
            for tr in lista_trincas:
                lista5.append(tr)
        if k == 5:
            for tr in lista_trincas:
                lista6.append(tr)
        if k == 6:
            for tr in lista_trincas:
                lista7.append(tr)
        if k == 7:
            for tr in lista_trincas:
                lista8.append(tr)

    if len(lista8) > 0:
        lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
        lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
        lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
        lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)
        lista_combina_lista12345_com_lista6 = monta_arvore(lista_combina_lista1234_com_lista5, lista6, False)
        lista_combina_lista123456_com_lista7 = monta_arvore(lista_combina_lista12345_com_lista6, lista7, False)
        lista_combina_lista1234567_com_lista8 = monta_arvore(lista_combina_lista123456_com_lista7, lista8, False)

        print(f'Total de registros: {len(lista_combina_lista1234567_com_lista8)}')
        return lista_combina_lista1234567_com_lista8

    if len(lista7) > 0:
        lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
        lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
        lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
        lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)
        lista_combina_lista12345_com_lista6 = monta_arvore(lista_combina_lista1234_com_lista5, lista6, False)
        lista_combina_lista123456_com_lista7 = monta_arvore(lista_combina_lista12345_com_lista6, lista7, False)

        print(f'Total de registros: {len(lista_combina_lista123456_com_lista7)}')
        return lista_combina_lista123456_com_lista7

    if len(lista6) > 0:
        lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
        lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
        lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
        lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)
        lista_combina_lista12345_com_lista6 = monta_arvore(lista_combina_lista1234_com_lista5, lista6, False)

        print(f'Total de registros: {len(lista_combina_lista12345_com_lista6)}')
        return lista_combina_lista12345_com_lista6

    if len(lista5) > 0:
        lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
        lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
        lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
        lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)

        print(f'Total de registros: {len(lista_combina_lista1234_com_lista5)}')
        return lista_combina_lista1234_com_lista5
# ====================================
def imprime_arvore(lista_combinada):
    print(f'\n\nÁrvore => {len(lista_combinada)} registros: \n====================================')

    for k,it1 in enumerate(lista_combinada):
        print(f'[{k}]->{it1}',end='\n')   
# ====================================
def monta_arvore(lista1, lista2, flg_imprimir):
    lista_combinada_lista1_lista2 = multiplica_lista(lista2)

    for it1 in lista1:
        for it2 in lista2:
            lista_combinada_lista1_lista2.append(str(it1)+str(it2))

    if flg_imprimir:
        print('\nTam => ',len(lista_combinada_lista1_lista2))

        print(f'Arvore:',end='\n')
        for k,it1 in enumerate(lista_combinada_lista1_lista2):
            concat = ''
            for it2 in it1:
                concat = concat + it2
            print(f'[{k}]->{concat}',end='\n')        

    lista_combina_lista_e_lista2_ajustada = []
    for k,it1 in enumerate(lista_combinada_lista1_lista2):
        if isinstance(it1, str) and it1 != '':
            lista_combina_lista_e_lista2_ajustada.append(it1)


    return lista_combina_lista_e_lista2_ajustada 
# ====================================
def retorna_lista_matrizes_validas(lista_combinada_linha, matriz_entrada):
    matrizes_combinadas_validas = []
    contador_matrizes_combinadas_validas = 0

    for k, item_lista in enumerate(lista_combinada_linha):
        matriz_teste = matriz_entrada.copy()

        if type(item_lista) == str:
            lista_trincas = recebe_lista_retorna_trincas(item_lista)
            for trinca in lista_trincas:
                matriz_teste[trinca.linha][trinca.coluna] = trinca.valor

            eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
            if eh_valida and '[]' not in item_lista:
                matrizes_combinadas_validas.append(item_lista)
                contador_matrizes_combinadas_validas += 1
    return matrizes_combinadas_validas       
# ====================================
def recebe_lista_retorna_trincas(item_lista):
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

    return lista_trincas
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

    #del lista_combinada_lista1_lista2[0:4]

    if flg_imprimir:
        print('\nTam => ',len(lista_combinada_lista1_lista2))

        print(f'Arvore:',end='\n')
        for k,it1 in enumerate(lista_combinada_lista1_lista2):
            concat = ''
            for it2 in it1:
                concat = concat + it2
            print(f'[{k}]->{concat}',end='\n')        

    lista_combina_lista_e_lista2_ajustada = []
    for k,it1 in enumerate(lista_combinada_lista1_lista2):
        if isinstance(it1, str) and it1 != '':
            lista_combina_lista_e_lista2_ajustada.append(it1)


    return lista_combina_lista_e_lista2_ajustada
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
if __name__ == '__main__':
    inicio()
# ====================================  