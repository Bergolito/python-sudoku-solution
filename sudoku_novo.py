import numpy as np
import time
import datetime

from random import choice
from collections import Counter

from sudoku_utils import *
from sudoku import *
from solucao_arvore_geral import *
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

        cam_hor_01 = analise_cam_horinzontal_01(matriz_entrada)
        cam_hor_02 = analise_cam_horinzontal_02(matriz_entrada)
        cam_hor_03 = analise_cam_horinzontal_03(matriz_entrada)
        
        lista_comb_camadas1e2 = monta_arvore(cam_hor_01, cam_hor_02, False)
        matrizes_validas_cams_1e2 = retorna_lista_matrizes_validas(lista_comb_camadas1e2, matriz_entrada)
        
        lista_comb_camadas1e2_cam3 = monta_arvore(matrizes_validas_cams_1e2, cam_hor_03, False)
        matrizes_validas_cams1e2_cam3 = retorna_lista_matrizes_validas(lista_comb_camadas1e2_cam3, matriz_entrada)

        #imprime_arvore(matrizes_validas_cams1e2_cam3) 
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

# ====================================
def analise_cam_horinzontal_01(matriz_entrada):
    print(f'\nAnalisando a camada horizontal 01 => \n')

    linha0 = retorno_linha0(matriz_entrada)
    matrizes_validas_linha0 = retorna_lista_matrizes_validas(linha0, matriz_entrada)

    linha1 = retorno_linha1(matriz_entrada)
    matrizes_validas_linha1 = retorna_lista_matrizes_validas(linha1, matriz_entrada)
    
    # 34560 registro
    linha2 = retorno_linha2(matriz_entrada)
    matrizes_validas_linha2 = retorna_lista_matrizes_validas(linha2, matriz_entrada)

    lista_combinada_mats_linha0_linha1 = monta_arvore(matrizes_validas_linha0, matrizes_validas_linha1, False)
    matrizes_validas_linhas_0e1 = retorna_lista_matrizes_validas(lista_combinada_mats_linha0_linha1, matriz_entrada)

    lista_combinada_mats_0e1_linha2 = monta_arvore(matrizes_validas_linhas_0e1, matrizes_validas_linha2, False)
    matrizes_validas_linhas_0e1_linha2 = retorna_lista_matrizes_validas(lista_combinada_mats_0e1_linha2, matriz_entrada)

    print(f'\nCamada Horizontal 01 => {len(matrizes_validas_linhas_0e1_linha2)} Matrizes Válidas')

    return matrizes_validas_linhas_0e1_linha2
# ====================================
def analise_cam_horinzontal_02(matriz_entrada):
    print(f'\nAnalisando a camada horizontal 02 => \n')

    linha3 = retorno_linha3(matriz_entrada)
    matrizes_validas_linha3 = retorna_lista_matrizes_validas(linha3, matriz_entrada)

    linha4 = retorno_linha4(matriz_entrada)
    matrizes_validas_linha4 = retorna_lista_matrizes_validas(linha4, matriz_entrada)
    
    linha5 = retorno_linha5(matriz_entrada)
    matrizes_validas_linha5 = retorna_lista_matrizes_validas(linha5, matriz_entrada)

    lista_combinada_mats_linha3_linha4 = monta_arvore(matrizes_validas_linha3, matrizes_validas_linha4, False)
    matrizes_validas_linhas_3e4 = retorna_lista_matrizes_validas(lista_combinada_mats_linha3_linha4, matriz_entrada)

    lista_combinada_mats_3e4_linha5 = monta_arvore(matrizes_validas_linhas_3e4, matrizes_validas_linha5, False)
    matrizes_validas_linhas_3e4_linha5 = retorna_lista_matrizes_validas(lista_combinada_mats_3e4_linha5, matriz_entrada)

    print(f'\n\nCamada Horizontal 02 => {len(matrizes_validas_linhas_3e4_linha5)} Matrizes Válidas')

    return matrizes_validas_linhas_3e4_linha5
# ====================================
def analise_cam_horinzontal_03(matriz_entrada):
    print(f'\nAnalisando a camada horizontal 03 => \n')

    linha6 = retorno_linha6(matriz_entrada)
    matrizes_validas_linha6 = retorna_lista_matrizes_validas(linha6, matriz_entrada)

    linha7 = retorno_linha7(matriz_entrada)
    matrizes_validas_linha7 = retorna_lista_matrizes_validas(linha7, matriz_entrada)
    
    linha8 = retorno_linha8(matriz_entrada)
    matrizes_validas_linha8 = retorna_lista_matrizes_validas(linha8, matriz_entrada)

    lista_combinada_mats_linha6_linha7 = monta_arvore(matrizes_validas_linha6, matrizes_validas_linha7, False)
    matrizes_validas_linhas_6e7 = retorna_lista_matrizes_validas(lista_combinada_mats_linha6_linha7, matriz_entrada)

    lista_combinada_mats_6e7_linha8 = monta_arvore(matrizes_validas_linhas_6e7, matrizes_validas_linha8, False)
    matrizes_validas_linhas_6e7_linha8 = retorna_lista_matrizes_validas(lista_combinada_mats_6e7_linha8, matriz_entrada)

    #imprime_arvore(matrizes_validas_linhas_6e7_linha8)   
    print(f'\nCamada Horizontal 03 => {len(matrizes_validas_linhas_6e7_linha8)} Matrizes Válidas')

    return matrizes_validas_linhas_6e7_linha8
# ====================================

# ====================================
def retorno_linha0(matriz_entrada):
    '''
    (0,3)=[3, 5, 7]  |=> Trincas 3 |=> (0,3,3)(0,3,5)(0,3,7)
    (0,4)=[2, 3, 5, 7]  |=> Trincas 4 |=> (0,4,2)(0,4,3)(0,4,5)(0,4,7)
    (0,5)=[2, 5, 7]  |=> Trincas 3 |=> (0,5,2)(0,5,5)(0,5,7)
    (0,7)=[9, 2, 3, 5]  |=> Trincas 4 |=> (0,7,9)(0,7,2)(0,7,3)(0,7,5)
    (0,8)=[9, 2]  |=> Trincas 2 |=> (0,8,9)(0,8,2)
    '''
    #Analisando a Linha 0: Total de registros: 288
    print(f'\nAnalisando a Linha 0: ', end='')
    
    #(0,3,3)(0,3,5)(0,3,7)
    trinca1 = Trinca(0,3,3)
    trinca2 = Trinca(0,3,5)
    trinca3 = Trinca(0,3,7)
    lista1 = [trinca1, trinca2, trinca3]

    #(0,4,2)(0,4,3)(0,4,5)(0,4,7)
    trinca4 = Trinca(0,4,2)
    trinca5 = Trinca(0,4,3)
    trinca6 = Trinca(0,4,5)
    trinca7 = Trinca(0,4,7)
    lista2 = [trinca4, trinca5, trinca6, trinca7] 

    #(0,5,2)(0,5,5)(0,5,7)
    trinca8 = Trinca(0,5,2)
    trinca9 = Trinca(0,5,5)
    trinca10 = Trinca(0,5,7)
    lista3 = [trinca8, trinca9, trinca10] 

    #(0,7,9)(0,7,2)(0,7,3)(0,7,5)
    trinca11 = Trinca(0,7,9)
    trinca12 = Trinca(0,7,2)
    trinca13 = Trinca(0,7,3)
    trinca14 = Trinca(0,7,5)
    lista4 = [trinca11, trinca12, trinca13, trinca14] 

    #(0,8,9)(0,8,2)
    trinca15 = Trinca(0,8,9)
    trinca16 = Trinca(0,8,2)
    lista5 = [trinca15, trinca16] 

    lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
    lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
    lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
    lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)

    #Analisando a Linha 0: Total de registros: 288
    print(f'Total de registros: {len(lista_combina_lista1234_com_lista5)}')

    return lista_combina_lista1234_com_lista5
# ====================================
# ====================================
def retorno_linha3(matriz_entrada):
    '''
    0=>(3,0)=[1, 2, 5, 7]  |=> Trincas 4 |=> 
    1=>(3,1)=[2, 5]  |=> Trincas 2 |=> 
    2=>(3,2)=[1, 2, 5, 7]  |=> Trincas 4 |=> 
    3=>(3,6)=[1, 2, 5]  |=> Trincas 3 |=> 
    4=>(3,7)=[1, 2, 4, 5, 7]  |=> Trincas 5 |=> =>tipo <class 'int'> 0
    '''
    print(f'\nAnalisando a Linha 3: ', end='')

    #0=>(3,0)=[1, 2, 5, 7]
    trinca1 = Trinca(3,0,1)
    trinca2 = Trinca(3,0,2)
    trinca3 = Trinca(3,0,5)
    trinca4 = Trinca(3,0,7)
    lista1 = [trinca1, trinca2, trinca3, trinca4]

    #1=>(3,1)=[2, 5]
    trinca5 = Trinca(3,1,2)
    trinca6 = Trinca(3,1,5)
    lista2 = [trinca5, trinca6] 

    #2=>(3,2)=[1, 2, 5, 7]
    trinca7 = Trinca(3,2,1)
    trinca8 = Trinca(3,2,2)
    trinca9 = Trinca(3,2,5)
    trinca10 = Trinca(3,2,7)
    lista3 = [trinca7, trinca8, trinca9, trinca10] 

    #3=>(3,6)=[1, 2, 5]
    trinca11 = Trinca(3,6,1)
    trinca12 = Trinca(3,6,2)
    trinca13 = Trinca(3,6,5)
    lista4 = [trinca11, trinca12, trinca13] 

    #4=>(3,7)=[1, 2, 4, 5, 7]
    trinca14 = Trinca(3,7,1)
    trinca15 = Trinca(3,7,2)
    trinca16 = Trinca(3,7,4)
    trinca17 = Trinca(3,7,5)
    trinca18 = Trinca(3,7,7)
    lista5 = [trinca14, trinca15, trinca16, trinca17, trinca18] 

    lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
    lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
    lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
    lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)

    print(f'Total de registros: {len(lista_combina_lista1234_com_lista5)}')

    return lista_combina_lista1234_com_lista5
# ====================================
def retorno_linha4(matriz_entrada):
    '''
    0=>(4,1)=[2, 3, 5, 6, 8]  |=> Trincas 5 |=> 
    1=>(4,2)=[2, 3, 5, 6, 7]  |=> Trincas 5 |=> 
    2=>(4,4)=[2, 3, 5, 7]  |=> Trincas 4 |=> 
    3=>(4,5)=[2, 5, 7]  |=> Trincas 3 |=> 
    4=>(4,6)=[9, 2, 5, 6]  |=> Trincas 4 |=> 
    5=>(4,7)=[2, 5, 6, 7, 9]  |=> Trincas 5 |=> 
    6=>(4,8)=[9, 2]  |=> Trincas 2 |=> =>tipo <class 'int'> 0
    '''
    print(f'\nAnalisando a Linha 4: ', end='')

    #0=>(4,1)=[2, 3, 5, 6, 8]
    trinca1 = Trinca(4,1,2)
    trinca2 = Trinca(4,1,3)
    trinca3 = Trinca(4,1,5)
    trinca4 = Trinca(4,1,6)
    trinca5 = Trinca(4,1,8)
    lista1 = [trinca1, trinca2, trinca3, trinca4, trinca5]

    #1=>(4,2)=[2, 3, 5, 6, 7]
    trinca6 = Trinca(4,2,2)
    trinca7 = Trinca(4,2,3)
    trinca8 = Trinca(4,2,5)
    trinca9 = Trinca(4,2,6)
    trinca10 = Trinca(4,2,7)
    lista2 = [trinca6, trinca7, trinca8, trinca9, trinca10] 

    #2=>(4,4)=[2, 3, 5, 7]
    trinca11 = Trinca(4,4,2)
    trinca12 = Trinca(4,4,3)
    trinca13 = Trinca(4,4,5)
    trinca14 = Trinca(4,4,7)
    lista3 = [trinca11, trinca12, trinca13, trinca14] 

    #3=>(4,5)=[2, 5, 7]
    trinca15 = Trinca(4,5,2)
    trinca16 = Trinca(4,5,5)
    trinca17 = Trinca(4,5,7)
    lista4 = [trinca15, trinca16, trinca17] 

    #4=>(4,6)=[9, 2, 5, 6]
    trinca18 = Trinca(4,6,9)
    trinca19 = Trinca(4,6,2)
    trinca20 = Trinca(4,6,5)
    trinca21 = Trinca(4,6,6)
    lista5 = [trinca18, trinca19, trinca20, trinca21] 

    #5=>(4,7)=[2, 5, 6, 7, 9]
    trinca22 = Trinca(4,7,2)
    trinca23 = Trinca(4,7,5)
    trinca24 = Trinca(4,7,6)
    trinca25 = Trinca(4,7,7)
    trinca26 = Trinca(4,7,9)
    lista6 = [trinca22, trinca23,trinca24, trinca25,trinca26] 

    #6=>(4,8)=[9, 2]
    trinca27 = Trinca(4,8,9)
    trinca28 = Trinca(4,8,2)
    lista7 = [trinca27, trinca28] 

    lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
    lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
    lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
    lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)
    lista_combina_lista12345_com_lista6 = monta_arvore(lista_combina_lista1234_com_lista5, lista6, False)
    lista_combina_lista123456_com_lista7 = monta_arvore(lista_combina_lista12345_com_lista6, lista7, False)

    print(f'Total de registros: {len(lista_combina_lista123456_com_lista7)}')

    return lista_combina_lista123456_com_lista7
# ====================================
# ====================================
def retorno_linha5(matriz_entrada):
    '''
    0=>(5,1)=[2, 3, 5, 6]  |=> Trincas 4 |=> 
    1=>(5,2)=[1, 2, 3, 5, 6, 7]  |=> Trincas 6 |=> 
    2=>(5,3)=[3, 5, 7]  |=> Trincas 3 |=> 
    3=>(5,5)=[2, 5, 7]  |=> Trincas 3 |=> 
    4=>(5,6)=[1, 2, 5, 6]  |=> Trincas 4 |=> 
    5=>(5,7)=[1, 2, 5, 6, 7]  |=> Trincas 5 |=> =>tipo <class 'int'> 0
    '''
    print(f'\nAnalisando a Linha 5: ', end='')

    #0=>(5,1)=[2, 3, 5, 6]
    trinca1 = Trinca(5,1,2)
    trinca2 = Trinca(5,1,3)
    trinca3 = Trinca(5,1,5)
    trinca4 = Trinca(5,1,6)
    lista1 = [trinca1, trinca2, trinca3, trinca4]

    #1=>(5,2)=[1, 2, 3, 5, 6, 7]
    trinca5 = Trinca(5,2,1)
    trinca6 = Trinca(5,2,2)
    trinca7 = Trinca(5,2,3)
    trinca8 = Trinca(5,2,5)
    trinca9 = Trinca(5,2,6)
    trinca10 = Trinca(5,2,7)
    lista2 = [trinca5, trinca6, trinca7, trinca8, trinca9, trinca10] 

    #2=>(5,3)=[3, 5, 7]
    trinca11 = Trinca(5,3,3)
    trinca12 = Trinca(5,3,5)
    trinca13 = Trinca(5,3,7)
    lista3 = [trinca11, trinca12, trinca13] 

    #3=>(5,5)=[2, 5, 7]
    trinca14 = Trinca(5,5,2)
    trinca15 = Trinca(5,5,5)
    trinca16 = Trinca(5,5,7)
    lista4 = [trinca14, trinca15, trinca16] 

    #4=>(5,6)=[1, 2, 5, 6]
    trinca17 = Trinca(5,6,1)
    trinca18 = Trinca(5,6,2)
    trinca19 = Trinca(5,6,5)
    trinca20 = Trinca(5,6,6)
    lista5 = [trinca17, trinca18, trinca19, trinca20] 

    #5=>(5,7)=[1, 2, 5, 6, 7]
    trinca21 = Trinca(5,7,1)
    trinca22 = Trinca(5,7,2)
    trinca23 = Trinca(5,7,5)
    trinca24 = Trinca(5,7,6)
    trinca25 = Trinca(5,7,7)
    lista6 = [trinca21, trinca22, trinca23, trinca24, trinca25] 

    lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
    lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
    lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
    lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)
    lista_combina_lista12345_com_lista6 = monta_arvore(lista_combina_lista1234_com_lista5, lista6, False)

    print(f'Total de registros: {len(lista_combina_lista12345_com_lista6)}')

    return lista_combina_lista12345_com_lista6
# ====================================
# ====================================
def retorno_linha6(matriz_entrada):
    '''
    0=>(6,0)=[1, 2, 3, 5, 8]  |=> Trincas 5 |=> 
    1=>(6,1)=[2, 3, 5, 6, 8, 9]  |=> Trincas 6 |=> 
    2=>(6,2)=[1, 2, 3, 5, 6, 9]  |=> Trincas 6 |=> 
    3=>(6,3)=[9, 4, 5]  |=> Trincas 3 |=> 
    4=>(6,4)=[1, 5, 6]  |=> Trincas 3 |=> 
    5=>(6,5)=[8, 1, 4, 5]  |=> Trincas 4 |=> 
    6=>(6,7)=[1, 2, 3, 4, 8, 9]  |=> Trincas 6 |=> 
    7=>(6,8)=[1, 2, 4, 9]  |=> Trincas 4 |=> =>tipo <class 'int'> 0
    '''
    print(f'\nAnalisando a Linha 6: ', end='')

    #0=>(6,0)=[1, 2, 3, 5, 8]
    trinca1 = Trinca(6,0,1)
    trinca2 = Trinca(6,0,2)
    trinca30 = Trinca(6,0,3)
    trinca31 = Trinca(6,0,5)
    trinca32 = Trinca(6,0,8)
    lista1 = [trinca1, trinca2, trinca30, trinca31, trinca32]

    #1=>(6,1)=[2, 3, 5, 6, 8, 9]
    trinca4 = Trinca(6,1,2)
    trinca5 = Trinca(6,1,3)
    trinca6 = Trinca(6,1,5)
    trinca70 = Trinca(6,1,6)
    trinca71 = Trinca(6,1,8)
    trinca72 = Trinca(6,1,9)
    lista2 = [trinca4, trinca5, trinca6, trinca70, trinca71, trinca72] 

    #2=>(6,2)=[1, 2, 3, 5, 6, 9]
    trinca8 = Trinca(6,2,1)
    trinca9 = Trinca(6,2,2)
    trinca10 = Trinca(6,2,3)
    trinca101 = Trinca(6,2,5)
    trinca102 = Trinca(6,2,6)
    trinca103 = Trinca(6,2,9)
    lista3 = [trinca8, trinca9, trinca10, trinca101, trinca102, trinca103] 

    #3=>(6,3)=[9, 4, 5]
    trinca11 = Trinca(6,3,9)
    trinca12 = Trinca(6,3,4)
    trinca13 = Trinca(6,3,5)
    lista4 = [trinca11, trinca12, trinca13] 

    #4=>(6,4)=[1, 5, 6]
    trinca15 = Trinca(6,4,1)
    trinca16 = Trinca(6,4,5)
    trinca17 = Trinca(6,4,6)
    lista5 = [trinca15, trinca16, trinca17] 

    #5=>(6,5)=[8, 1, 4, 5]
    trinca18 = Trinca(6,5,8)
    trinca19 = Trinca(6,5,1)
    trinca20 = Trinca(6,5,4)
    trinca21 = Trinca(6,5,5)
    lista6 = [trinca18, trinca18, trinca20, trinca21] 

    #6=>(6,7)=[1, 2, 3, 4, 8, 9]
    trinca22 = Trinca(6,7,1)
    trinca23 = Trinca(6,7,2)
    trinca24 = Trinca(6,7,3)
    trinca25 = Trinca(6,7,4)
    trinca26 = Trinca(6,7,8)
    trinca27 = Trinca(6,7,9)
    lista7 = [trinca22, trinca23, trinca24, trinca25, trinca26, trinca27] 

    #7=>(6,8)=[1, 2, 4, 9]
    trinca28 = Trinca(6,8,1)
    trinca29 = Trinca(6,8,2)
    trinca30 = Trinca(6,8,4)
    trinca31 = Trinca(6,8,9)
    lista8 = [trinca28, trinca29, trinca30, trinca31] 

    lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
    lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
    lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
    lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)
    lista_combina_lista12345_com_lista6 = monta_arvore(lista_combina_lista1234_com_lista5, lista6, False)
    lista_combina_lista123456_com_lista7 = monta_arvore(lista_combina_lista12345_com_lista6, lista7, False)
    lista_combina_lista1234567_com_lista8 = monta_arvore(lista_combina_lista123456_com_lista7, lista8, False)

    print(f'Total de registros: {len(lista_combina_lista1234567_com_lista8)}')

    return lista_combina_lista1234567_com_lista8
# ====================================
# ====================================
def retorno_linha7(matriz_entrada):
    '''
    0=>(7,0)=[8, 1, 2, 5]  |=> Trincas 4 |=> 
    1=>(7,2)=[1, 2, 5, 9]  |=> Trincas 4 |=> 
    2=>(7,3)=[9, 4, 5]  |=> Trincas 3 |=> 
    3=>(7,4)=[1, 5]  |=> Trincas 2 |=> 
    4=>(7,6)=[8, 1, 2, 9]  |=> Trincas 4 |=> 
    5=>(7,7)=[1, 2, 4, 8, 9]  |=> Trincas 5 |=> =>tipo <class 'int'> 0
    '''
    print(f'\nAnalisando a Linha 7: ', end='')

    #0=>(7,0)=[8, 1, 2, 5]
    trinca1 = Trinca(7,0,8)
    trinca2 = Trinca(7,0,1)
    trinca3 = Trinca(7,0,2)
    trinca4 = Trinca(7,0,5)
    lista1 = [trinca1, trinca2, trinca3, trinca4]

    #1=>(7,2)=[1, 2, 5, 9]
    trinca5 = Trinca(7,2,1)
    trinca6 = Trinca(7,2,2)
    trinca7 = Trinca(7,2,5)
    trinca8 = Trinca(7,2,9)
    lista2 = [trinca5, trinca6, trinca7, trinca8] 

    #2=>(7,3)=[9, 4, 5]
    trinca9 = Trinca(7,3,9)
    trinca10 = Trinca(7,3,4)
    trinca11 = Trinca(7,3,5)
    lista3 = [trinca9, trinca10, trinca11] 

    #3=>(7,4)=[1, 5] 
    trinca12 = Trinca(7,4,1)
    trinca13 = Trinca(7,4,5)
    lista4 = [trinca12, trinca13] 

    #4=>(7,6)=[8, 1, 2, 9]
    trinca14 = Trinca(7,6,8)
    trinca15 = Trinca(7,6,1)
    trinca16 = Trinca(7,6,2)
    trinca17 = Trinca(7,6,9)
    lista5 = [trinca14, trinca15, trinca16, trinca17] 

    #5=>(7,7)=[1, 2, 4, 8, 9]
    trinca18 = Trinca(7,7,1)
    trinca19 = Trinca(7,7,2)
    trinca20 = Trinca(7,7,4)
    trinca21 = Trinca(7,7,8)
    trinca22 = Trinca(7,7,9)
    lista6 = [trinca18, trinca19, trinca20, trinca21, trinca22] 

    lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
    lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
    lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
    lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)
    lista_combina_lista12345_com_lista6 = monta_arvore(lista_combina_lista1234_com_lista5, lista6, False)

    print(f'Total de registros: {len(lista_combina_lista12345_com_lista6)}')

    return lista_combina_lista12345_com_lista6
# ====================================
# ====================================
def retorno_linha8(matriz_entrada):
    '''
    0=>(8,0)=[8, 1, 3]  |=> Trincas 3 |=> 
    1=>(8,2)=[1, 3, 6, 9]  |=> Trincas 4 |=> 
    2=>(8,4)=[1, 6, 7]  |=> Trincas 3 |=> 
    3=>(8,5)=[8, 1, 7]  |=> Trincas 3 |=> 
    4=>(8,6)=[8, 1, 3, 9]  |=> Trincas 4 |=> 
    5=>(8,7)=[8, 1, 3, 9]  |=> Trincas 4 |=> =>tipo <class 'int'> 0
    '''
    print(f'\nAnalisando a Linha 8: ', end='')

    #0=>(8,0)=[8, 1, 3]
    trinca1 = Trinca(8,0,8)
    trinca2 = Trinca(8,0,1)
    trinca3 = Trinca(8,0,3)
    lista1 = [trinca1, trinca2, trinca3]

    #1=>(8,2)=[1, 3, 6, 9]
    trinca4 = Trinca(8,2,1)
    trinca5 = Trinca(8,2,3)
    trinca6 = Trinca(8,2,6)
    trinca7 = Trinca(8,2,9)
    lista2 = [trinca4, trinca5, trinca6, trinca7] 

    #2=>(8,4)=[1, 6, 7]
    trinca8 = Trinca(8,4,1)
    trinca9 = Trinca(8,4,6)
    trinca10 = Trinca(8,4,7)
    lista3 = [trinca8, trinca9, trinca10] 

    #3=>(8,5)=[8, 1, 7]
    trinca11 = Trinca(8,5,8)
    trinca12 = Trinca(8,5,1)
    trinca13 = Trinca(8,5,7)    
    lista4 = [trinca11, trinca12, trinca13] 

    #4=>(8,6)=[8, 1, 3, 9]
    trinca15 = Trinca(8,6,8)
    trinca16 = Trinca(8,6,1)
    trinca17 = Trinca(8,6,3)
    trinca18 = Trinca(8,6,9)
    lista5 = [trinca15, trinca16, trinca17, trinca18] 

    #5=>(8,7)=[8, 1, 3, 9]
    trinca19 = Trinca(8,7,8)
    trinca20 = Trinca(8,7,1)
    trinca21 = Trinca(8,7,3)
    trinca22 = Trinca(8,7,9)
    lista6 = [trinca19, trinca20, trinca21, trinca22] 

    lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
    lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
    lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
    lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)
    lista_combina_lista12345_com_lista6 = monta_arvore(lista_combina_lista1234_com_lista5, lista6, False)

    print(f'Total de registros: {len(lista_combina_lista12345_com_lista6)}')

    return lista_combina_lista12345_com_lista6
# ====================================
def retorno_linha1(matriz_entrada):
    '''
    Analisando a Linha 1
    ====================================

    0=>(1,0)=[2, 3, 5, 7]  |=> Trincas 4 |=> 
    1=>(1,1)=[2, 3, 5]  |=> Trincas 3 |=> 
    2=>(1,2)=[2, 3, 4, 5, 7]  |=> Trincas 5 |=> 
    3=>(1,3)=[3, 4, 5, 7]  |=> Trincas 4 |=> 
    4=>(1,6)=[1, 2, 3, 5, 8]  |=> Trincas 5 |=> 
    5=>(1,7)=[1, 2, 3, 5, 8]  |=> Trincas 5 |=> 
    6=>(1,8)=[1, 2]
    '''
    print(f'\nAnalisando a Linha 1: ', end='')

    #0=>(1,0)=[2, 3, 5, 7]
    trinca1 = Trinca(1,0,2)
    trinca2 = Trinca(1,0,3)
    trinca3 = Trinca(1,0,5)
    trinca4 = Trinca(1,0,7)
    lista1 = [trinca1, trinca2, trinca3, trinca4]

    #1=>(1,1)=[2, 3, 5]
    trinca5 = Trinca(1,1,2)
    trinca6 = Trinca(1,1,3)
    trinca7 = Trinca(1,1,5)
    lista2 = [trinca5, trinca6, trinca7] 

    #2=>(1,2)=[2, 3, 4, 5, 7]
    trinca8 = Trinca(1,2,2)
    trinca9 = Trinca(1,2,3)
    trinca10 = Trinca(1,2,4)
    trinca11 = Trinca(1,2,5)
    trinca12 = Trinca(1,2,7)
    lista3 = [trinca8, trinca9, trinca10, trinca11, trinca12] 

    #3=>(1,3)=[3, 4, 5, 7]
    trinca13 = Trinca(1,3,3)
    trinca14 = Trinca(1,3,4)
    trinca15 = Trinca(1,3,5)
    trinca16 = Trinca(1,3,7)
    lista4 = [trinca13, trinca14, trinca15, trinca16] 

    #4=>(1,6)=[1, 2, 3, 5, 8]
    trinca17 = Trinca(1,6,1)
    trinca18 = Trinca(1,6,2)
    trinca19 = Trinca(1,6,3)
    trinca20 = Trinca(1,6,5)
    trinca21 = Trinca(1,6,8)
    lista5 = [trinca17, trinca18, trinca19, trinca20, trinca21] 

    #5=>(1,7)=[1, 2, 3, 5, 8]
    trinca22 = Trinca(1,7,1)
    trinca23 = Trinca(1,7,2)
    trinca24 = Trinca(1,7,3)
    trinca25 = Trinca(1,7,5)
    trinca26 = Trinca(1,7,8)
    lista6 = [trinca22, trinca23, trinca24, trinca25, trinca26] 

    #6=>(1,8)=[1, 2]
    trinca27 = Trinca(1,8,1)
    trinca28 = Trinca(1,8,2)
    lista7 = [trinca27, trinca28] 

    lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
    lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
    lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
    lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)
    lista_combina_lista12345_com_lista6 = monta_arvore(lista_combina_lista1234_com_lista5, lista6, False)
    lista_combina_lista123456_com_lista7 = monta_arvore(lista_combina_lista12345_com_lista6, lista7, False)

    print(f'Total de registros: {len(lista_combina_lista123456_com_lista7)}')

    return lista_combina_lista123456_com_lista7
# ====================================
def retorno_linha2(matriz_entrada):
    '''
    0=>(2,0)=[2, 3, 5]  |=> Trincas 3 |=> 
    1=>(2,1)=[9, 2, 3, 5]  |=> Trincas 4 |=> 
    2=>(2,2)=[2, 3, 4, 5, 9]  |=> Trincas 5 |=> 
    3=>(2,4)=[1, 2, 3, 5]  |=> Trincas 4 |=> 
    4=>(2,5)=[1, 2, 4, 5]  |=> Trincas 4 |=> 
    5=>(2,6)=[1, 2, 3, 5, 6, 9]  |=> Trincas 6 |=> 
    6=>(2,7)=[1, 2, 3, 5, 6, 9]  |=> Trincas 6 |=> =>tipo <class 'int'> 0
    '''
    print(f'\nAnalisando a Linha 2: ', end='')

    #0=>(2,0)=[2, 3, 5]
    trinca1 = Trinca(2,0,2)
    trinca2 = Trinca(2,0,3)
    trinca3 = Trinca(2,0,5)
    lista1 = [trinca1, trinca2, trinca3]

    #1=>(2,1)=[9, 2, 3, 5]
    trinca4 = Trinca(2,1,9)
    trinca5 = Trinca(2,1,2)
    trinca6 = Trinca(2,1,3)
    trinca7 = Trinca(2,1,5)
    lista2 = [trinca4, trinca5, trinca6, trinca7] 

    #2=>(2,2)=[2, 3, 4, 5, 9]
    trinca8 = Trinca(2,2,2)
    trinca9 = Trinca(2,2,3)
    trinca10 = Trinca(2,2,4)
    trinca11 = Trinca(2,2,5)
    trinca12 = Trinca(2,2,9)
    lista3 = [trinca8, trinca9, trinca10, trinca11, trinca12] 

    #3=>(2,4)=[1, 2, 3, 5]
    trinca13 = Trinca(2,4,1)
    trinca14 = Trinca(2,4,2)
    trinca15 = Trinca(2,4,3)
    trinca16 = Trinca(2,4,5)
    lista4 = [trinca13, trinca15, trinca15, trinca16] 

    #4=>(2,5)=[1, 2, 4, 5]
    trinca17 = Trinca(2,5,1)
    trinca18 = Trinca(2,5,2)
    trinca19 = Trinca(2,5,4)
    trinca20 = Trinca(2,5,5)
    lista5 = [trinca17, trinca18, trinca19, trinca20] 

    #5=>(2,6)=[1, 2, 3, 5, 6, 9]
    trinca21 = Trinca(2,6,1)
    trinca22 = Trinca(2,6,2)
    trinca23 = Trinca(2,6,3)
    trinca24 = Trinca(2,6,5)
    trinca25 = Trinca(2,6,6)
    trinca26 = Trinca(2,6,9)
    lista6 = [trinca21, trinca22, trinca23, trinca24, trinca25, trinca26] 

    #6=>(2,7)=[1, 2, 3, 5, 6, 9]
    trinca27 = Trinca(2,7,1)
    trinca28 = Trinca(2,7,2)
    trinca29 = Trinca(2,7,3)
    trinca30 = Trinca(2,7,5)
    trinca31 = Trinca(2,7,6)
    trinca32 = Trinca(2,7,9)    
    lista7 = [trinca27, trinca28, trinca29, trinca30, trinca31, trinca32] 

    lista_combina_lista_e_lista2 = monta_arvore(lista1, lista2, False)
    lista_combina_lista12_com_lista3 = monta_arvore(lista_combina_lista_e_lista2, lista3, False)
    lista_combina_lista123_com_lista4 = monta_arvore(lista_combina_lista12_com_lista3, lista4, False)
    lista_combina_lista1234_com_lista5 = monta_arvore(lista_combina_lista123_com_lista4, lista5, False)
    lista_combina_lista12345_com_lista6 = monta_arvore(lista_combina_lista1234_com_lista5, lista6, False)
    lista_combina_lista123456_com_lista7 = monta_arvore(lista_combina_lista12345_com_lista6, lista7, False)

    print(f'Total de registros: {len(lista_combina_lista123456_com_lista7)}')

    return lista_combina_lista123456_com_lista7
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
def retorna_analise_camada_horizontal(numero_camada, matriz_entrada):
    matrizes_validas_linha0, matrizes_validas_linha1, matrizes_validas_linha2 = retorna_matrizes_validas_camada_horizontal(numero_camada, matriz_entrada)
    
    lista_combinada_mats_linha0_linha1 = monta_arvore(matrizes_validas_linha0, matrizes_validas_linha1, False)
    matrizes_validas_linhas_0e1 = retorna_lista_matrizes_validas(lista_combinada_mats_linha0_linha1, matriz_entrada)
    #imprime_arvore(matrizes_validas_linhas_0e1) 

    lista_combinada_mats_0e1_linha2 = monta_arvore(matrizes_validas_linhas_0e1, matrizes_validas_linha2, False)
    matrizes_validas_linhas_0e1_linha2 = retorna_lista_matrizes_validas(lista_combinada_mats_0e1_linha2, matriz_entrada)
    #imprime_arvore(matrizes_validas_linhas_0e1_linha2)          

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
    #imprime_arvore(matrizes_validas_linha0)

    lista_combinada_linha1 = retorna_arvore_linha(indices_linha[1], matriz_entrada)
    matrizes_validas_linha1 = retorna_lista_matrizes_validas(lista_combinada_linha1, matriz_entrada)
    #imprime_arvore(matrizes_validas_linha1)
    
    lista_combinada_linha2 = retorna_arvore_linha(indices_linha[2], matriz_entrada)
    matrizes_validas_linha2 = retorna_lista_matrizes_validas(lista_combinada_linha2, matriz_entrada)
    #imprime_arvore(matrizes_validas_linha2)
    
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
            lista_trincas = recebe_lista_retorna_trincas(item_lista)
            for trinca in lista_trincas:
                matriz_teste[trinca.linha][trinca.coluna] = trinca.valor

            eh_valida = verifica_matriz_incompleta_esta_valida(matriz_teste)
            if eh_valida and '[]' not in item_lista:
                matrizes_combinadas_validas.append(item_lista)
                contador_matrizes_combinadas_validas += 1
    return matrizes_combinadas_validas       
# ====================================

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
def retorna_arvore_linha(numero_linha, matriz_entrada):
    linha = retorna_posicoes_possibilidades_linha(numero_linha, matriz_entrada)
    print(f'\nAnalisando a Linha {numero_linha}\n====================================')

    lista_final1 = []
    lista_final2 = []
    lista_final3 = []
    lista_final4 = []
    lista_final5 = []

    for k, posicao in enumerate(linha):
        print(f'\n{k}=>{posicao} ', end='')
        trincas = retorna_lista_trincas(posicao)
        print(f' |=> Trincas {len(trincas)} |=> ', end='')
        if k == 0:
            lista_final1.append(trincas)
        elif k == 1:
            lista_final2.append(trincas)
        elif k == 2:
            lista_final3.append(trincas)
        elif k == 3:
            lista_final4.append(trincas)
        elif k == 4:
            lista_final5.append(trincas)
    
    for lista in enumerate(lista_final1):
        for it in lista:
            print(f'=>tipo {type(it)} {str(it)}')    
    for it in lista_final2:
        print(str(it))    
    for it in lista_final3:
        print(str(it))    
    for it in lista_final4:
        print(str(it))    
    for it in lista_final5:
        print(str(it))    

    return lista_final1
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
if __name__ == '__main__':
    inicio()
# ====================================


# ====================================
            